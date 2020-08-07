#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gizmo


def exercise(name="Ariel"):
    print(">>> gizmo.hello('Gizmo', 'Germany')")
    gizmo.hello('Gizmo', 'Germany')
    print(">>> gizmo.hello('Gizmo')")
    gizmo.hello('Gizmo')

    print(">>> gizmo.spell('hello')")
    gizmo.spell('hello')


    print(">>> print(gizmo.relative_path(['subject1', 'subject2']))")
    print(gizmo.relative_path(['subject1', 'subject2']))

    print(">>> giz = gizmo.Gizmo(name='Ariel')")
    giz = gizmo.Gizmo('Ariel')

    print(">>> print(giz)")
    print(giz)

    print(">>> print(giz.name)")
    print(giz.name)

    print(">>> giz.speak()")
    giz.speak()

    print(">>> print(gizmo.multiplication_table())")
    print(gizmo.multiplication_table())

    print(">>> print(gizmo.multiplication_table(zero_out_multiples=5))")
    print(gizmo.multiplication_table(zero_out_multiples=5))

    print(">>> fib = gizmo.generate_fibonacci_sequence(10)")
    fib = gizmo.generate_fibonacci_sequence(10)

    print(">>> while(True): print(next(fib))")
    try:
        while(True): 
            print(next(fib))
    except StopIteration:
        pass

    print(">>> print(gizmo.get_fibonacci_sequence(10))")
    print(gizmo.get_fibonacci_sequence(10))

    print(">>> print(gizmo.get_titanic().head(5))")
    print(gizmo.get_titanic().head(5))

    print(">>> print(gizmo.get_titanic_children())")
    print(gizmo.get_titanic_children())


if __name__ == "__main__":
    exercise()
