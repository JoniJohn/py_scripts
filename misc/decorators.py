import datetime

def log(func):
	def wrapper(*args, **kwargs):
		# you can do something before calling the function
		val = func(*args, **kwargs)
		# you can do something after calling the function
		return val
	return wrapper

@log
def run(a, b, c=9):
	print(a+b+c)

run(1, 3, c=9)
