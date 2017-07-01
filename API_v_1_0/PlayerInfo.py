#!/usr/bin/python
# coding=utf-8
from ShipInfo import ShipInfo

__author__ = "Aleksandr Shyshatsky"


class PlayerInfo(object):
    """
    Restored from dir(), real signatures unknown.
    """
    def __init__(self): 
        self.isLeaver = False
        self.isConnected = False
        self.teamId = 0
        self.shipId = 767545
        self.avatarId = 767544
        self.id = 339168
        self.preBattleIdOnStart = 0
        self.maxHealth = 0.0
        self.preBattleSign = 0
        self.ttkStatus = False
        self.shipConfig = object() # Fixme
        self.shipParamsId = 0L
        self.isAlive = True
        self.prebattleIndex = 0
        self.prebattleId = 0
        self.hTTKStatus = False
        self.shipInfo = ShipInfo()
        self.teammateDamages = dict()
        self.isPreBattleOwner = False
        self.clanTag = u''
        self.shipComponents = dict()
        self.name = str()
        self.shipGameData = object()
        self.invitationsEnabled = True
        self.fragsCount = 0
        self.vehicleParams = object()
        self.isClientLoaded = True
        self.rankInfoDump = 0
        self.tkillStatus = False
        self.isOwn = False
        self.isBot = False
