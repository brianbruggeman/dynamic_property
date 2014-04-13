#!/usr/bin/env python
import uuid

from Component import Component


class Entity(object):

    def __init__(self, **components):
        self.id = uuid.uuid4()
        self.components = []
        for name, obj in components.iteritems():
            if not isinstance(obj, Component):
                obj = Component(obj)
            obj.register_entity(self.id)
            setattr(self, name, obj)
            self.components.append(name)
        super(Entity, self).__init__()

    def __del__(self):
        for name in self.components:
            obj = getattr(self, name)
            func_name = 'deregister_entity'
            if hasattr(obj, func_name):
                func = getattr(obj, func_name)
                func(self.id)
