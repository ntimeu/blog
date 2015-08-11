#!/usr/bin/env python3
# -*- coding: utf8 -*-

import requests
import urllib.robotparser

resp = requests.get("http://www.example.com/robots.txt")
rp = urllib.robotparser.RobotFileParser()
rp.parse(resp.text.split('\n'))

rp.can_fetch(...)
