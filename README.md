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
the letters. Use a `for`-loop to implement this.

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
'./subjects/mock_recording_<subject_identifier>.rec'
``` 
where `<subject_identifier>` is any string. Subject identifiers will be passed
to the method as a list of strings.

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


## Exercise 8: Add a property to your class
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

[Learn how to add a property](https://docs.python.org/3.6/library/functions.html#property)


## Exercise 9: Add a NumPy array
Modify the `gizmo` module such that it has a `multiplication_table` function.
This function should return a two-dimensional NumPy array (i.e. a matrix) that
contains the [multiplication table from 1 to 12](
https://multiplicationtablecharts.com/wp-content/uploads/2019/12/Multiplication-Table.jpg)
that you had to learn in elementary school. A quick way to generate this table is to take the outer product of two vectors with numbers from 1 to 12.

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

[Learn about NumPy arrays](https://numpy.org/doc/stable/user/quickstart.html#the-basics)  
[Learn about the outer product](https://numpy.org/doc/stable/reference/generated/numpy.outer.html)


## Exercise 10: Use Numpy's fancy indexing
Modify the `multiplication_table` function so that it takes a parameter called
`zero_out_multiples`. When this parameter is set to an integer number, then the
multiplication table that is returned by the function will have all multiples
of the given number set to zero. Use NumPy's boolean indexing to accomplish
this. The default value of the `zero_out_multiples` parameter should be
``None``, meaning that no numbers will be set to zero.

```python
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

[Learn about the modulo (%) operator](https://docs.python.org/3.6/reference/expressions.html#binary-arithmetic-operations)  
[Learn about NumPy array boolean indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html#boolean-array-indexing)

## Exercise 11: Build a generator
Add a function `generate_fibonacci_sequence(n)` to your `gizmo` module that will be a generator that `yield`s the first `n` numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number).

For example:
```python
>>> import gizmo
>>> fib = gizmo.generate_fibonacci_sequence(n)
>>> while(True):
>>>     print(next(fib))
0
1
1
2
3
5
8
13
21
34
```

[Learn about Python generators](https://www.programiz.com/python-programming/generator)


## Exercise 12: Build a NumPy array from a generator
Add a function `get_fibonacci_sequence(n)` to your `gizmo` module that takes a single parameter `n` and returns a NumPy array of the first `n` Fibonacci numbers. This function should use the generator you build in exercise 11 to generate the numbers, store them in a list and return the list in the form of a NumPy array.

For example:
```python
>>> import gizmo
>>> gizmo.get_fibonacci_sequence(10)
array([ 0,  1,  1,  2,  3,  5,  8, 13, 21, 34])
```

[How do I build a NumPy array from a generator?](https://stackoverflow.com/questions/367565/how-do-i-build-a-numpy-array-from-a-generator)

## Exercise 13: Read a CSV file with Pandas
The Gizmo git repository has a CSV in it called `titanic.csv`. This file contains information about all the passengers that were on board the Titanic when it sank. Add a function `get_titanic()` to your `gizmo` module that uses [Pandas](https://pandas.pydata.org/) to load the CSV file and return it as a `DataFrame`.

For example:
```python
>>> import gizmo
>>> gizmo.get_titanic().head(5)
     survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
0           0       3    male  22.0      1      0   7.2500        S   Third   
1           1       1  female  38.0      1      0  71.2833        C   First   
2           1       3  female  26.0      0      0   7.9250        S   Third   
3           1       1  female  35.0      1      0  53.1000        S   First   
4           0       3    male  35.0      0      0   8.0500        S   Third   
..        ...     ...     ...   ...    ...    ...      ...      ...     ...   
886         0       2    male  27.0      0      0  13.0000        S  Second   
887         1       1  female  19.0      0      0  30.0000        S   First   
888         0       3  female   NaN      1      2  23.4500        S   Third   
889         1       1    male  26.0      0      0  30.0000        C   First   
890         0       3    male  32.0      0      0   7.7500        Q   Third   

       who  adult_male deck  embark_town alive  alone  
0      man        True  NaN  Southampton    no  False  
1    woman       False    C    Cherbourg   yes  False  
2    woman       False  NaN  Southampton   yes   True  
3    woman       False    C  Southampton   yes  False  
4      man        True  NaN  Southampton    no   True  
..     ...         ...  ...          ...   ...    ...  
886    man        True  NaN  Southampton    no   True  
887  woman       False    B  Southampton   yes   True  
888  woman       False  NaN  Southampton    no  False  
889    man        True    C    Cherbourg   yes   True  
890    man        True  NaN   Queenstown    no   True  

[891 rows x 15 columns]
```

[Learn about the Pandas package](https://pandas.pydata.org/docs/getting_started/index.html#intro-to-pandas)  
[Learn about reading CSV data with Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#how-do-i-read-and-write-tabular-data)

## Exercise 14: Select rows from a Pandas DataFrame
Add a function `get_titanic_children()` to your `gizmo` module. This function should read the `titanic.csv` file in this git repository and return a Pandas `DataFrame` with all the children, age ≤ 12, that were on board the Titanic when it sunk.

For example:
```python
>>> import gizmo
>>> gizmo.get_titanic_children()
     survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
7           0       3    male  2.00      3      1  21.0750        S   Third   
10          1       3  female  4.00      1      1  16.7000        S   Third   
16          0       3    male  2.00      4      1  29.1250        Q   Third   
24          0       3  female  8.00      3      1  21.0750        S   Third   
43          1       2  female  3.00      1      2  41.5792        C  Second   
..        ...     ...     ...   ...    ...    ...      ...      ...     ...   
827         1       2    male  1.00      0      2  37.0042        C  Second   
831         1       2    male  0.83      1      1  18.7500        S  Second   
850         0       3    male  4.00      4      2  31.2750        S   Third   
852         0       3  female  9.00      1      1  15.2458        C   Third   
869         1       3    male  4.00      1      1  11.1333        S   Third   

       who  adult_male deck  embark_town alive  alone  
7    child       False  NaN  Southampton    no  False  
10   child       False    G  Southampton   yes  False  
16   child       False  NaN   Queenstown    no  False  
24   child       False  NaN  Southampton    no  False  
43   child       False  NaN    Cherbourg   yes  False  
..     ...         ...  ...          ...   ...    ...  
827  child       False  NaN    Cherbourg   yes  False  
831  child       False  NaN  Southampton   yes  False  
850  child       False  NaN  Southampton    no  False  
852  child       False  NaN    Cherbourg    no  False  
869  child       False  NaN  Southampton   yes  False  

[69 rows x 15 columns]
```

[Learn how to select rows from a Pandas `DataFrame`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#how-do-i-select-a-subset-of-a-dataframe)
