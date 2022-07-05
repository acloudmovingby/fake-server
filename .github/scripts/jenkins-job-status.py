#!/usr/bin/python

import sys
import requests

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

r = requests.get('http://20.106.205.93:8080/job/fake-server-pipeline/31/')
success = str(r.content).find('tooltip=\"Success') != -1
print("found_success=" + str(success))

