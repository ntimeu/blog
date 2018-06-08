#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.ntimeu.fr'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS  = 'feeds/all.rss.xml'

DELETE_OUTPUT_DIRECTORY = True
