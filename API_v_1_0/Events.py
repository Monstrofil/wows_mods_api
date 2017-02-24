#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"
from typing import Callable


def onSFMEvent(self, onSFMEvent):
    pass

# noinspection PyPep8Naming,PyMethodMayBeStatic
class Events(object):
    """
    Subscribe on events.
    E.g. events.onFlashReady(myHandler)
    """
    def onFlashReady(self, callback):
        """
        :param callback: func(modName)
        :type callback: Callable[str]
        """
        pass

    def onSFMEvent(self, callback):
        """
        :param callback: func(eventName, eventData)
        :type callback: Callable[str, list]
        """
        pass

    def onReceiveShellInfo(self, callback):
        """
        :param callback: func(victimID, shooterID,
                              ammoId, matId,
                              shotID, booleans,
                              damage, shotPosition,
                              yaw, hlinfo)

        :type callback: Callable[long, long, long, long, long, None, float,
                                 tuple, float, None]
        """
        pass

    def onBattleStart(self, callback):
        """
        Event called when 30 second's waiting ends
        :param callback: func()
        :type callback: Callable[]
        """
        pass

    def onBattleQuit(self, callback):
        """
        :param callback: func(arg)
        :type callback: Callable[bool]
        """
        pass

    def onKeyEvent(self, callback):
        """
        :param callback: func(event)
        :type callback: Callable[KeyEvent]
        """
        pass

    def onMouseEvent(self, callback):
        """
        :param callback: func(event)
        :type callback: Callable[MouseEvent]
        """
        pass
