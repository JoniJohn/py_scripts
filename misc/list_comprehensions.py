# Python's list compresion are awesome
# vals = [expression
#	for value in collection
#	if condition]

# this is equivalent to:
vals = []
for value in collection:
	if condition:
		vals.append(expression)

# Example:
even_squares = [x * x for x in range(10) if not x % 2]
even_squares

###### LINKS ######
# https://realpython.com/list-comprehension-python/
