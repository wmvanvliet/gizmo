#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Gizmo():
    name: str

    def speak(self):
        print(self.name)

    @property
    def friendship_name(self):
        return self.name[-1].upper() + self.name[::-1].lower()[1:]
    