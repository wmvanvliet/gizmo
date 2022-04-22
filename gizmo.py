def hello(name, country='Finland'):
	print('Hello {}, how are things in {}?'.format(name, country))

def spell(word):
	res = ''
	for letter in word:
		res += letter + '.'
	print(res[:-1])

def relative_path(subject_identifiers):
	return [f'./subjects/mock_recording_{subject_identifier}.rec' for subject_identifier in subject_identifiers]

class Gizmo():
	def __init__(self, name):
		self.name = name

	def speak(self):
		print(self.name)

def generate_fibonacci_sequence(n):
	'''
	Generates the first n Fibonacci numbers.

	Generates Fibonacci numbers up to n using the following recurrence:
	Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1.

	Parameters
	----------
	n : int
		The number of Fibonacci numbers to generate.
	
	Yields
	------
	fibonacci_number : int
		The next Fibonacci number.
	'''
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b