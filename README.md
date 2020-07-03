# Can you speak Python?

This is a Python challenge. Create pull requests to this repository to solve
it. Upon PR submission, the GitHub action robots will check your code and
report back how well you did. You can then add more commits to your pull
request until all tests come back green, which means you win!

## Exercise 1: Make a pull request

 1. Fork this repository
 2. Create a new branch (name it whatever you like)
 3. Add a new file `gizmo.py` to the repository
 4. Create a pull-request from your new branch to the master branch of this repository

When the `gizmo.py` exists, there should be `gizmo` python module that you can import:
```python
>> import gizmo
```

## Exercise 2: Create a Class
Add a class called `Gizmo` to your `gizmo.py` module.
For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo()
```

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

## Exercise 4: Add a property to your class.
Modify your class such that it has a `friendship_name` property. The formula to
computing the secret friendship name is to reverse the name given upon creation
of the class (stored in the `.name` attribute), reverse it and capitalize the
first letter.



