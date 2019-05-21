#!/usr/bin/env python3
import smtplib

from email.message import EmailMessage

class AbuseReport(EmailMessage):
    """
    Template for final email message to be sent to report spam abuse.
    """
    def __init__(self):
        pass
