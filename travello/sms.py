import requests
import json

url="http://site.bulksmsnagpur.net/sendsms?uname=sunilj1&pwd=sunilj1&senderid=SUNILJ&to=8329258755&msg='T1e1s1t hr uju 1i1n1g1%20'sms&route=T"

response = requests.request("POST",url)



