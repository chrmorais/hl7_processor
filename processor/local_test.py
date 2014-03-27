# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:31:16 2014

Local testing script

@author: tdiethe
"""

import os
from hl7_parser import HL7Parser
from hl7_docx_converter import HL7DocXConverter

#archive = '/home/curoseven/webapps/hl7_processor/archive'
archive = '/home/tdiethe/webfaction/archive'

fname = os.path.join(archive, '201401131942560014T024759CUROSEVEN.hl7')

with open(fname) as f:
    parser = HL7Parser()
    parser.parse_file(f)
    #print parser.message
    converter = HL7DocXConverter()
    converter.convert(parser.message)
    converter.save('test.docx')