def caching(function):
	computed_results = {}
	def new_function(*args):
		if args not in computed_results:
			computed_results[args] = function(*args)
		return computed_results[args]
	return new_function


#специально неудачная реализация 
@caching
def fib(n):
	if n == 0 or n == 1:
		return 1
	return fib(n-1) + fib(n-2)


print(fib(100))#79 ms
print(fib(100))#при повторном вызове мнгновенно получаем рез
