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

from grscheller.boring_math.integer_math import gcd, lcm, mkCoprime, primes

class Test_simple_ones:
    def test_gcd(self):
        assert gcd(0, 0) == 0   # mathematicaly does not exist
        assert gcd(1, 1) == 1
        assert gcd(1, 5) == 1
        assert gcd(5, 1) == 1
        assert gcd(0, 5) == 5
        assert gcd(21, 0) == 21 
        assert gcd(2, 5) == 1
        assert gcd(5, 2) == 1
        assert gcd(15, 35) == 5
        assert gcd(35, 15) == 5
        assert gcd(2*3*5*7, 3*5*7*11) == 3*5*7
        assert gcd(123454321, 11111) == 11111
        assert gcd(123454321, 1111) == 1

    def test_lcm(self):
        assert lcm(5, 0) == 0
        assert lcm(0, 11) == 0
        assert lcm(0, 0) == 0
        assert lcm(3, 5) == 15
        assert lcm(2*3*25*7, 3*5*11) == 2*3*25*7*11

    def test_mkCoprime(self):
        assert mkCoprime(0, 0) == (0, 0)
        assert mkCoprime(5, 0) == (1, 0)
        assert mkCoprime(0, 4) == (0, 1)
        assert mkCoprime(1, 4) == (1, 4)
        assert mkCoprime(6, 15) == (2, 5)
        assert mkCoprime(2*3*4*5, 3*4*5*11) == (2, 11)

    def test_primes(self):
        generated = list(primes(10, 50))
        assert generated == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
