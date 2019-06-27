#!/usr/bin/env python3

import abuse_address


def main():
abuseEmail = abuse_address.findAbuseAddress('tslarge.com')
print(abuseEmail)

if __name__ == "__main__":
    main()
