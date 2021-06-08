# Solutions for [Project Euler](https://projecteuler.net/)
These are my solutions for [Project Euler problems](https://projecteuler.net/archives). I've listed many languages in the About section on the right. However, I can barely code in Python and absolutely nothing in any other language at this moment, since I've started coding about 2 months ago. Hence, that's more like a wishlist than an actual description, at least for now.

All code in this repo is runnable, and gives you a comparison of the execution times of each implementation (overall execution times of each implementation for the predetermined number of iterations, as well as min/avg/max of single run). It is tested whether the solution provides a correct answer for the given variable, but may produce an error on different variable. I'm planning to add more testing.

Main files on each folder (e.g. [main.py](https://github.com/lcsm29/project-euler/blob/main/py/main.py)) will run every function implemented on every problems I've solved so far. By default, each problem takes about a second to finish the entire iterations on my computer, so it'll take about a couple of minutes to run if I ever write the solutions for every problems. Right now, it takes 10 seconds.

## Current Progress
| Languages                                                                      |     Progress      |
| ------------------------------------------------------------------------------ | ----------------- |
| [Python](https://github.com/lcsm29/project-euler/tree/main/py)                 |     19 / 747      |
| [C](https://github.com/lcsm29/project-euler/tree/main/c)                       |      0 / 747      |
| [C++](https://github.com/lcsm29/project-euler/tree/main/cpp)                   |      0 / 747      |
| [C#](https://github.com/lcsm29/project-euler/tree/main/cs)                     |      0 / 747      |
| [F#](https://github.com/lcsm29/project-euler/tree/main/fs)                     |      0 / 747      |
| [Go](https://github.com/lcsm29/project-euler/tree/main/go)                     |      0 / 747      |
| [Haskell](https://github.com/lcsm29/project-euler/tree/main/hs)                |      0 / 747      |
| [Java](https://github.com/lcsm29/project-euler/tree/main/java)                 |      0 / 747      |
| [JavaScript](https://github.com/lcsm29/project-euler/tree/main/js)             |      0 / 747      |
| [PHP](https://github.com/lcsm29/project-euler/tree/main/php)                   |      0 / 747      |
| [Ruby](https://github.com/lcsm29/project-euler/tree/main/rb)                   |      0 / 747      |
| [SQL](https://github.com/lcsm29/project-euler/tree/main/sql)                   |      0 / 747      |


## Scoreboard
This section hasn't been fully implemented yet. This is my attempt to compare the crunching speed of each language, but there are many limitations. The first and foremost limitation would be: each implementation of each language may use slightly different algorithms (or substantially different one in some cases), due to various reasons, including the differences in features, data types, or styles of each language, my own limited capability, et cetera. Also, each language may have a varying degree of optimization. As such, this is more like the comparison between apple and orange, rather than apple to apple comparison.

### Average execution time (in nanoseconds, unless specified) (lower is better)
This table shows how much nanoseconds it took for the fastest algo to complete one iteration on average. I haven't implemented the auto-update feature yet (except for Python), but once implemented, running main files on each folder (e.g. [main.py](https://github.com/lcsm29/project-euler/blob/main/py/main.py)) will trigger the automatic update of this table.
| Problems  | py         | pypy       | c          | cpp        | cs         | fs         | go         | hs         | java       | js         | php        | rb         | sql        |
| --------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 1         |[        688 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0001_multiples_of_3_and_5.py)|[         26 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0001_multiples_of_3_and_5.py)|            |            |            |            |            |            |            |            |            |        982 |            |
| 2         |[      2,175 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0002_even_fibonacci_numbers.py)|[        109 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0002_even_fibonacci_numbers.py)|            |            |            |            |            |            |            |            |            |            |            |
| 3         |[    315,218 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0003_largest_prime_factor.py)|[      5,696 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0003_largest_prime_factor.py)|            |            |            |            |            |            |            |            |            |            |            |
| 4         |[    520,481 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0004_largest_palindrome_product.py)|[     46,062 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0004_largest_palindrome_product.py)|            |            |            |            |            |            |            |            |            |            |            |
| 5         |[     50,703 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0005_smallest_multiple.py)|[     17,386 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0005_smallest_multiple.py)|            |            |            |            |            |            |            |            |            |            |            |
| 6         |[        227 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0006_sum_square_difference.py)|[         35 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0006_sum_square_difference.py)|            |            |            |            |            |            |            |            |            |            |            |
| 7         |[    9,459μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0007_10001st_prime.py)|[    1,316μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0007_10001st_prime.py)|            |            |            |            |            |            |            |            |            |            |            |
| 8         |[    1,429μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0008_largest_product_in_a_series.py)|[    145,872 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0008_largest_product_in_a_series.py)|            |            |            |            |            |            |            |            |            |            |            |
| 9         |[   19,604μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0009_special_pythagorean_triplet.py)|[     60,004 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0009_special_pythagorean_triplet.py)|            |            |            |            |            |            |            |            |            |            |            |
| 10        |[  166,420μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0010_summation_of_primes.py)|[   30,659μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0010_summation_of_primes.py)|            |            |            |            |            |            |            |            |            |            |            |
| 11        |[    787,162 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0011_largest_product_in_a_grid.py)|[    103,955 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0011_largest_product_in_a_grid.py)|            |            |            |            |            |            |            |            |            |            |            |
| 12        |[  157,001μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0012_highly_divisible_triangular_number.py)|[   30,326μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0012_highly_divisible_triangular_number.py)|            |            |            |            |            |            |            |            |            |            |            |
| 13        |[      1,917 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0013_large_sum.py)|[      2,523 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0013_large_sum.py)|            |            |            |            |            |            |            |            |            |            |            |
| 14        |[  782,930μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0014_longest_collatz_sequence.py)|[  403,116μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0014_longest_collatz_sequence.py)|            |            |            |            |            |            |            |            |            |            |            |
| 15        |[      1,722 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0015_lattice_paths.py)|[        394 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0015_lattice_paths.py)|            |            |            |            |            |            |            |            |            |            |            |
| 16        |[     23,123 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0016_power_digit_sum.py)|[     13,155 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0016_power_digit_sum.py)|            |            |            |            |            |            |            |            |            |            |            |
| 17        |[    1,486μs ](https://github.com/lcsm29/project-euler/blob/main/py/py_0017_number_letter_counts.py)|[    569,949 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0017_number_letter_counts.py)|            |            |            |            |            |            |            |            |            |            |            |
| 18        |[     39,424 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0018_maximum_path_sum_i.py)|[     21,963 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0018_maximum_path_sum_i.py)|            |            |            |            |            |            |            |            |            |            |            |
| 19        |[    144,441 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0019_counting_sundays.py)|[      6,714 ](https://github.com/lcsm29/project-euler/blob/main/py/py_0019_counting_sundays.py)|            |            |            |            |            |            |            |            |            |            |            |
* The table above is auto-generated from the following environments;
  * py: Python 3.9.5.final.0 (64 bit), macOS 11.4 (arm64), Apple M1
  * pypy: PyPy 7.3.5 with GCC Apple LLVM 12.0.5 (clang-1205.0.22.9), macOS 11.4 (x86_64), Apple M1
  * rb: Ruby 3.0.1p64, Windows 10 Professional (AMD64), Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz

### Number of Iterations (higher is better)
This table shows how much iterations it computes for about a second.
| Problems  | py         | pypy       | c          | cpp        | cs         | fs         | go         | hs         | java       | js         | php        | rb         | sql        |
| --------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 1         |     65,000 |    600,000 |            |            |            |            |            |            |            |            |            |      4,000 |            |
| 2         |    150,000 |  1,000,000 |            |            |            |            |            |            |            |            |            |            |            |
| 3         |      1,500 |     26,000 |            |            |            |            |            |            |            |            |            |            |            |
| 4         |        420 |      2,200 |            |            |            |            |            |            |            |            |            |            |            |
| 5         |     20,000 |     60,000 |            |            |            |            |            |            |            |            |            |            |            |
| 6         |     44,000 |  1,500,000 |            |            |            |            |            |            |            |            |            |            |            |
| 7         |        110 |        780 |            |            |            |            |            |            |            |            |            |            |            |
| 8         |        700 |      7,000 |            |            |            |            |            |            |            |            |            |            |            |
| 9         |         50 |     17,000 |            |            |            |            |            |            |            |            |            |            |            |
| 10        |          6 |         32 |            |            |            |            |            |            |            |            |            |            |            |
| 11        |      1,250 |      9,500 |            |            |            |            |            |            |            |            |            |            |            |
| 12        |          7 |         31 |            |            |            |            |            |            |            |            |            |            |            |
| 13        |     25,000 |     10,000 |            |            |            |            |            |            |            |            |            |            |            |
| 14        |          1 |          3 |            |            |            |            |            |            |            |            |            |            |            |
| 15        |    560,000 |  2,300,000 |            |            |            |            |            |            |            |            |            |            |            |
| 16        |     43,000 |     80,000 |            |            |            |            |            |            |            |            |            |            |            |
| 17        |        680 |      1,650 |            |            |            |            |            |            |            |            |            |            |            |
| 18        |     26,000 |     27,000 |            |            |            |            |            |            |            |            |            |            |            |
| 19        |      3,200 |     31,000 |            |            |            |            |            |            |            |            |            |            |            |
* Each main script not just runs the fastest algo, but runs every implementations. Thus, doing poorly on some algo could hamper the result greatly, even if the language is pretty fast on most implementations.
