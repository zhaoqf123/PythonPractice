tg = "This is the initial variable of this module"

def hold_client(name):
	yield 'Hello, %s! You will be connected soon' % name
	yield 'Dear %s, could you please wait a bit.' % name
	yield 'Sorry %s, we will play a nice music for you!' % name
	yield '%s, your call is extremely important to us!' % name


def fibonacci(n):
	curr = 1
	prev = 0
	counter = 0
	while counter < n:
		yield curr
		prev, curr = curr, prev + curr
		counter += 1


def fib():
	a, b = 0, 1
	while 1:
		yield b
		a, b = b, a + b