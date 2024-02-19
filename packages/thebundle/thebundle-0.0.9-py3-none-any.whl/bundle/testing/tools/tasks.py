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


import logging
from pathlib import Path
from functools import wraps
import asyncio
from typing import Any

from ...core import data, tasks
from . import cprofile_decorator, assert_instance_identity, assert_compare

LOGGER = logging.getLogger(__name__)


@data.dataclass
class TestTaskSync(tasks.Task):
    born_time: int = 1

    def exec(self):
        return self.name


@data.dataclass
class TestTaskAsync(tasks.Task.Async):
    born_time: int = 1

    async def exec(self):
        return self.name


class TestTask:
    Sync: TestTaskSync = TestTaskSync
    Async: TestTaskAsync = TestTaskAsync


def task_decorator(
    expected_result: Any = None,
    cprofile_dump_dir: Path | None = None,
):
    def decorator(test_func):
        @wraps(test_func)
        def wrapper(*args, **kwds):
            task = test_func(*args, **kwds)
            LOGGER.debug(f"testing {task=}")

            assert_instance_identity(task, tasks.Task.Base)

            @cprofile_decorator(cprofile_dump_dir=cprofile_dump_dir)
            async def task_execution_async():
                return await task()

            @cprofile_decorator(cprofile_dump_dir=cprofile_dump_dir)
            def task_execution_sync():
                return task()

            # Execute task and assert based on task type
            if isinstance(task, tasks.AsyncTask):
                result = asyncio.run(task_execution_async())
            else:
                result = task_execution_sync()

            assert_compare(expected_result, result)

        return wrapper

    return decorator
