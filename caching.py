def caching(function):
	computed_results = {}
	def new_function(*args):
		if args not in computed_results:
			computed_results[args] = function(*args)
		return computed_results[args]