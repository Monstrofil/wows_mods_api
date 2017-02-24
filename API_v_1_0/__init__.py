#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

from Battle import Battle
from Flash import Flash
from Callbacks import Callbacks
from Events import Events

callbacks = Callbacks()
flash = Flash()
battle = Battle()
events = Events()

__all__ = ['flash', 'battle', 'callbacks', 'events']
