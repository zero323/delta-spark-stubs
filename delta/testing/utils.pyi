import unittest
from typing import Any

class DeltaTestCase(unittest.TestCase):
    warehouse_dir: Any
    spark: Any
    sc: Any
    tempPath: Any
    tempFile: Any
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
