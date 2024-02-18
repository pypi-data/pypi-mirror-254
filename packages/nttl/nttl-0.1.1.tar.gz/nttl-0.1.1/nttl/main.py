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
"""nttl program module"""
import sys
import argparse
import datetime
from pathlib import Path

from nttl import version
from nttl.dt import parse_when, parse_dt
from nttl.data import Action, Entry, load_entries, get_entries_between
from nttl.report import print_report

try:
    from xdg import BaseDirectory
except ImportError:
    BaseDirectory = None


HERE = Path(__file__).absolute().parent
HOME = Path().home()
PROGRAMNAME = 'nttl'
CONFIGDIR = HOME / ".config" / PROGRAMNAME
DATADIR = HOME / ".local" / "share" / PROGRAMNAME

if BaseDirectory is not None:
    CONFIGDIR = Path(BaseDirectory.save_config_path(PROGRAMNAME) or CONFIGDIR)
    DATADIR = Path(BaseDirectory.save_data_path(PROGRAMNAME) or DATADIR)

CONFIGFILE = CONFIGDIR / "config.toml"
DATAFILE = DATADIR / "times.toml"


def error(text, *args, **kwargs):
    print(text, *args, file=sys.stderr, **kwargs)


def get_started_tasks(datafile):
    now = datetime.datetime.now()
    active_tracks = {}
    for entry in sorted(load_entries(datafile)):
        if entry.timestamp > now:
            continue
        if entry.action == Action.START:
            active_tracks[entry.timestamp] = entry
        if entry.action == Action.SWITCH:
            active_tracks = {entry.timestamp: entry}
        if entry.action == Action.STOP:
            if entry.startentry is None:
                active_tracks = {}
                continue
            if entry.startentry not in active_tracks:
                continue
            del active_tracks[entry.startentry]

    for entry in sorted(active_tracks.values()):
        if entry.timestamp > now:
            break
        yield entry


def add_entry_params(parser):
    parser.add_argument('-d', '--description',
                        default='',
                        type=str)
    parser.add_argument('-l', '--label',
                        default=[],
                        action="append",
                        type=str)
    add_when_parameter(parser)


def add_when_parameter(parser):
    parser.add_argument('-w', '--when',
                        type=str,
                        default=None,
                        help="Set the time when this happened. Either as "
                             "absolute time, date+time, or relative. "
                             "A date+time is written as 'YYYY-MM-DD HH:MM:SS', "
                             "time is written as 'HH:MM:SS'. The seconds are "
                             "optional. Relative time is written 'T-2h5m10s'. "
                             "'h', 'm', and 's' can be mixed and combined. If "
                             "you only provide a number (e.g. 'T-5'), 'm' is "
                             "assumed.")


def add_start_end_parameters(parser):
    parser.add_argument('-s', '--start',
                        type=str,
                        default="-1w",
                        help="Start of report period. Relative date, "
                             "absolute date, or day of week in your locale. "
                             "Default is '-1w'.")
    parser.add_argument('-e', '--end',
                        type=str,
                        default="0d",
                        help="End of report period. Relative date, absolute "
                             "date, or day of week in your locale. Default is "
                             "'today'.")


def add_task_id_parameter(parser):
    parser.add_argument('-t', '--task',
                        type=int,
                        default=None,
                        help="Active task id. If not provided, "
                             "all active tasks are stopped.")


def print_status(sourcefile, outputformat, customformat):
    if outputformat == 'text':
        print("Active tasks:")
    elif outputformat == 'json':
        print('[')

    started_tasks = list(get_started_tasks(sourcefile))
    for idx, entry in enumerate(started_tasks):
        assert isinstance(entry.labels, list)
        if outputformat == 'text':
            print(f"({idx+1})",
                  entry.timestamp,
                  entry.description,
                  entry.labels)
        elif outputformat == 'json':
            comma = ','
            if idx+1 >= len(started_tasks):
                comma = ''
            labels = ', '.join('"' + l + '"' for l in entry.labels)
            print(f''' {{"start": "{entry.timestamp}",
"description": "{entry.description}",
"labels": [{labels}]
}}{comma}''')
        elif outputformat == 'csv':
            labels = ",".join(l for l in entry.labels)
            print(f'{entry.timestamp},"{entry.description}","{labels}"')

        elif outputformat == 'custom':
            labels = ', '.join(l for l in entry.labels)
            descr_or_labels = entry.description
            if len(descr_or_labels.strip()) == 0:
                descr_or_labels = labels
            print(customformat.format(timestamp=str(entry.timestamp),
                                      description=str(entry.description),
                                      descr_or_labels=descr_or_labels,
                                      labels=labels))

    if outputformat == 'json':
        print(']')


