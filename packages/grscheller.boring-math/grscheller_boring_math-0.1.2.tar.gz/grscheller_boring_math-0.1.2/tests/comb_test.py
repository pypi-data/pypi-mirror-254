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

import math
from grscheller.boring_math.integer_math import comb

class Test_comb:
    def test_edge_cases(self):
        assert comb(0, 0) == 1
        assert comb(0, 1) == 0
        assert comb(4, 0) == 1
        assert comb(0, 5) == 0
        assert comb(4, 5) == 0

        try:
            comb(5, 3)
        except ValueError:
            assert False
        else:
            assert True

        try:
            comb(5, -3)
        except ValueError:
            assert True
        else:
            assert False

        try:
            comb(-5, 3)
        except ValueError:
            assert True
        else:
            assert False

        try:
            comb(-5, -3)
        except ValueError:
            assert True
        else:
            assert False

        try:
            comb(-5, 0)
        except ValueError:
            assert True
        else:
            assert False

        try:
            comb(0, -3)
        except ValueError:
            assert True
        else:
            assert False

    def test_small(self):
        assert comb(5, 0) == 1
        assert comb(5, 1) == 5
        assert comb(5, 2) == 10
        assert comb(5, 2) == 10
        assert comb(5, 3) == 10
        assert comb(5, 4) == 5
        assert comb(5, 5) == 1
        assert comb(20, 4) == 20*19*18*17/(4*3*2*1)
        assert comb(37, 7) == comb(37, 37 - 7)
        assert comb(31, 7) == comb(30, 6) + comb(30, 7)

    def test_with_math_version(self):
        assert comb(11, 8) == math.comb(11, 8)
        assert comb(211, 80) == math.comb(211, 80)
        assert comb(514, 213) == math.comb(514, 213)
        assert comb(300, 299) == math.comb(300, 299) == 300
        assert comb(2000, 60) == math.comb(2000, 60)
        assert comb(20001, 601) == math.comb(20001, 601)
        assert comb(200012, 6012) == math.comb(200012, 6012)
        assert comb(2000, 4) == math.comb(2000, 4)
        assert comb(2001, 30) == math.comb(2001, 30)
        assert comb(2002, 200) == math.comb(2002, 200)
        assert comb(2003, 1000) == math.comb(2003, 1000)

    def test_paramenters(self):
        assert comb(3000, 45) == comb(3000, 45, 1, 1)
        assert comb(1300, 450) == comb(1300, 450, 2, 2)
        assert comb(13000, 454) == comb(13000, 454, 10, 6)
        assert comb(20000, 15) == comb(20000, 15, 5, 11) == math.comb(20000, 15)
        assert comb(20, 15) == comb(20, 15, 50, 110) == math.comb(20, 15)
