# NTTL

**N**o **T**ime **T**o **L**ose, a tiny command line (work) time tracker
with basic report capabilities and a plain text data storage format.


## Tracking Time

To start tracking the time you spend on a task, simply run

```bash
    nttl start
```

To see what you’re currently tracking, run

```bash
    nttl status
```

Once you’re done, run

```bash
    nttl stop
```

To list the measured time spans, run

```bash
    nttl list
```

`nttl` might then output something like this, indicating a time period of
work between 07:32 and 08:57 on 2024-01-28.

```
    2024-01-28 07:32:10 (start)  []
    2024-01-28 08:57:41 (stop)  []
```


If you switch to a new activity, it would be very annoying to have to run
`nttl stop` and `nttl start`. Instead you can use

```bash
    nttl switch
```

There’s also the `event` command, but that only makes sense when you use
labels and descriptions:


## Labels and Descriptions

For `start`, `stop`, `switch`, and `event` you can provide *labels* and a
*description* to specify what exactly you’re working on, like this:

```bash
    nttl start -l work -l programming -d "Adding a new feature to Blarp"
```

This will add the labels `work` and `programming` to the time span that
you’re tracking. This is very useful once you’re getting to the reporting
side of things:

## Time Reports

`nttl` can report the time spent in the three human-readable formats and
one for integration with other programs:

 - Gantt chart, a textual Gantt chart of time spent grouped by labels
 - Bar chart, a textual bar chart of time spent grouped by labels
 - Text report, just a listing grouped by time or labels
 - `CSV` file format

You can tell `nttl` to only include activities with certain labels in the
report with `--label` (or `-l`), or exclude activities that have certain
labels with `--exclude-label` (or `-x`). Both parameters, `-l` and `-x`,
may be provided multiple times.

To select the time window for which to create a report, see Time range
selection:

### Time range selection

The `--start` and `--end` parameters can be used to select the time range
for which a `report` (or `list`) should be created. Their default values
will create a time report for the last seven days.

Both `--start` and `--end` have a short form: `-s` and `-e` respectively.

You can express times in two different ways: absolute and relative.

#### Absolute time selection

Absolute uses the ISO date format and looks like this:

```bash
    nttl report --start "2023-11-28 12:00" --end "2023-12-31 23:59"
```

This would create a report for the time between 2023-11-28 and the end of
the year 2023.

If you only provide a time (e.g. `07:23`), `nttl` assumes you meant "today" at
that time.

If you only provide a date (e.g. `2023-11-29`), `nttl` assumes you meant
`00:00` (midnight) of that date.


#### Relative time selection

You can specify points in time relative to "now" by prefixing the `-s` or
`-e` parameter with `T` followed by, for example:

 - `+20s`, 20 seconds later
 - `+5m`, 5 minutes later
 - `-2h`, 2 hours earlier
 - `-1d`, 1 day earlier
 - `+2w`, 2 weeks later

These can be combined to express, for example, "two weeks and two hours ago": `-2w2h`.

Example, request the report for the last 7 days, excluding today:

```bash
    nttl report --start "T-7d" --end "T-1d"
```

#### Day of week

For the `--start` and `--end` parameters you may also provide the name of a
day of the week in your locale. For example, if your computer is set to
Dutch and you want to show everything since the last Friday, you could run

```bash
    nttl report --start Vrijdag
```

The short version of the day of the week is also understood (e.g. `vr.` in
this example).

No matter what your locale is set to, English weekdays are always
understood.


#### Today

You can use the phrase `today` in both `--start` and `--end`. But it's
usually faster to write the equivalent `T0`.


### Textual report

The textual report is the default, but you can request it explicitly with

```bash
    nttl report -f text
```

The output might look like this:

```
    2024-01-03
      07:30 - 08:15    emails, work    
      08:15 - 08:30    meeting, work    weekly team meeting
      08:30 - 08:43    break    
      08:43 - 10:00    bigProject1, programming, work    
      10:00 - 10:35    bigProject1, meeting, work    project meeting
      10:35 - 12:00    bigProject1, programming, work    
      12:00 - 12:35    break, lunch    
      12:35 - 14:30    otherProject, programming, work    going home earlier
```

You can see the time spans sorted by day and time followed by labels
and description.


### Gantt chart report

This report will produce a textual Gantt chart of time spent on activities
grouped by labels. With the previous textual report in mind, a Gantt chart
report would look like this:

```
     bigProject1  │               ████████████████████████████████████████                             
     break        │            ████                                      ████████                      
     emails       │██████████                                                                          
     lunch        │                                                      ████████                      
     meeting      │         ████                 ████████                                              
     otherProject │                                                             ███████████████████████
     programming  │               ████████████████      ██████████████████      ███████████████████████
     work         │█████████████  ████████████████████████████████████████      ███████████████████████
    ──────────────┼─────────────────────────────────────────────────────────────────────────────────────
                  │└ 07:30 └ 08:10 └ 08:50 └ 09:30 └ 10:10 └ 10:50 └ 11:30 └ 12:10 └ 12:50 └ 13:30 └ 14:10 
                  │
```

