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
Modify your class such that it has a `friendship_name` property. The formula to
computing a friendship name is to reverse the name given upon creation of the
class (stored in the `.name` attribute), reverse it and capitalize only the
first letter (all other letters should be in lower case).

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo('Ariel')
>>> g.friendship_name
Leira
```

[Learn how to add a property](https://docs.python.org/3/library/functions.html#property)
