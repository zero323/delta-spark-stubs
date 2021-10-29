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

from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject  # type: ignore[import]
from pyspark.sql.utils import CapturedException

class DeltaConcurrentModificationException(CapturedException): ...
class ConcurrentWriteException(CapturedException): ...
class MetadataChangedException(CapturedException): ...
class ProtocolChangedException(CapturedException): ...
class ConcurrentAppendException(CapturedException): ...
class ConcurrentDeleteReadException(CapturedException): ...
class ConcurrentDeleteDeleteException(CapturedException): ...
class ConcurrentTransactionException(CapturedException): ...
