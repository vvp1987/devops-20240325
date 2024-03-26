import requests
import time

while True:
    time.sleep(5)
    result = requests.get('http://myserver/time')
    #print(result.text)
    with open('/srv/log.txt', 'a') as logfile:
        logfile.write(result.text)
        logfile.write('\n')