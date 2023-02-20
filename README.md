py2stat
=======

`py2stat` provides an alternative to `stat.filemode()` and more in Python2.

This is intended for use on older Linux distributions.

Usage:
```
import sys
import os
import py2stat

st = os.stat(sys.argv[1])
print py2stat.filemode(st)
print py2stat.user(st)
print py2stat.group(st)
```
