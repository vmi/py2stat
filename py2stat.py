#!/usr/bin/python2

from __future__ import print_function
import six

import sys
import os
import pwd
import grp

TYPES = [
    '-', # 0o000000
    'p', # 0o010000
    'c', # 0o020000
    '-', # 0o030000
    'd', # 0o040000
    '-', # 0o050000
    'b', # 0o060000
    '-', # 0o070000
    '-', # 0o100000
    '-', # 0o110000
    'l', # 0o120000
    '-', # 0o130000
    's'  # 0o140000
]

MODES = [
    '---', # 0o0
    '--x', # 0o1
    '-w-', # 0o2
    '-wx', # 0o3
    'r--', # 0o4
    'r-x', # 0o5
    'rw-', # 0o6
    'rwx'  # 0o7
]

MODES_T = [
    '--T', # 0o0
    '--t', # 0o1
    '-wT', # 0o2
    '-wt', # 0o3
    'r-T', # 0o4
    'r-t', # 0o5
    'rwT', # 0o6
    'rwt'  # 0o7
]

MODES_S = [
    '--S', # 0o0
    '--s', # 0o1
    '-wS', # 0o2
    '-ws', # 0o3
    'r-S', # 0o4
    'r-s', # 0o5
    'rwS', # 0o6
    'rws'  # 0o7
]

def filemode(stat):
    m = stat.st_mode
    # sticky bit
    if m & 0o1000:
        om = MODES_T
    else:
        om = MODES
    # set group ID
    if m & 0o2000:
        gm = MODES_S
    else:
        gm = MODES
    # set user ID
    if m & 0o4000:
        um = MODES_S
    else:
        um = MODES
    mode = (
        TYPES[(m >> 12) & 15] +
        um[(m >> 6) &  7] +
        gm[(m >> 3) &  7] +
        om[ m       &  7]
    )
    return mode

def user(stat):
    try:
        entry = pwd.getpwuid(stat.st_uid)
        return entry.pw_name
    except KeyError:
        return str(uid)

def group(stat):
    try:
        entry = grp.getgrgid(stat.st_gid)
        return entry.gr_name
    except KeyError:
        return str(gid)

def test(args):
    for file in args:
        stat = os.lstat(file)
        print(" ".join([
            filemode(stat),
            oct(stat.st_mode),
            user(stat),
            group(stat),
            file]))

if __name__ == '__main__':
    test(sys.argv[1:])
