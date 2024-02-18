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
"""Data model classes"""
import enum
import datetime
import tomllib
import logging
from pathlib import Path
from dataclasses import dataclass

from nttl.dt import dt_as_str


TOML_TABLE_DT_FORMAT = "%Y-%m-%dT%H-%M-%S"


class Action(enum.StrEnum):
    START = 'start'
    STOP = 'stop'
    SWITCH = 'switch'
    EVENT = 'event'


@dataclass
class Entry:
    timestamp: datetime.datetime
    action: str
    description: str = ''
    labels: list[str]|None = None
    startentry: datetime.datetime|None = None

    def __post_init__(self):
        if self.labels is None:
            self.labels = []

    def as_toml(self):
        lines = ['[' + dt_as_toml_table_str(self.timestamp) + ']',
                 'action = "' + self.action + '"']

        if len(self.description) > 0:
            text = self.description
            wrap = '"'
            if "\n" in text:
                wrap = "'''"
            elif "'" not in text:
                wrap = "'"
            elif '"' in text:
                text = text.replace('"', '\\"')
            lines += ['description = ' + wrap + text + wrap]

        assert self.labels is not None
        labels = {label.strip()
                  for label in self.labels
                  if label is not None and len(label.strip()) > 0}
        if len(labels) > 0:
            lines += ['labels = ' + repr(sorted(list(labels)))]

        if self.action == Action.STOP and self.startentry is not None:
            lines += ['startentry = ' + dt_as_str(self.startentry)]
        return "\n".join(lines) + "\n\n"

    def __lt__(self, other):
        return self.timestamp < other.timestamp


def dt_as_toml_table_str(value):
    return value.strftime(TOML_TABLE_DT_FORMAT)


def toml_table_str_as_dt(value):
    return datetime.datetime.strptime(value, TOML_TABLE_DT_FORMAT)


class Activity:
    """The time span of a task"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if end < start:
            self.start, self.end = end, start

    def get_labels(self):
        return list(sorted(set(self.start.labels) | set(self.end.labels)))

    def duration(self):
        return self.end.timestamp - self.start.timestamp

    def __contains__(self, dt):
        """Return True if dt is between start and end"""
        return self.start.timestamp <= dt <= self.end.timestamp

    def description(self):
        return ' '.join([a.description
                         for a in [self.start, self.end]
                         if len(a.description) > 0])

    def __lt__(self, other):
        return self.start < other.start

    def overlaps(self, start, end):
        if isinstance(start, Entry):
            start = start.timestamp
        if isinstance(end, Entry):
            end = end.timestamp
        if end < start:
            end, start = start, end
        mystart = self.start.timestamp
        myend = self.end.timestamp
        return any([
            start >= mystart and end <= myend,
            mystart >= start and myend <= end,
            start >= mystart and start <= myend,
            mystart >= start and mystart <= end,
            end <= myend and end >= mystart,
            myend <= end and myend >= start,
            ])


def load_entries(datafile):
    datafile = Path(datafile)
    if not datafile.is_file():
        return

    with open(datafile, "rb") as datafile:
        raw = tomllib.load(datafile)

    for key, data in raw.items():
        try:
            timestamp = toml_table_str_as_dt(key)
        except ValueError:
            logging.warning(f"Not a timestamp: {key}")
            continue
        entry = Entry(timestamp,
                      data['action'],
                      data.get('description', ''),
                      data.get('labels', None),
                      data.get('startentry', None))
        yield entry


def get_entries_between(datafile, start, end):
    for entry in sorted(load_entries(datafile)):
        if entry.timestamp.date() < start:
            continue
        if entry.timestamp.date() > end:
            break

        yield entry
