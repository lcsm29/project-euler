# Solutions for [Project Euler](https://projecteuler.net/)
These are my solutions for [Project Euler problems](https://projecteuler.net/archives). I've listed many languages in the About section on the right. However, I can barely code in Python and absolutely nothing in any other language at this moment, since I've started coding about 2 months ago. Hence, that's more like a wishlist than an actual description, at least for now.

All code in this repo is runnable, and gives you a comparison of the execution times of each implementation (overall execution times of each implementation for predetermined number of iterations, as well as min/avg/max of single run). It is tested whether the solution provides a correct answer for the given variable, but may produce an error on different variable. I'm planning to add more testing.

Main files on each folder (e.g. [main.py](https://github.com/lcsm29/project-euler/blob/main/py/main.py)) will run every function implemented on every problems I've solved so far. By default, each problem takes about a second to finish the entire iterations on my computer, so it'll take about a couple of minutes to run if I ever write the solutions for every problems. Right now, it takes 3 seconds.

## Current Progress
| Languages                                                                      | Progress          |
| ------------------------------------------------------------------------------ | ----------------- |
| [Python](https://github.com/lcsm29/project-euler/tree/main/py)                 | 8 / 747           |
| [C](https://github.com/lcsm29/project-euler/tree/main/c)                       | 0 / 747           |
| [C++](https://github.com/lcsm29/project-euler/tree/main/cpp)                   | 0 / 747           |
| [C#](https://github.com/lcsm29/project-euler/tree/main/cs)                     | 0 / 747           |
| [F#](https://github.com/lcsm29/project-euler/tree/main/fs)                     | 0 / 747           |
| [Go](https://github.com/lcsm29/project-euler/tree/main/go)                     | 0 / 747           |
| [Haskell](https://github.com/lcsm29/project-euler/tree/main/hs)                | 0 / 747           |
| [Java](https://github.com/lcsm29/project-euler/tree/main/java)                 | 0 / 747           |
| [JavaScript](https://github.com/lcsm29/project-euler/tree/main/js)             | 0 / 747           |
| [PHP](https://github.com/lcsm29/project-euler/tree/main/php)                   | 0 / 747           |
| [Ruby](https://github.com/lcsm29/project-euler/tree/main/rb)                   | 0 / 747           |
| [SQL](https://github.com/lcsm29/project-euler/tree/main/sql)                   | 0 / 747           |


## Scoreboard
This section is not implemented yet, but it's for the speed comparison of each languages.

### Average execution time (in nanoseconds, unless specified) (lower is better)
This table shows how much nanoseconds it took for the fastest algo to complete one iteration on average. I haven't implemented the auto-update feature yet (except for Python), but once implemented, running main files on each folder (e.g. [main.py](https://github.com/lcsm29/project-euler/blob/main/py/main.py)) will trigger the automatic update of this table.
| Problems  | py         | c          | cpp        | cs         | fs         | go         | hs         | java       | js         | php        | rb         | sql        |
| --------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 1         |[        800 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0001_multiples_of_3_and_5.py)|            |            |            |            |            |            |            |            |            |      1,043 |            |
| 2         |[      2,023 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0002_even_fibonacci_numbers.py)|            |            |            |            |            |            |            |            |            |            |            |
| 3         |[    307,434 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0003_largest_prime_factor.py)|            |            |            |            |            |            |            |            |            |            |            |
| 4         |[    548,254 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0004_largest_palindrome_product.py)|            |            |            |            |            |            |            |            |            |            |            |
| 5         |[     50,945 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0005_smallest_multiple.py)|            |            |            |            |            |            |            |            |            |            |            |
| 6         |[        302 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0006_sum_square_difference.py)|            |            |            |            |            |            |            |            |            |            |            |
| 7         |[   10,263μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0007_10001st_prime.py)|            |            |            |            |            |            |            |            |            |            |            |
| 8         |[    1,666μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0008_largest_product_in_a_series.py)|            |            |            |            |            |            |            |            |            |            |            |
| 9         |            |            |            |            |            |            |            |            |            |            |            |            |
| 10        |            |            |            |            |            |            |            |            |            |            |            |            |

### Number of Iterations (higher is better)
This table shows how much iterations it computes for about a second. The main file not just runs the fastest algo, but runs every implementations. Thus, doing poorly on some algo could hamper the result greatly, even if the language is pretty fast on most implementations.
| Problems  | py         | c          | cpp        | cs         | fs         | go         | hs         | java       | js         | php        | rb         | sql        |
| --------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 1         |     50,000 |            |            |            |            |            |            |            |            |            |      4,000 |            |
| 2         |    150,000 |            |            |            |            |            |            |            |            |            |            |            |
| 3         |      1,500 |            |            |            |            |            |            |            |            |            |            |            |
| 4         |        300 |            |            |            |            |            |            |            |            |            |            |            |
| 5         |     20,000 |            |            |            |            |            |            |            |            |            |            |            |
| 6         |     50,000 |            |            |            |            |            |            |            |            |            |            |            |
| 7         |        100 |            |            |            |            |            |            |            |            |            |            |            |
| 8         |        600 |            |            |            |            |            |            |            |            |            |            |            |
| 9         |            |            |            |            |            |            |            |            |            |            |            |            |
| 10        |            |            |            |            |            |            |            |            |            |            |            |            |
