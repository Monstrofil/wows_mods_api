#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

DEFAULT_NAME = 'Individual|Персональный'


# noinspection PyPep8Naming,PyMethodMayBeStatic
class CustomPorts(object):
    def addCustomPort(self, portName, portDisplayName=DEFAULT_NAME, isPremium=False, peculiarities=None):
        """
        Add custom port in hangar menu.
        :param str portName: unique port name, the same as space folder name
        :param str portDisplayName: displayed name
        :param bool isPremium: True -> port will be available only with premium account
        :param list|None peculiarities: e.g. peculiarities = [ 'arpeggio' ]
        """
        pass

    def removeCustomPort(self, portName):
        """
        Remove port from hangar menu
        :param str portName: unique port name, the same as space folder name
        """
        pass