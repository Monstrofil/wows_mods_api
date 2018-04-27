#!/usr/bin/python
# coding=utf-8
import os
import datetime
import json

__author__ = "Aleksandr Shyshatsky"


class Utils(object):
    @staticmethod
    def getGameVersion():
        pass

    @staticmethod
    def getModDir():
        pass

    @staticmethod
    def stat(path):
        return os.stat(path)

    @staticmethod
    def walk(top, topdown, followlinks):
        return os.walk(top, topdown, followlinks)

    @staticmethod
    def isFile(path):
        return os.path.isfile(path)

    @staticmethod
    def isDir(path):
        return os.path.isdir(path)

    @staticmethod
    def isPathExists(path):
        return os.path.exists(path)

    @staticmethod
    def timeNowUTC():
        return datetime.datetime.utcnow()

    @staticmethod
    def timeNow():
        return datetime.datetime.now()

    @staticmethod
    def jsonEncode(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
                   allow_nan=True, cls=None, indent=None, separators=None,
                   encoding='utf-8', default=None, sort_keys=False, **kw):
        return json.dumps(obj, skipkeys, ensure_ascii, check_circular,
                          allow_nan, cls, indent, separators, encoding,
                          default, sort_keys, **kw)

    @staticmethod
    def jsonDecode(s, encoding='utf-8', parse_float=False, parse_int=False, parse_constant=False):
        return json.loads(s, encoding, parse_float, parse_int, parse_constant)
