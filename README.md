# Can you speak Python?

This is a Python challenge. Create pull requests (PR's) to this repository to solve
it. Upon PR submission, the GitHub action robots will check your code and
report back how well you did. You can then add more commits to your PR until
all tests come back green, which means you win!

## Exercise 1: Make a pull request

 1. Fork this repository
 2. Create a new branch (name it whatever you like)
 3. Add a new file `gizmo.py` to the repository
 4. Create a pull-request from your new branch to the master branch of this repository

When the `gizmo.py` exists, there should be `gizmo` python module that you can import.

For example:

```python
>> import gizmo
```

[Learn how to fork, branch and submit a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests)  
[Learn how to create a Python module](https://docs.python.org/3.8/tutorial/modules.html)

## Exercise 2: Create a Class
Add a class called `Gizmo` to your `gizmo.py` module.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo()
```
[Learn how to create a Python class](https://docs.python.org/3.8/tutorial/classes.html)

## Exercise 3: Add an attribute to your class.
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

[Learn how to add attributes](https://docs.python.org/3.8/tutorial/classes.html#class-object)

## Exercise 4: Add a method to your class.
Modify your class such that it has a `.speak()` method. Calling this method
will make the `Gizmo` object print its name using the `print()` function.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo('Ariel')
>>> g.speak()
Ariel
```

[Learn how to add methods to your class](https://docs.python.org/3/tutorial/classes.html#method-objects)

## Exercise 5: Add a property to your class.
Modify your class such that it has a `friendship_name` property. A property is
a method that you can access like you would an attribute. The formula to
computing a friendship name is to reverse the name given upon creation of the
class (stored in the `.name` attribute), reverse it and capitalize only the
first letter (all other letters should be in lower case). This computation
should happen "live", i.e. whenever the `friendship_name` property is being
accessed.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo('Ariel')
>>> g.friendship_name
Leira
>>> g.name = 'New name'  # Assign Gizmo a new name
>>> g.friendship_name    # Friendship name is being re-computed
Eman wen
```

[Learn how to add a property](https://docs.python.org/3/library/functions.html#property)

## Exercise 10: Add a NumPy array.
Modify the `gizmo` module such that it has a `multiplication_table` function.
This function should return a two-dimensional NumPy array (i.e. a matrix) that
contains the [multiplication table from 1 to 12](
https://multiplicationtablecharts.com/wp-content/uploads/2019/12/Multiplication-Table.jpg)
that you had to learn in elementary school.

For example:
```python
>>> import gizmo
>>> gizmo.multiplication_table()
array([[  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12],
       [  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24],
       [  3,   6,   9,  12,  15,  18,  21,  24,  27,  30,  33,  36],
       [  4,   8,  12,  16,  20,  24,  28,  32,  36,  40,  44,  48],
       [  5,  10,  15,  20,  25,  30,  35,  40,  45,  50,  55,  60],
       [  6,  12,  18,  24,  30,  36,  42,  48,  54,  60,  66,  72],
       [  7,  14,  21,  28,  35,  42,  49,  56,  63,  70,  77,  84],
       [  8,  16,  24,  32,  40,  48,  56,  64,  72,  80,  88,  96],
       [  9,  18,  27,  36,  45,  54,  63,  72,  81,  90,  99, 108],
       [ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110, 120],
       [ 11,  22,  33,  44,  55,  66,  77,  88,  99, 110, 121, 132],
       [ 12,  24,  36,  48,  60,  72,  84,  96, 108, 120, 132, 144]])
```

## Exercise 11: Numpy fancy indexing
Modify the `multiplication_table` function so that it takes a parameter called
`zero_out_multiples`. When this parameter is set of an integer number, then the
multiplication table that is returned by the function will have all multiples
of the given number set to zero. The default value of the `zero_out_multiples`
parameter should be ``None``, meaning that no numbers will be set to zero.

For example:
```python
>>> import gizmo
>>> gizmo.multiplication_table(zero_out_multiples=5)
array([[  1,   2,   3,   4,   0,   6,   7,   8,   9,   0,  11,  12],
       [  2,   4,   6,   8,   0,  12,  14,  16,  18,   0,  22,  24],
       [  3,   6,   9,  12,   0,  18,  21,  24,  27,   0,  33,  36],
       [  4,   8,  12,  16,   0,  24,  28,  32,  36,   0,  44,  48],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
       [  6,  12,  18,  24,   0,  36,  42,  48,  54,   0,  66,  72],
       [  7,  14,  21,  28,   0,  42,  49,  56,  63,   0,  77,  84],
       [  8,  16,  24,  32,   0,  48,  56,  64,  72,   0,  88,  96],
       [  9,  18,  27,  36,   0,  54,  63,  72,  81,   0,  99, 108],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
       [ 11,  22,  33,  44,   0,  66,  77,  88,  99,   0, 121, 132],
       [ 12,  24,  36,  48,   0,  72,  84,  96, 108,   0, 132, 144]])
```

[Learn about the modulo operator](https://docs.python.org/3.3/reference/expressions.html#binary-arithmetic-operations)
[Learn about NumPy array boolean indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html#boolean-array-indexing)
