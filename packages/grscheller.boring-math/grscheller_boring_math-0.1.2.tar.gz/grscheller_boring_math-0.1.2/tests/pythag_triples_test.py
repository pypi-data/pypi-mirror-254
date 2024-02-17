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

from grscheller.boring_math.integer_math import pythag3

class Test_pythag3:
    def test_triples(self):
        for triple in pythag3(40):
            a, b, c = triple
            assert a*a + b*b == c*c
            assert a <= 40

        for triple in pythag3(60, 100):
            a, b, c = triple
            assert a*a + b*b == c*c
            assert 3 <= a <= 60
            assert 4 <= b <= 100
            assert 5 <= c <= 100

    def test_spot_check(self):
        triples = set(pythag3(40))
        assert (3, 4, 5) in triples
        assert (5, 12, 13) in triples
        assert (8, 15, 17) in triples
        assert (23, 264, 265) in triples

        triples = set(pythag3(200, 500))
        assert (23, 264, 265) in triples
        assert (189, 340, 389) in triples
        assert (87, 416, 425) in triples
        assert (33, 544, 545) not in triples
