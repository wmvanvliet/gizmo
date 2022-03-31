# Can you speak Python?

This is a Python challenge. Create pull requests (PR's) to this repository to
solve it. Upon PR submission, the GitHub action robots will check your code and
report back how well you did. You can then add more commits to your PR until
all tests come back green, which means you win!

The exercises are meant to test your knowledge of some important features of
the Python programming language. When it's not immediately obvious to you how
to solve an exercise using only a few lines of code, it is likely you can learn
a new Python trick by checking the links below the exercise.


## Exercise 1: Make a pull request

 1. Fork this repository
 2. Create a new branch (name it whatever you like)
 3. Add a new file `gizmo.py` to the repository
 4. Create a pull-request from your new branch to the master branch of this repository

When `gizmo.py` exists, there should be `gizmo` python module that you can import.

For example:

```python
>>> import gizmo
```

[Learn how to fork, branch and submit a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests)  
[Learn how to create a Python module](https://docs.python.org/3.6/tutorial/modules.html)


## Exercise 2: Create a function
Add a `hello()` function to the `gizmo` module. The function should take two parameters: `name` and `country`. The `country` parameter is optional and should default to `'Finland'`. When called, the function uses the `print()` function to write the text `Hello {name}, how are things in {country}?` to the screen, where `{name}` and `{country}` should be the name and country given as parameters.

For example:
```python
>>> import gizmo
>>> gizmo.hello('Gizmo', 'Germany')
Hello Gizmo, how are things in Germany?
>>> gizmo.hello('Gizmo')
Hello Gizmo, how are things in Finland?
```

[Learn how to define functions in Python](https://docs.python.org/3.6/tutorial/controlflow.html#defining-functions)


## Exercise 3: Use a loop
Add a `spell()` function to the `gizmo` module that uses the `print()` function
to spell out the word given as a parameter to the function, with dots between
the letters. Use a `for`-loop to implement this (no `split`/`join`).

For example:
```python
>>> import gizmo
>>> gizmo.spell('hello')
h.e.l.l.o
```

[Learn how to write a for loop in Python](https://docs.python.org/3.6/tutorial/controlflow.html#for-statements)


## Exercise 4: Use string formatting
Reading a bunch of files with only small differences in their filenames is a
very common occurrence in any research code. Add a function `relative_path()`
to the `gizmo` module that returns a list of files, including their relative
path, following the following pattern:
```text
'./subjects/mock_recording_{subject_identifier}.rec'
``` 
where `{subject_identifier}` is any string. Subject identifiers will be passed
to the function as a list of strings.

For example:
```python
>>> import gizmo
>>> subject_identifiers = ['subject1', 'subject2']
>>> names = gizmo.relative_path(subject_identifiers)
>>> print(names)
['./subjects/mock_recording_subject1.rec', './subjects/mock_recording_subject2.rec']
```

[Get started with string formatting](https://realpython.com/python-f-strings/)  
[If you want to go into more detail you can also check the python documentation here.](https://docs.python.org/3.6/library/string.html)


## Exercise 5: Create a Class
Add a class called `Gizmo` to your `gizmo.py` module.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo()
```
[Learn how to create a Python class](https://docs.python.org/3.6/tutorial/classes.html)


## Exercise 6: Add an attribute to your class
Modify your class such that when you create a new instance of `Gizmo`, you can give it a name.
The name is a string.
Afterwards, the name should be available as the `.name` attribute.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo('Ariel')
>>> g.name
'Ariel'
```

[Learn how to add attributes](https://docs.python.org/3.6/tutorial/classes.html#class-objects)


## Exercise 7: Add a method to your class
Modify your class such that it has a `.speak()` method. Calling this method
will make the `Gizmo` object print its name using the `print()` function.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo('Ariel')
>>> g.speak()
Ariel
```

[Learn how to add methods to your class](https://docs.python.org/3.6/tutorial/classes.html#method-objects)


## Exercise 8: Build a generator
Add a function `generate_fibonacci_sequence(n)` to your `gizmo` module that will be a generator that `yield`s the first `n` numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number).

For example:
```python
>>> import gizmo
>>> fib = gizmo.generate_fibonacci_sequence(5)
>>> while(True):
>>>     print(next(fib))
0
1
1
2
3
StopIteration
```

[Learn about Python generators](https://www.programiz.com/python-programming/generator)


## Exercise 9: Document your function using numpydoc
Add a docstring to the `generate_fibonacci_sequence` function. Use the "numpydoc" style
for this documentation. The documentation should contain:

 1. Short summary: a one-line description of what the function does.
 2. Extended summary: A longer description with more details about what the function does.
 3. Parameters: a list of all parameters that the function takes. For each parameter, describe:
     1. The parameter name
     2. Its expected type (int, bool, str, array, ...)
     3. What the parameter does
 4. Yields: a list of all values yielded by the generator. For each return value,  describe:
     1. The yielded value's name
     2. Its type (int, bool, str, array, ...)
     3. What the yielded value means

[Learn about docstrings](https://docs.python.org/3.6/tutorial/controlflow.html#documentation-strings)  
[Learn about the numpydoc documentation style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
