# Copyright 2023 HorusElohim

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from datetime import timedelta

from . import LOGGER
from .. import data, Path, time, typing, version, Emoji


@data.dataclass
class Entity(data.JSONData):
    name: str = data.field(default_factory=str)
    path: Path = data.field(default_factory=Path)
    born_time: int = data.field(default_factory=time.time_ns, compare=False)
    dead_time: int = data.field(default_factory=int)
    auto_save: bool = data.field(default_factory=bool)

    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    @property
    def age(self) -> int:
        return time.time_ns() - self.born_time

    @property
    def code(self) -> str:
        import inspect

        if frame := inspect.currentframe():
            if module := inspect.getmodule(frame):
                return inspect.getsource(module)
        return ""

    def __post_init__(self):
        self.name = self.name if self.name else "Default"
        LOGGER.debug("%s  %s.%s path=%s", Emoji.born, self.class_name, self.name, self.path)

    def __del__(self):
        if self.auto_save:
            try:
                self.dead_time = time.time_ns()
                self.dump_json(self.path / f"{self.__class__.__name__}_{version}.json")
            except Exception as ex:
                if LOGGER:
                    LOGGER.error(f"Exception: {ex}")
        if LOGGER:
            LOGGER.debug("%s  %s.%s age=%s", Emoji.dead, self.class_name, self.name, Entity.format_ns(self.age))

    def move(self, new_path: typing.Union[Path, str]):
        """
        Update the entity's path.

        :param new_path: The new path (as a Path object or a string) to update the entity's path to.
        """
        # Absolute and Relative
        # Update the entity's path
        self.path = self.path.parent / new_path if not Path(new_path).is_absolute() else new_path

    @staticmethod
    def format_ns(ns: int) -> str:
        # Convert nanoseconds to microseconds for timedelta compatibility
        td = timedelta(microseconds=ns / 1000)

        units = [
            (td.days, "d"),
            (td.seconds // 3600, "h"),
            (td.seconds % 3600 // 60, "m"),
            (td.seconds % 60, "s"),
            (td.microseconds // 1000, "ms"),
            (td.microseconds % 1000, "µs"),  # Add microseconds
        ]

        time_str = ":".join(f"{value}{unit}" for value, unit in units if value > 0)

        # Append remaining nanoseconds for durations less than 1 microsecond
        remaining_ns = ns % 1000
        if remaining_ns > 0:
            time_str += f":{remaining_ns}ns"

        return time_str
