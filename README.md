hl7_processor
=============

System for processing HL7 messages. Parses the messages, and drops them into mongodb for storage. 
A separate process reads the messages from mongodb and creates HTML reports (static pages).
