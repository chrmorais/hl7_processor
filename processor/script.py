# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:35:41 2014

Loads in the messages from the dropbox and puts them into mongodb
Moves successful files to archive, and renames failed files to *-fail.hl7

@author: tdiethe
"""

import os
import shutil
from hl7_parser import HL7Parser
from client import Client

dropbox = '/home/curoseven/webapps/hl7_processor/tdl_dropbox'
archive = '/home/curoseven/webapps/hl7_processor/archive'

client = Client()

i = 0
for subdir, dirs, files in os.walk(dropbox):
    for fname in files:
        fullfile = os.path.join(dropbox, subdir, fname)
        if (fname.startswith('FAIL-')):
            continue
        with open(fullfile) as f:
            try:
                hl7_parser = HL7Parser()
                hl7_parser.parse_file(os.path.join(f))
                client.insert_tdl_message(hl7_parser.message)
                # move file
                dest = os.path.join(archive, subdir, fname)
                if os.path.exists(dest):
                    shutil.copy(fullfile, archive)
                    os.remove(fullfile)
                else:
                    shutil.move(fullfile, archive)
                i += 1
            except Exception as e:
                print e.message
                # rename file
                failed = os.path.join(dropbox, subdir, 'FAIL-' + fname)
                shutil.move(fullfile, failed)

print "Processed", i, "messages"