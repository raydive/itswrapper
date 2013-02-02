#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
iTunes Store Search APIを使用して、該当するiTunes IDの
アルバム内容（曲を含む）を取得する
"""
class LookingupiTS(object):
    __URL = "https://itunes.apple.com/lookup?id="

    def __init__(self):
        pass

    def lookup(self, iTunesID, entity='song'):
        pass