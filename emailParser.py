#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
import sys
import pprint
import email
# from email.parser import Parser, BytesParser, HeaderParser
# from email.policy import default, compat32

# emlFilePath = 'samples/<spam email>.eml'
emlFilePath = sys.argv[1]

with open(emlFilePath, 'r') as fp:
    data = fp.read()
    msg = email.message_from_string(data)
    headerDict = dict()
    for i in msg._headers:
        headerDict[ i[0].strip(':') ] = i[1]
    pprint.pprint(headerDict)
    # print(msg.__dict__)

    if 'multipart' in headerDict['Content-Type']:  # Email prob has attachments
        msgStr = msg._payload[0]                   # meaning _payload is list
    else:
        msgStr = msg._payload

    if type(msgStr) != str:
        msgStr = msgStr.as_string()

    linkSearch = re.findall(r'http[s]?://[^\'" ]+', msgStr)
    aSearch = re.findall(r'<a href="(.*)" .*>', msgStr)
    print('=== linkSearch ===\n')
    if linkSearch is not None:
        for i in linkSearch:
            print(i)
    print('\n=== aSearch ===\n')
    for a in aSearch:
        print(a)
