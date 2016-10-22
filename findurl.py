#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import urlmarker

rapor = open((sys.argv[1] + '_urls'), "w")
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        match = re.search(urlmarker.WEB_URL_REGEX, line)
        if match is not None:
            i = match.group()
            rapor.write(i + "\n")

f.close()
rapor.close()
