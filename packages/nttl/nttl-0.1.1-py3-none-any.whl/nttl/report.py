# Copyright (C)  2024  Robert Labudda
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Time reporting"""
import sys
import csv
import datetime

from nttl.data import Action, Activity, Entry, get_entries_between
from nttl.dt import parse_dt, parse_timedelta


BARS = ' ▂▄▆█'
BAR_WIDTH = 4
SLICES = '▏▎▍▌▋▊▉█'


def ignore_error(*_):
    # dummy function to ignore errors
    pass


def print_report(sourcefile, args, error=None):
    if error is None:
        error = ignore_error
    now = datetime.datetime.now()
    time_range = [parse_dt(args.start),
                  parse_dt(args.end)]

    started_tasks = {}
    activities = []
    all_labels = set()

    # collect all start/(stop|switch) pairs
    for entry in get_entries_between(sourcefile, *time_range):
        if entry.labels is not None:
            all_labels.update(set(entry.labels))

        if entry.action == Action.STOP:
            if entry.startentry is None:
                for started in started_tasks.values():
                    activities.append(Activity(started, entry))
                started_tasks = {}
                continue

            if entry.startentry not in started_tasks:
                error("Task ended but did not start in report period")
                continue

            activities.append(Activity(started_tasks[entry.startentry], entry))
            del started_tasks[entry.startentry]

        if entry.action == Action.START:
            started_tasks[entry.timestamp] = entry

        if entry.action == Action.SWITCH:
            for started in started_tasks.values():
                activities.append(Activity(started,
                                           Entry(entry.timestamp, Action.STOP)))
            started_tasks = {entry.timestamp: entry}

    # some tasks are still running? pretend they're done now
    for entry in started_tasks.values():
        activities.append(Activity(entry, Entry(now, Action.STOP)))

    # accumulate by labels
    by_labels = {label: [] for label in all_labels}

    filtered_sorted = []
    for activity in activities:
        labels = activity.get_labels()
        if len(args.label) > 0 and not all(l in labels for l in args.label):
            continue
        if len(args.description) > 0 and not all(d in activity.start.description for d in args.description):
            continue
        # accumulate by labels
        for label in activity.get_labels():
            by_labels[label].append(activity)

        filtered_sorted.append(activity)
    filtered_sorted.sort()

    # don't show labels without any registered activity
    by_labels = {lbl: act
                 for lbl, act in by_labels.items()
                 if len(act) > 0}
    for lbl in args.exclude_label:
        if lbl not in by_labels:
            continue
        del by_labels[lbl]

    if args.group_by_labels:
        lines = [[label, sum([a.duration() for a in activities],
                             start=datetime.timedelta(0))]
                  for label, activities in by_labels.items()]
        lines.sort()
    else:
        lines = [[a.start.timestamp,
                  a.end.timestamp,
                  a.duration(),
                  a.description(),
                  a.get_labels()] for a in filtered_sorted]

    if args.format == 'csv':
        writer = csv.writer(sys.stdout)
        if args.group_by_labels:
            for line in lines:
                writer.writerow([line[0], str(line[1])])
        else:
            for line in lines:
                line[-1] = ','.join(line[-1])
                writer.writerow(line)

    elif args.format == 'bar':
        if len(activities) == 0:
            return
        labels = [lbl for lbl in sorted(by_labels.keys())]
        spacing = [max(len(lbl), BAR_WIDTH) for lbl in labels]
        durations = [int(sum([a.duration() for a in activities],
                             start=datetime.timedelta(0)).total_seconds())
                     for _, activities in sorted(by_labels.items())]
        # durations is in seconds per label
        # convert to (full hours, remaining minutes)
        durations = [(d // 3600,  (d % 3600)//60)
                     for d in durations]
        max_hours = max(d[0] for d in durations) + 1
        for line in range(0, max_hours+1):
            hour = max_hours - line
            print(f" {hour: >3}  │ ", end="") 
            for idx, label in enumerate(labels):
                pad = spacing[idx]
                if durations[idx][0] >= hour:
                    symbol = BARS[4]
                    if durations[idx][0] == hour:
                        symbol = BARS[int(4*durations[idx][1]/60.0)]
                    pad = (pad-BAR_WIDTH)//2
                    print(' '*(pad+1) + symbol*BAR_WIDTH + ' '*(pad+1), end="")
                    if spacing[idx] % 2 == 1:
                        print(' ', end="")
                else:
                    print(' '*(pad + 2), end="")
            print()

        # x-axis
        print("──────┼─" + "─"*(sum([max(BAR_WIDTH, len(l))+2 for l in labels])))
        print("      │ ", end="")
        for idx, label in enumerate(labels):
            pad = max(0, BAR_WIDTH-len(label))
            print(" "*max(1, pad) + label + " "*max(1, pad), end="")
        print()

    elif args.format == 'gantt':
        if len(activities) == 0:
            return
        start = min(a.start.timestamp for a in activities)
        end = max(a.end.timestamp for a in activities)
        granularity = parse_timedelta(args.resolution)
        ticks = int((end - start).total_seconds() // granularity.total_seconds()) + 2
        max_lbl_len = max(len(lbl) for lbl in by_labels.keys())+1
        for label, activities in sorted(by_labels.items()):
            print(" " + label, end="")
            print(" "*max(1, max_lbl_len-len(label)) + "│", end="")
            dt = start
            last_dt = start
            while dt < end:
                is_active = any(a.overlaps(last_dt, dt) for a in activities)
                symbol = " "
                if is_active:
                    symbol = "█"
                print(symbol, end="")
                last_dt = dt
                dt += granularity
            print()

        print("─"*(max_lbl_len+1) + "┼", end="")
        print("─"*(ticks))

        # hours x-axis
        print(" "*(max_lbl_len+1) + "│", end="")
        dt = start
        counter = 0
        while dt < end:
            if counter % 8 == 0:
                print("└ " + dt.strftime("%H:%M"), end=" ")
            dt += granularity
            counter += 1
        print()

        # dates x-axis
        print(" "*(max_lbl_len+1) + "│", end="")
        dt = start
        overshoot = 0
        last_date = None
        while dt < end:
            if dt.hour == 0 and last_date != dt.date():
                last_date = dt.date()
                text = "└ " + dt.strftime("%Y-%m-%d") + " "
                overshoot = len(text)
                print(text, end="")
            elif overshoot > 0:
                overshoot -= 1
            else:
                print(" ", end="")
            dt += granularity

        print()

    else:
        if args.group_by_labels:
            start = filtered_sorted[0].start.timestamp.strftime("%x")
            end = filtered_sorted[-1].end.timestamp.strftime("%x")
            print(f"{start} --- {end}")
            for line in lines:
                print(f"{line[0]}    {line[1]}")
        else:
            day = None
            for line in lines:
                if line[0].day != day:
                    day = line[0].day
                    print(line[0].strftime("%x"))
                start = line[0].strftime("%H:%M")
                end = line[1].strftime("%H:%M")
                labels = ", ".join(line[-1])
                description = line[3]
                print(f"  {start} - {end}    {labels}    {description}")
