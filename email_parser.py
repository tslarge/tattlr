#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
import sys
import pprint
import email
# from email.parser import Parser, BytesParser, HeaderParser
# from email.policy import default, compat32

# eml_file_path = 'samples/<spam email>.eml'
eml_file_path = sys.argv[1]

with open(eml_file_path, 'r') as fp:
    data = fp.read()
    msg = email.message_from_string(data)
    header_dict = dict()
    for i in msg._headers:
        header_dict[ i[0].strip(':') ] = i[1]
    pprint.pprint(header_dict)
    # print(msg.__dict__)

    if 'multipart' in header_dict['Content-Type']:  # Email prob has attachments
        msg_str = msg._payload[0]                   # meaning _payload is list
    else:
        msg_str = msg._payload

    if type(msg_str) != str:
        msg_str = msg_str.as_string()

    link_search = re.findall(r'http[s]?://[^\'" ]+', msg_str)
    a_search = re.findall(r'<a href="(.*)" .*>', msg_str)
    print('=== link_search ===\n')
    if link_search is not None:
        for i in link_search:
            print(i)
    print('\n=== a_search ===\n')
    for a in a_search:
        print(a)
