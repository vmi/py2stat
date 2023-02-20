#!/usr/bin/python2

import sys
import os
import py2stat

st = os.stat(sys.argv[1])
print py2stat.filemode(st)
print py2stat.user(st)
print py2stat.group(st)
