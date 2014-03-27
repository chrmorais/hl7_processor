# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:49:12 2014

@author: tdiethe
"""

from jinja2 import Environment, FileSystemLoader
import os
from hl7_parser import HL7Parser
from datetime import datetime
from normal_ranges import get_additional_info
from detailed_info import get_detailed_info

#archive = '/home/curoseven/webapps/hl7_processor/archive'
archive = '/home/tdiethe/webfaction/archive'

fname = os.path.join(archive, '201401131942560014T024759CUROSEVEN.hl7')

class ReportGenerator(object):
    """
    A class to generate an html report from an HL7 message
    """
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.template = self.env.get_template('report_2014_02_17.html')

    def ord(self, n):
        """
        Adds st/th/rd/nd to date
        """        
        return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))
    
    def stylish_datetime(self, dt,f):
        return dt.strftime(f).replace("{th}", self.ord(dt.day))

    def generate(self, message):
        """
        Generate the report
        """
        message['today'] = generator.stylish_datetime(datetime.now(), '{th} %B %Y')
        for obs in message['observations']:
            get_additional_info(obs)
            get_detailed_info(obs)
        self.report = self.template.render(message)

# In reality we want to check if the file with the given id already exists here

parser = HL7Parser()
with open(fname) as f:
    parser.parse_file(f)
message = parser.message

generator = ReportGenerator()
generator.generate(message)

with open(message['id'] + '.html', 'w') as f:
    f.write(generator.report)