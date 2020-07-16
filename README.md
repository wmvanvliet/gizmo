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


## Exercise 6: Use a loop
Add a `.spell()` method to your `Gizmo` class that uses the `print()` function to spell out its name, with dots between the 
letters. Use a `for`-loop to implement this.

For example:
```python
>>> from gizmo import Gizmo
>>> g = Gizmo('Ariel')
>>> g.spell()
A.r.i.e.l
```

[Learn how to write a for loop in Python](https://docs.python.org/3.8/tutorial/controlflow.html#for-statements)

## Exercise 7 Using string formatting
Reading a bunch of files with only small differences in their filenames is a very common 
occurrence in any research code. Please extend the gizmo module with a method relative_path() 
that will return a list of files, including their relative path following the following pattern:
```text
" ./subjects/mock_recording_<subject_identifier>.rec"
``` 
where <subject_identifier> is any string. Subject identifiers will be passed to the method as a 
list of strings.

For example:
```python
>>> import gizmo
>>> subject_identifiers = ["subject1","subject2"]
>>> names = gizmo.relative_path(subject_identifiers)
>>> print(names)
['./subjects/mock_recording_subject1.rec', './subjects/mock_recording_subject2.rec']
```
[Getting started with string formatting](https://realpython.com/python-f-strings/)

[If you want to go into more detail you can also check the python documentation here.](https://docs.python.org/3.4/library/string.html)

