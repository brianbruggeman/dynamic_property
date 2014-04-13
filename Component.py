#!/usr/bin/env python
import uuid

from Attribute import Attributes


class Component(object):

    """
    Components are collections of attributes
    """
    @property
    def attributes(self):
        attrs = {}
        for field in self.__fields__:
            attrs[field] = self.get(field)
        return attrs

    @property
    def id(self):
        attr = '__id__'
        if not hasattr(self, attr):
            setattr(self, attr, uuid.uuid4().hex)
        return getattr(self, attr)

    def __init__(self, **attributes):
        super(Component, self).__init__()
        self.__fields__ = []
        for name, val in attributes.iteritems():
            if name not in self.__fields__:
                self.__fields__.append(name)
                setattr(self, name, val)

    def __setattr__(self, name, value):
        if not name.startswith("__"):
            if not isinstance(value, Attribute):
                value = Attribute(value)
        super(Component, self).__setattr__(name, value)

    def __getitem__(self, name):
        """
        Doesn't raise an exception if the value doesn't exist
        """
        return getattr(self, name, None)

    def get(self, name, default=None):
        """
        Acts like a dictionary's get command
        """
        return getattr(self, name, default)

    def __str__(self):
        return str(self.dict)

    def __repr__(self):
        cname = self.__class__.__name__
        return "<%s %s>" % (cname, self.id)
