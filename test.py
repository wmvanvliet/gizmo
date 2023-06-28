#!/usr/bin/env python3

from gizmo import Gizmo

g=Gizmo("testname")
g.speak()

g.hello("Joan", "Germany")
g.hello("Joan", "Netherlands")
g.hello("Joan")
g.spell("Joan")

subject_identifiers = ['subject1', 'subject2', 'subject3', 'subject4']
names = g.relative_path(subject_identifiers)
print(names)

fib = g.generate_fibonacci_sequence(10)
while(True):
    try:
        print(next(fib))
    except StopIteration:
        break
