#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:32:24 2021

@author: jenska
"""

import gizmo

#%%
gizmo.hello('Roi','Latvia')
gizmo.hello('Roi')

#%%
gizmo.spell('word')

#%%
#ids = ['subj1','subj2']
ids = 'subjx'
paths = gizmo.relative_path(ids)
print(paths)

#%%
from gizmo import Gizmo

g = Gizmo('Mabelle')
g.speak()

#%%
t = gizmo.multiplication_table()
print(t)

#%%
print(gizmo.multiplication_table.__doc__)

#%%
fib = gizmo.generate_fibonacci_sequence(7)
for f in fib:
    print(f)

#%%
f = gizmo.get_fibonacci_sequence(5)
print(f)

#%%
tit = gizmo.get_titanic_children(5)
print(tit)
#%%