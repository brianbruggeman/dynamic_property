#!/usr/bin/env python

from Attribute import Attribute
from mixins import LockableMixin


class LockableAttribute(Attribute, LockableMixin):
    pass


if __name__ == "__main__":
    attr = LockableAttribute(1)
    assert attr.locked is False
    assert attr.value == 1
    attr.lock()
    assert attr.locked is True
    attr.unlock()
    assert attr.locked is False
    attr.value = 2
    assert attr.value == 2
    attr.locked = True
    attr.value = 3
    assert attr.value == 2    # This will fail
