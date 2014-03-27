# -*- coding: utf-8 -*-
"""
Spyder Editor

Simple HL7 message processor
"""

# import hl7
from dateutil import parser
# import TestResults


class HL7ParseException(object):
    """HL7 parser exceptions"""
    def __init__(self, message):
        print message

class HL7Parser(object):
    """
    HL7 parser
    """
    def __init__(self):
        self.message = {'orders': [], 'observations': []}

    def parse_header(self, fields):
        """
        Message Header
        http://jwenet.net/notebook/1777/1250.html
        """
        if fields[1] != '^~\\&':
            raise HL7ParseException("Unkown message format " + fields[1])
        self.message['sending_app'] = fields[2]
        self.message['sender'] = fields[3]
        self.message['datetime'] = parser.parse(fields[6])
        self.message['processing_id'] = fields[11]
        self.message['continuation_ptr'] = fields[14]
    
    def parse_patient_id(self, fields):
        """
        Patient identification
        http://jwenet.net/notebook/1777/1295.html
        """
        self.message['patient'] = {}
        self.message['patient']['id'] = fields[3]
        self.message['patient']['names'] = filter(None, fields[5].split('^'))[::-1]
        self.message['patient']['first_name'] = self.message['patient']['names'][0].title()
        self.message['patient']['last_name'] = self.message['patient']['names'][-1].title()
        self.message['patient']['date_of_birth'] = parser.parse(fields[7])
        self.message['patient']['gender'] = fields[8]
        # Note that there may well be more than this ...
    
    def parse_patient_information(self, fields):
        """
        Patient information
        http://jwenet.net/notebook/1777/1305.html
        """
        self.message['visit'] = {}
        self.message['visit']['location'] = fields[3].split('^')[0]
        self.message['visit']['consuting_doctor'] = fields[9]
        
        
    def parse_order_common_information(self, fields):    
        """
        Order common information
        http://jwenet.net/notebook/1777/1275.html
        """
        self.message['order_common'] = {}
        self.message['order_common']['control'] = fields[1]
        self.message['order_common']['filler_number'] = fields[3]
        self.message['order_common']['status'] = fields[5]
        self.message['order_common']['transaction_date'] = parser.parse(fields[9])
    
    def parse_order_information(self, fields):
        """
        Order information
        http://jwenet.net/notebook/1777/1265.html
        """
        order = {}
        order['set_id'] = fields[1]
        order['filler_number'] = fields[3]
        usif = fields[4].split('^')
        usi = {}    
        usi['code'] = usif[0]
        usi['title'] = usif[1]
        order['universal_service_identifier'] = usi
        order['request_datetime'] = parser.parse(fields[6])
        order['observed_datetime'] = parser.parse(fields[7])
        order['diagnostic_service_sector_id'] = fields[24]
        order['result_status'] = fields[25]
        self.message['orders'].append(order)
    
    def parse_observation_information(self, fields):
        """
        Obvservation information
        http://jwenet.net/notebook/1777/1270.html    
        """
        observation = {}
        observation['set_id'] = fields[1]
        observation['value_type'] = fields[2]
        obsid = fields[3].split('^')
        observation['identifier'] = {}
        observation['identifier']['code'] = obsid[0]
        observation['identifier']['title'] = obsid[1]
        observation['identifier']['type'] = obsid[3]
        observation['identifier']['id1'] = obsid[4]
        observation['identifier']['id2'] = obsid[5]
        try:
            observation['value'] = float(fields[5].split('%')[-1].strip())
        except:
            observation['value'] = float('nan')
        observation['units'] = fields[6]
        observation['abnormal_flags'] = fields[8]
        observation['result_status'] = fields[11]
        self.message['observations'].append(observation)
        
    def parse_notes_and_comments(self, fields):
        self.message['notes'] = { 'source': fields[1], 'comment': fields[2] }
        
        """
        for (i, field) in enumerate(fields):
            if (field):
                print i, field
        """

    def parse_file(self, file_handle):
        segments = file_handle.readlines()
        for segment in segments:
            fields = segment.strip().split('|')
            if (fields[0] == 'MSH'):
                self.parse_header(fields)
                continue
            if (fields[0] == 'PID'):
                self.parse_patient_id(fields)
                continue
            if (fields[0] == 'PV1'):
                self.parse_patient_information(fields)
                continue
            if (fields[0] == 'ORC'):
                self.parse_order_common_information(fields)
                continue
            if (fields[0] == 'OBR'):
                self.parse_order_information(fields)
                continue
            if (fields[0] == 'OBX'):
                self.parse_observation_information(fields)
                continue
            if (fields[0] == 'NTE'):
                self.parse_notes_and_comments(fields)
                continue
        # Create an id based on name and date
        self.message['id'] = self.message['datetime'].isoformat() \
            + self.message['patient']['first_name'] \
            + self.message['patient']['last_name']
            
            
            
#f = open('201401131942560014T024759CUROSEVEN.hl7')
#f = open('201401131739390014T024760CUROSEVEN.hl7')
#with open('201401221041240014T056771CUROSEVEN.hl7') as f:
#    hl7_parser = HL7Parser()
#    hl7_parser.parse_file(f)
#    print hl7_parser.message

# print tr.keys()