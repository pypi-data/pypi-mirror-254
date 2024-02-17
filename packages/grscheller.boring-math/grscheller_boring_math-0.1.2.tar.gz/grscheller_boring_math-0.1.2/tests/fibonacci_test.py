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

from grscheller.boring_math.integer_math import fibonacci

class Test_fibonacci:
    def test_fib(self):
        someFibs = []
        fib0 = 0
        fib1 = 1
        fibs = fibonacci(fib0, fib1)
        fib = next(fibs)
        while(fib < 60):
            someFibs.append(fib)
            fib = next(fibs)
        assert someFibs == [0,1,1,2,3,5,8,13,21,34,55]
