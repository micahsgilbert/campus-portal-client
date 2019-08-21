#!/usr/bin/env python3
import requests
import request
import json

with open("client_config.txt") as f:
    dat = f.read().split("\n")

username = dat[0]
password = dat[1]

s = requests.Session()
request.makeLoginAttempt(s, username, password)

notifs = request.getNotificationNum(s)

print(notifs)
