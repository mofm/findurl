#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('test') as f:
    rapor = open("rapor.txt", "w")
    for line in f.readlines():
        match = re.search("(?P<url>https?://[^\s]+)", line)
        if match is not None:
            i = match.group("url")
            rapor.write(i+"\n")

rapor.close()