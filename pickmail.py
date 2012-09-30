#!/usr/bin/env python

import pickmail
import pprint

PERSIST=False

config = pickmail.Config()
config.setup_config(persist=PERSIST)

connection = pickmail.Connection(config)
data = connection.dict_of_messages()

for k, v in data.items():
    print v['info']

msg = input('Please select a message:\n')
if msg != '':
    uid = data[msg]['uid']
    file = open('pickmail.out', 'w')
    file.write(connection.fetch_message(uid))
    file.close()