def run():
    CONFIGDIR.mkdir(exist_ok=True, parents=True)
    DATADIR.mkdir(exist_ok=True, parents=True)

    parser = argparse.ArgumentParser(prog=PROGRAMNAME)
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s ' + version.__version__)
    subparsers = parser.add_subparsers(dest="fn")

    startparser = subparsers.add_parser(Action.START,
                                        help="Start another task.")
    add_entry_params(startparser)

    stopparser = subparsers.add_parser(Action.STOP,
                                       help="Stop an active task.")
    add_entry_params(stopparser)
    add_task_id_parameter(stopparser)

    switchparser = subparsers.add_parser(Action.SWITCH,
                                         help="Switch tasks (stop active, "
                                              "start another)")
    add_entry_params(switchparser)
    add_task_id_parameter(switchparser)

    eventparser = subparsers.add_parser(Action.EVENT,
                                        help="Add an event")
    add_entry_params(eventparser)

    statusparser = subparsers.add_parser('status', help="Show the active tasks")
    statusparser.add_argument('-f', '--format',
                              choices=['text', 'json', 'csv', 'custom'],
                              default='text',
                              help="Output format. 'json', 'csv', 'custom', or "
                                   "'text' (the default).")
    statusparser.add_argument('-c', '--custom',
                              default="{timestamp}: {description} ({labels})",
                              help="The format of the custom format.")

    listparser = subparsers.add_parser('list', help="List all task tracking events")
    add_start_end_parameters(listparser)

    reportparser = subparsers.add_parser('report', help="Show a report about time spent")
    add_start_end_parameters(reportparser)
    reportparser.add_argument('-d', '--description',
                              type=str,
                              default=[],
                              action='append',
                              help="Filter by description. Each -d phrase must "
                                   "be in a tasks description to be included.")
    reportparser.add_argument('-l', '--label',
                              default=[],
                              action='append',
                              help='Filter by label. Each -l label must appear '
                                   'in a task to be included')
    reportparser.add_argument('-x', '--exclude-label',
                              default=[],
                              action='append',
                              help='Exclude activities that have this label. '
                                   'May be provided multiple times.')
    reportparser.add_argument('-f', '--format',
                              choices=['csv', 'text', 'bar', 'gantt'],
                              default='text',
                              help='What format to use. Options are csv or '
                                   'text. "text" is the default.')
    reportparser.add_argument('-g', '--group-by-labels',
                              default=False,
                              action='store_true',
                              help='Group by labels')
    reportparser.add_argument('--resolution',
                              default='1h',
                              help='Resolution for graphs. Default is '
                                   '"%(default)s".')

    args = parser.parse_args()
    if args.fn is None:
        parser.print_help()
        return

    if args.fn in list(Action):
        entry = Entry(parse_when(args.when),
                      args.fn)
        entry.description = args.description
        if args.label is not None:
            entry.labels = args.label

        if args.fn in [Action.STOP, Action.SWITCH]:
            if args.task is not None:
                active_tasks = list(get_started_tasks(DATAFILE))
                entry.startentry = active_tasks[args.task-1].timestamp

        with open(DATAFILE, "a+t", encoding='utf-8') as datafile:
            datafile.write(entry.as_toml())

    if args.fn == 'list':
        time_range = [parse_dt(args.start),
                      parse_dt(args.end)]

        for entry in sorted(get_entries_between(DATAFILE, *time_range)):
            print(entry.timestamp,
                  f"({entry.action})",
                  entry.description,
                  entry.labels)

    if args.fn == 'status':
        print_status(DATAFILE, args.format, args.custom)

    if args.fn == 'report':
        print_report(DATAFILE, args, error=error)
