#
# Copyright 2021 zero323
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from delta.testing.utils import DeltaTestCase as DeltaTestCase
from py4j.java_gateway import JVMView as JVMView  # type: ignore[import]
from typing import Any

class DeltaExceptionTests(DeltaTestCase):
    jvm: Any
    def setUp(self) -> None: ...
    def test_capture_concurrent_write_exception(self) -> None: ...
    def test_capture_metadata_changed_exception(self) -> None: ...
    def test_capture_protocol_changed_exception(self) -> None: ...
    def test_capture_concurrent_append_exception(self) -> None: ...
    def test_capture_concurrent_delete_read_exception(self) -> None: ...
    def test_capture_concurrent_delete_delete_exception(self) -> None: ...
    def test_capture_concurrent_transaction_exception(self) -> None: ...
