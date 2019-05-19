#!/usr/bin/env python3

import subprocess

whois = subprocess.run(['whois','tslarge.com'], capture_output=True)

whoisResult = whois.stdout.decode('utf-8').split('\n')

for item in whoisResult:
    itemSplit = item.split(':')
    if itemSplit[0] == "Registrar Abuse Contact Email":
        print(itemSplit[1])
