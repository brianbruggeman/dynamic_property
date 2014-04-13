#!/usr/bin/env python

from Component import Component
from mixins import LockableMixin, EnableMixin, RenderableMixin


class LockableComponent(Component, LockableMixin):
    pass


class EnablableComponent(Component, EnableMixin):
    pass


class RenderableComponent(Component, RenderableMixin):
    pass
