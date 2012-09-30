#!/usr/bin/env python

import imaplib
import getpass
import email

server = "imap.gmail.com"
port = "993"
username = "ewdurbin@gmail.com"
password = None

mail = imaplib.IMAP4_SSL(server, port)
if not password:
  prompt = "IMAP Password for %s?:\n" % (username)
  password = getpass.getpass(prompt)
mail.login(username, password)
mail.select("INBOX", readonly=True)

result, data = mail.uid('search', None, "ALL")
mail_list = data[0].split()
latest = mail_list[-10:]

result, data = mail.uid('fetch', ",".join(latest), '(BODY[HEADER])')

i = 0
for msg in data:
    if msg != ')':
      email_msg = email.message_from_string(msg[1])
      print "%s:   %5s\n\t%s" % (i, email_msg['From'], email_msg['Subject'])
      i = i+1

msg = input('Please select a message:\n')
if msg != '':
    result, data = mail.uid('fetch', latest[msg], '(RFC822)')
    raw_email = data[0][1]
    file = open('pickmail.out', 'w')
    file.write(raw_email)
    file.close()

mail.close()
mail.logout()
