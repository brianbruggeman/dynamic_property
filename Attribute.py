#!/usr/bin/env python

from collections import OrderedDict as OD


class Attribute(object):

    @property
    def value(self):
        attr = "__value__"
        if not hasattr(self, attr):
            setattr(self, attr, False)
        return getattr(self, attr)

    @value.setter
    def value(self, value):
        self.__value__ = value

    def __init__(self, value):
        self.value = value
        super(Attribute, self).__init__()

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        cname = self.__class__.__name__
        value = str(self.value)
        return "<%s %s>" % (cname, value)
