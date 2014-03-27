# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:28:53 2014

script to rename files back

@author: tdiethe
"""

import os
import shutil

dropbox = '/home/curoseven/webapps/hl7_processor/tdl_dropbox'

for subdir, dirs, files in os.walk(dropbox):
    for fname in files:
        fullfile = os.path.join(dropbox, subdir, fname)
        if (fname.startswith('FAIL-')):
            notfailed = os.path.join(dropbox, subdir, fname[5:])
            shutil.move(fullfile, notfailed)