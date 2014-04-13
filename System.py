#!/usr/bin/env python
from exceptions import UnimplementedException

class System(object):

    """
    All Systems inherit from this base class
    """

    def update(self, tick=None):
        """
        update should be called each frame
        """
        raise UnimplementedException()

