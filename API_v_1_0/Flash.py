#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


# noinspection PyPep8Naming
class Flash(object):
    def call(self, methodName, args=None):
        """
        Send some data to as3.
        :type methodName: str
        :type args: list|None
        """
        pass

    def addExternalCallback(self, command, function):
        pass

    def removeExternalCallback(self, command=None, function=None):
        pass

    def loadFlashMod(self, modName):
        pass

    def loadPyMod(self, modName):
        """
        Load modification that was (probably) unloaded.
        :type modName: str
        """
        pass

    def reloadMod(self, modName, needToReloadPy=False):
        """
        Unload and load modification again.
        :type modName: str
        :param bool needToReloadPy: should we reload python code
        """
        pass

    def unloadMod(self, modName, needToUnloadPy=False):
        """
        Unload modification.
        :type modName: str
        :param bool needToUnloadPy: should we unload python code
        """
        pass

    def getModsStatus(self):
        """
        Get dict with mods info.
        E.g.:
        {
         'modName': isLoaded
        }
        :rtype: dict[str, bool]
        """
        pass
