#!/usr/bin/env python
from Mixin import Mixin


def lockable(func, locked=None):
    def wrapper(*args, **kwds):
        if locked:
            val = None
        else:
            val = func(*args, **kwds)
        return val
    return wrapper


class LockableMixin(Mixin):

    @property
    def locked(self):
        self.meta.setdefault("locked", False)
        return self.meta.get("locked")

    @locked.setter
    def locked(self, value):
        locked = self.meta['locked']
        if value in [None, True, False]:
            locked = value
        self.meta['locked'] = locked

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def is_locked(self):
        return self.locked

    def __init__(self):
        super(LockableMixin, self).__init__()
        self.__setattr__ = lockable(self.__setattr__, self.locked)


class EnabledMixin(Mixin):

    """
    Adds enabled value to a Property or Component
    """

    @property
    def enabled(self):
        self.meta.setdefault("enabled", None)
        return self.meta.get('enabled')

    @enabled.setter
    def enabled(self, value):
        value_was_set = False
        if value in [None, True, False]:
            self.meta['enabled'] = value
            value_was_set = True
        return value_was_set

    def is_enabled(self):
        return self.enabled


class RenderableMixin(Mixin):

    """
    Adds rendered value to a Property or Component
    """

    @property
    def renderable(self):
        self.meta.setdefault("renderable", None)
        return self.meta.get('renderable')

    @renderable.setter
    def renderable(self, value):
        value_was_set = False
        if value in [None, True, False]:
            self.meta['renderable'] = value
            value_was_set = True
        return value_was_set

    def is_renderable(self):
        return self.renderable
