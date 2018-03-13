#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


class KeyEvent(object):
    def __init__(self):
        self.key = 1

    def isKeyDown(self):
        """
        :rtype: bool
        """
        pass

    def isKeyUp(self):
        """
        :rtype: bool
        """
        pass

    def isCtrlDown(self):
        """
        :rtype: bool
        """
        pass

    def isAltDown(self):
        """
        :rtype: bool
        """
        pass
