#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gizmo import Gizmo


def exercise(name="Ariel"):
    giz = Gizmo(name=name)
    print(f"giz  = '{giz}'")
    print(f"giz.name = '{giz.name}'")
    print("Speaking:")
    giz.speak()
    print(f"giz.friendship_name = '{giz.friendship_name}'")

if __name__ == "__main__":
    exercise()
