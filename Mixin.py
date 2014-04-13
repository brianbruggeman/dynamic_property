#!/usr/bin/env python
"""
Mixins control meta properties on their objects
"""

from collections import OrderedDict as OD

class Mixin(object):
    """
    Adds meta properties
    """

    @property
    def meta(self):
        attr = "__meta__"
        if not hasattr(self, attr):
            setattr(self, attr, OD())
        return getattr(self, attr)
