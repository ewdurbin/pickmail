#!/usr/bin/env python

import pickmail
import pprint

PERSIST=False

config = pickmail.Config()
config.setup_config(persist=PERSIST)

connection = pickmail.Connection(config)

data = {}

def print_messages(offset=0):
    global data
    data = connection.dict_of_messages(offset=offset)
    for k, v in data.items():
        print v['info']

offset=0
print_messages()

selected = -1
while selected < 0:
    print data
    msg = raw_input('Please select a message, or press return for more:\n')
    if msg == '':
        offset = offset + 10
        print_messages(offset=offset)
    else:
        selected = msg

print selected

if selected != '':
    uid = data[int(selected)]['uid']
    file = open('pickmail.out', 'w')
    file.write(connection.fetch_message(uid))
    file.close()
