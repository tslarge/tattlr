#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pprint
import email
# from email.parser import Parser, BytesParser, HeaderParser
# from email.policy import default, compat32

eml_file_path = 'samples/<spam email>.eml'

with open(eml_file_path, 'r') as fp:
    data = fp.read()
    msg = email.message_from_string(data)
    header_dict = dict()
    for i in msg._headers:
        header_dict[ i[0].strip(':') ] = i[1]
    pprint.pprint(header_dict)
