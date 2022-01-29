# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:19:30 2022
@author: Brendan C
"""
import feedparser


def getData(link):
    # using feed parser we take the string that must lead to the rss feed
    # to get the link of the aritcles.
    newsFeed = feedparser.parse(link)
    return newsFeed


def getLatest(rssFeed):
    # takes the data feedparser data type to then get the most recent arcticle.
    return rssFeed.entries[0]
