import exrex

def force(start_depth, pattern, check_callback, cache_callback):
	attempts = start_depth

	gen = exrex.generate(pattern)
	for i in range(start_depth):
		next(gen)

	for guess in gen:
		attempts += 1
		if check_callback(guess) == 1:
				return (guess, attempts)
		print("- {} - permutations: {}".format(guess, attempts))
		if attempts % 1000 == 0:
			cache_callback(attempts)
	return False