By default the X-axis will be 1 hour per character, but you can provide a
`--resolution` parameter to change it. The Gantt chart above was created
with `--resolution 5m` to have 5 minutes per character.


### Bar chart report

This report will produce a textual bar chart of time spent on activities
grouped by labels. With the previous Gantt chart and textual report in
mind, the bar chart would look like this:

```
       7  │                                                                              
       6  │                                                                              
       5  │                                                                         ████ 
       4  │                                                               ▄▄▄▄      ████ 
       3  │     ▂▂▂▂                                                      ████      ████ 
       2  │     ████                                                      ████      ████ 
       1  │     ████                                         ▆▆▆▆         ████      ████ 
       0  │     ████      ▆▆▆▆    ▄▄▄▄   ▄▄▄▄    ▆▆▆▆        ████         ████      ████ 
    ──────┼──────────────────────────────────────────────────────────────────────────────
          │  bigProject1  break  emails  lunch  meeting  otherProject  programming  work
```

The Y-axis is 1 hour per line. This can not be changed at the moment.


## Advanced Usage

### Modified 'Now'

Sometimes you will only be able to `start`, `stop`, or `switch` after the
fact or even before the fact (e.g. when you know you will be in a meeting
in 5 minutes).

To express that, you can use the `--when` (or short `-w`) parameter to
modify the time when that action (`start`, `stop`, `switch`) should be
registered. `--when` accepts both absolute and relative time.

For example, if you have been interrupted in your work by an impromptu
meeting, you could run this after the 15 minutes meeting:

```bash
    nttl switch -l meeting -l work -w "T-15m"
    nttl switch -l work -l programming
```

### Multiple tasks

`nttl` can track multiple tasks at the same time. For example, you could
run

```bash
    nttl start -l work
    nttl start -l meeting
```

At which point `nttl status` would show two active tasks:

```
    Active tasks:
    (1) 2024-01-05 08:12:13  ['work']
    (2) 2024-01-05 08:12:14  ['meeting']
```

Just running `nttl stop` or `nttl switch` would stop the tracking of all
active tasks.  
To only stop one of the running tasks, use the `--task` (or short `-t`)
parameter.

For example, to stop tracking of the meeting, run

```bash
    nttl stop -t 2
```

The first task, labelled `work`, would remain active.

At the moment `-t` does not work for `switch`.


### Events

`nttl` supports an additional action to `start`, `stop`, and `switch`:
`event`. This can be useful when integrating `nttl` with your desktop
environment.

For example, when you lock your screen the desktop environment
could call `nttl event -d "Lock screen"`.

Or you could have a git hook set up to call `nttl event -d "git push"`.

Events can be useful if you want to have checkpoints in your daily
activities to be able to reconstruct the exact time of when you left your
desk or when you completed a task without having to call `nttl` with
`switch` or `start`/`stop` all the time.


### Status Display in Desktop Environment

You can utilise `nttl status` with its formats (`json`, `csv`, `custom`
text) to integrate the current status of tracked tasks into your desktop
environment.

For example, an integration into `sway` with `waybar` could work by adding
this to your `waybar` configuration file:

```json
    "custom/nttl": {
        "format": " {} ",
        "interval": 1,
        "exec-if": "test $(nttl status -f csv 2> /dev/null | wc -l) -gt 0",
        "exec": "nttl status -f custom -c '{description}, {labels}' | head -n 1"
    }
```

It would verify that at least one task is being tracked, by counting the
lines of the `nttl status` export as `csv`, and if there is a task running,
the custom format is used as the label in the task bar.


## Data Storage

The data file is stored in your home directory at
`.local/share/nttl/times.toml` and uses the [TOML](https://toml.io/) file
format.

`nttl` only accesses the data file while running, so you can manually edit
that file in any text editor at any other point in time without affecting
`nttl`.


## Installation

To install `nttl`, it’s probably best to use pip:

```bash
    pip install nttl
```

Alternatively you can clone the git repository and install `nttl` like
this:

```bash
    git clone https://codeberg.org/vonshednob/nttl
    cd nttl
    python setup.py install
```


## License

Copyright (C) 2024 Robert Labudda <mailto:contact+nttl@vonshednob.cc>.

This program is free software: you can redistribute it and/or modify
it under the terms of the [GNU General Public License](LICENSE) as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
[GNU General Public License](LICENSE) for more details.

You should have received a copy of the [GNU General Public License](LICENSE)
along with this program.  If not, see <https://www.gnu.org/licenses/>.

