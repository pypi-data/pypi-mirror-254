# Copyright 2023-2024 Geoffrey R. Scheller
#
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

from grscheller.boring_math.integer_math import ackermann

class Test_ackerman:
    def test_ack(self):
        assert ackermann(0, 0) == 1
        assert ackermann(0, 5) == 6
        assert ackermann(1, 0) == 2
        assert ackermann(1, 1) == 3
        assert ackermann(1, 2) == 4
        assert ackermann(1, 3) == 5
        assert ackermann(1, 4) == 6
        assert ackermann(1, 5) == 7
        assert ackermann(1, 6) == 8
        assert ackermann(1, 7) == 9
        assert ackermann(1, 8) == 10
        assert ackermann(1, 27) == 29      # inferring from patterns
        assert ackermann(2, 0) == 3
        assert ackermann(2, 1) == 5
        assert ackermann(2, 2) == 7
        assert ackermann(2, 3) == 9
        assert ackermann(2, 4) == 11
        assert ackermann(2, 5) == 13
        assert ackermann(2, 6) == 15
        assert ackermann(2, 13) == 29      # inferring from patterns
        assert ackermann(3, 0) == 5
        assert ackermann(3, 1) == 13
        assert ackermann(3, 2) == 29       # inferring from patterns
        assert ackermann(3, 3) == 61       # inferring from patterns
        assert ackermann(3, 4) == 125
        assert ackermann(3, 8) == 2045     # not hand computed
        assert ackermann(4, 0) == 13
      # assert ackermann(4, 1) == 65533    # not hand computed!
        assert ackermann(0, 21) == 22
        assert ackermann(4, 0) == ackermann(3, 1)
        assert ackermann(3, 7) == ackermann(2, ackermann(3, 6))
