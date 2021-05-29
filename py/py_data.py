file_names = {
    1: 'py_1_multiples_of_3_and_5',
	2: 'py_2_even_fibonacci_numbers',
	3: 'py_3_largest_prime_factor',
}

ans = {
	  1: 233168,
	  2: 4613732,
	  3: 6857,
}

var = {
	1: 1000,
	2: 4000000,
	3: 600851475143,
}

iters = {
	1: 5000,
	2: 500000,
	3: 1500,
}

def get_iters(index, seconds):
	return int(iters[index] * seconds)
