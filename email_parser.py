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
    #print(msg.__dict__)

    for i in msg._payload:
        msg_str = i.as_string()
        #link_search = msg_str.find('http')
        link_search = re.findall(r'http[s]?://[^\'" ]+', msg_str)
        if link_search is not None:
            #print(msg_str[link_search:link_search+200])
            for i in link_search:
                print(i)
