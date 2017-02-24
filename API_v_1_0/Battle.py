#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Battle(object):
    def getPlayersInfo(self):
        """
        Get dict with players in battle.
        :rtype: dict[long, PlayerInfo.PlayerInfo]
        """
        pass

    def getPlayerInfo(self, playerId):
        """
        Get info about player via playerId.
        :type playerId: long
        :rtype: PlayerInfo.PlayerInfo
        """
        pass

    def getSelfPlayerInfo(self):
        """
        Get current player info.
        :rtype: PlayerInfo.PlayerInfo
        """
        pass

    def getPlayerInfoByName(self, name):
        """
        Get player info by name.
        Return None if nothing found.
        :type name: str
        :rtype: PlayerInfo.PlayerInfo|None
        """
        pass

    def getPlayerShipInfo(self, playerId):
        """
        Get info about player's ship via playerId.
        :type playerId: long
        :rtype: ShipInfo
        """
        pass

    def getDistanceInMeters(self, start, end):
        """
        Get distance between points, in meters.
        :type start: tuple(x, y, z)
        :type end: tuple(x, y, z)
        :return float: dist in meters
        """
        pass

    def getPlayerByVehicleId(self, shipId):
        """
        Get player by his vehicle id.
        :type shipId: long
        :rtype: PlayerInfo.PlayerInfo|None
        """
        pass

    def getAmmoParams(self, ammoId):
        """
        Get ammo params
        :type ammoId: long
        :rtype: object
        """
        pass

    def onObserverdShipChanged(self, callback):
        """
        Called when observed ship changes.
        :type callback: typing.Callable
        """
        pass