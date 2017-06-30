#!/usr/bin/python
# coding=utf-8
from Utils import Utils

__author__ = "Aleksandr Shyshatsky"

from Battle import Battle
from Flash import Flash
from Callbacks import Callbacks
from Events import Events
from Web import Web

callbacks = Callbacks()
flash = Flash()
battle = Battle()
events = Events()
web = Web()
utils = Utils

__all__ = ['flash', 'battle', 'callbacks', 'events', 'web', 'utils']
