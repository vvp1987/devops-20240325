import requests
import time

while True:
    time.sleep(5)
    result = requests.get('http://127.0.0.1:8090/time')
    #print(result.text)
    with open('result.txt', 'a') as logfile:
        logfile.write(result.text)
        logfile.write('\n')