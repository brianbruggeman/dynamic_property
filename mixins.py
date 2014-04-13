#!/usr/bin/env python
from Mixin import Mixin
import MessageBus


def lockable(func):
    def _lockable(self, *args, **kwds):
        attr = 'locked'
        if not hasattr(self, attr):
            setattr(self, attr, None)
        locked = getattr(self, attr, None)
        val = None if locked else func(self, *args, **kwds)
        return val
    return _lockable


class LockableMixin(Mixin):

    @property
    def locked(self):
        value = None
        if hasattr(self, 'meta'):
            self.meta.setdefault("locked", False)
            value = self.meta.get("locked")
        return value

    @locked.setter
    def locked(self, value):
        locked = None
        if hasattr(self, 'locked'):
            if value in [None, True, False]:
                locked = value
            self.meta['locked'] = locked

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def is_locked(self):
        return self.locked

    def __setattr__(self, name, value):
        func = super(LockableMixin, self).__setattr__
        locked = getattr(self, 'locked', None)
        if not locked or name == 'locked':
            func(name, value)            

    def __init__(self):
        super(LockableMixin, self).__init__()


def notify(func, topic=None, binding=None, sock=None):
    def _notify(self, *fargs, **fkwds):
        mdata = data = func(self, *fargs, **fkwds)
        attr = 'notify_socket'
        if hasattr(self, attr):
            sock = getattr(self, attr)
        sock = MessageBus.publish(mdata, sock=sock)
        setattr(self, attr, sock)
        return data
    return _notify


