#!/usr/bin/env python
from mixins import notify


class Test(object):

    @notify
    def generate_data(self):
        return "hi"

t = Test()
x = t.generate_data()
x = t.generate_data()
x = t.generate_data()
print x