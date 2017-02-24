#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Callbacks(object):
    def perTick(self, func):
        """
        Setup new callback to call specified
        function each game tick.
        :param func: object with __call__ defined
        :return int: handler
        """
        pass

    def callback(self, dt, func, *args, **kw):
        """
        Call another function with some delay.
        :param int dt: delay, ms
        :param object func: object with __call__ defined
        :param list args: args to pass into func
        :param dict kw: kwargs to pass into func
        :return int: handler
        """
        pass

    def cancel(self, handle):
        """
        Cancel callbacks that were set up
        in perTick or callback method
        :type handle: int
        :rtype: None
        """
        pass

