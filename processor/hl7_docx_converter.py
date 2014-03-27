# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:00:30 2014

Create docx (MS Word) documents from HL7 messages

@author: tdiethe
"""

import docx
import os
from hl7_parser import HL7Parser

class HL7DocXConverter(object):
    def __init__(self):
        # Default set of relationshipships - the minimum components of a document
        self.relationships = docx.relationshiplist()
    
        # Make a new document tree - this is the main part of a Word document
        self.document = docx.newdocument()

        # This xpath location is where most interesting content lives
        self.body = self.document.xpath('/w:document/w:body', namespaces=docx.nsprefixes)[0]

        self.create_header()

    def create_header(self):
        """
        Create the header information
        """
        # Add logo
        self.relationships, picpara = docx.picture(self.relationships, 'curoseven_630x158.png', 'logo')
        self.body.append(picpara)

        self.body.append(docx.heading("Bespoke Blood Analysis", 1)) 
        self.body.append(docx.heading("Report & Recommendation", 1))

    def convert(self, message):
        """
        Convert HL7 messages into a formatted docx report
        """
        print message
        
    def save(self, filename):
        """
        Save the document
        """
        # Create our properties, contenttypes, and other support files
        title = 'CuroSeven custom report'
        subject = 'A practical example of making docx from Python'
        creator = 'CuroSeven'
        keywords = ['CuroSeven']

        coreprops = docx.coreproperties(title=title, subject=subject, creator=creator,
                               keywords=keywords)
        appprops = docx.appproperties()
        contenttypes = docx.contenttypes()
        websettings = docx.websettings()
        wordrelationships = docx.wordrelationships(self.relationships)

        docx.savedocx(self.document, coreprops, appprops, contenttypes, websettings,
             wordrelationships, filename)


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

"""
    body.append(paragraph('The module was created when I was looking for a '
        'Python support for MS Word .doc files on PyPI and Stackoverflow. '
        'Unfortunately, the only solutions I could find used:'))

    # Add a numbered list
    points = [ 'COM automation'
             , '.net or Java'
             , 'Automating OpenOffice or MS Office'
             ]
    for point in points:
        body.append(paragraph(point, style='ListNumber'))
    body.append(paragraph([('For those of us who prefer something simpler, I '
                          'made docx.', 'i')]))    
    body.append(heading('Making documents', 2))
    body.append(paragraph('The docx module has the following features:'))

    # Add some bullets
    points = ['Paragraphs', 'Bullets', 'Numbered lists',
              'Multiple levels of headings', 'Tables', 'Document Properties']
    for point in points:
        body.append(paragraph(point, style='ListBullet'))

    body.append(paragraph('Tables are just lists of lists, like this:'))
    # Append a table
    tbl_rows = [ ['A1', 'A2', 'A3']
               , ['B1', 'B2', 'B3']
               , ['C1', 'C2', 'C3']
               ]
    body.append(table(tbl_rows))

    body.append(heading('Editing documents', 2))
    body.append(paragraph('Thanks to the awesomeness of the lxml module, '
                          'we can:'))
    points = [ 'Search and replace'
             , 'Extract plain text of document'
             , 'Add and delete items anywhere within the document'
             ]
    for point in points:
        body.append(paragraph(point, style='ListBullet'))

    # Add an image
    relationships, picpara = picture(relationships, 'image1.png',
                                     'This is a test description')
    body.append(picpara)

    # Search and replace
    print 'Searching for something in a paragraph ...',
    if search(body, 'the awesomeness'):
        print 'found it!'
    else:
        print 'nope.'

    print 'Searching for something in a heading ...',
    if search(body, '200 lines'):
        print 'found it!'
    else:
        print 'nope.'

    print 'Replacing ...',
    body = replace(body, 'the awesomeness', 'the goshdarned awesomeness')
    print 'done.'

    # Add a pagebreak
    body.append(pagebreak(type='page', orient='portrait'))

    body.append(heading('Ideas? Questions? Want to contribute?', 2))
    body.append(paragraph('Email <python.docx@librelist.com>'))
"""