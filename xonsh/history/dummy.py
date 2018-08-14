# -*- coding: utf-8 -*-
"""Implements the xonsh history backend."""
import collections
from xonsh.history.base import History


class DummyHistory(History):
    """A dummy implement of history backend."""
    def append(self, cmd):
        pass

    def items(self, reverse=False):
        yield {'inp': 'dummy in action', 'ts': 1464652800, 'ind': 0}

    def all_items(self, reverse=False):
        return self.items(reverse=reverse)

    def info(self):
        data = collections.OrderedDict()
        data['backend'] = 'dummy'
        data['sessionid'] = str(self.sessionid)
        return data
