#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"
from typing import Callable


class Web(object):
    def getAllowedUrls(self):
        pass

    def addAllowedUrl(self, encodedUrl):
        """
        Accepts encrypted url and adds it to whitelist;
        Returns True if success, False otherwise
        :type encodedUrl: str 
        :rtype: bool 
        """
        pass

    def openUrl(self, url):
        pass

    def openUrlAsync(self, url, callback, data):
        """
        Open url and get result in callback (async)
        :type url: str 
        :type callback: Callable[str]
        :type data: dict
        :rtype: None 
        """
        pass

    def urlEncode(self, query, doseq=0):
        pass

    def urlQuote(self, s, safe='/'):
        pass
