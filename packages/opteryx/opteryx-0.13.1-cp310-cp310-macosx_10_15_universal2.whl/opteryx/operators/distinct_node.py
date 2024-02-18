# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Distinct Node

This is a SQL Query Execution Plan Node.

This Node eliminates duplicate records.
"""
import time
from typing import Generator

import pyarrow
from pyarrow import concat_tables

from opteryx.models import QueryProperties
from opteryx.operators import BasePlanNode
from opteryx.third_party.pyarrow_ops import drop_duplicates


class DistinctNode(BasePlanNode):
    def __init__(self, properties: QueryProperties, **config):
        super().__init__(properties=properties)
        self._distinct_on = config.get("on")
        if self._distinct_on:
            self._distinct_on = [col.schema_column.identity for col in self._distinct_on]

    @property
    def config(self):  # pragma: no cover
        return ""

    @property
    def greedy(self):  # pragma: no cover
        return True

    @property
    def name(self):  # pragma: no cover
        return "Distinction"

    def execute(self) -> Generator[pyarrow.Table, None, None]:
        morsels = self._producers[0]  # type:ignore

        start = time.monotonic_ns()
        dropped = drop_duplicates(
            concat_tables(morsels.execute(), promote_options="none"), self._distinct_on
        )
        self.statistics.time_distincting += time.monotonic_ns() - start

        yield dropped
