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

from functools import wraps


LOGGER = logging.getLogger(__name__)


def assert_instance_identity(instance, class_type):
    assert not isinstance(instance, type), f"{instance} must be an Instance, not a Class"
    assert issubclass(type(instance), class_type), f"The class {type(instance)=} must be a subclass of {class_type=}"


def assert_compare(ref: object, tmp: object) -> None:
    """Compare the content of two files."""
    assert (
        ref == tmp
    ), f"""        

ASSERT COMPARE 

REF: {ref.__class__=}:\n"{ref}" 

--
TEST:  {tmp.__class__=}:\n"{tmp}"

"""
