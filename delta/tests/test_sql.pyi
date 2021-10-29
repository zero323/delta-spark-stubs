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

class DeltaSqlTests(DeltaTestCase):
    def setUp(self) -> None: ...
    def test_vacuum(self) -> None: ...
    def test_describe_history(self) -> None: ...
    def test_generate(self) -> None: ...
    def test_convert(self) -> None: ...
    def test_ddls(self) -> None: ...
