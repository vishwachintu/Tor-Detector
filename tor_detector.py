
import requests
import json
from itertools import product
from random import choice
import sys

#Settings:
#Log File Name:
logfile = 'onionsdetected.txt'
onion_count = 0
onions_found = 0

#values used in site address space:
domain_values = "abcdefghijklmnopqrstuvwxyz234567"

#Proxy port:
proxy = '9150'

#Connection timeout(Higher for slower connections; stay above 1):
time = 1.5

proxies = {
    'http': 'socks5h://127.0.0.1:' + proxy,
    }
print("\nTor Detector\n")
print("This script creates a random onion site and uses a http GET request to if it is live.\nIf a site is detected, site code will be displayed and it will be logged into a file for you to further investigate.\n")
print("\nA bruteforce onion scanner created because why not?\n")
print("\n\n\n'Ambitous, yet rubbish.'")
print("\n                  -Vishwa(DrPinnacle)\n")
print("\nPress 'CTRL + C' to exit\n\nResults:")

#main loop:
with open(logfile, 'a') as f:
        x = 1
        while True:
            try:        
                onion = "".join([choice(domain_values) for _ in range(16)])#Creates random onion
                fullURL = "http://" + onion + ".onion"#Packages onion into url for request
                onion_count = onion_count + 1
                data = requests.get(fullURL, proxies=proxies, timeout=time).text#Data request
                print(data)#Print of data
                dataEntry = fullURL
                print(fullURL + " is active \n")
                onions_found = onions_found + 1
                f.write(dataEntry + "\n")
            #Exception City
            except requests.exceptions.ConnectTimeout:
                print ('Address: ' + fullURL + ' timed out. Nothing to see. Generating next onion site.')
            except requests.exceptions.RequestException as e:
                print(e)
                dataEntry = e
            except KeyboardInterrupt:#exit
                print ('\nScan exited by user input.\n\nOnions Checked: ' + str(onion_count) + '\nOnions Found: ' + str(onions_found))
                print('\n\nCheck ' + logfile + ' for detected onions.\n')
                print("You were so preocupied with whether or not you could,\nyou didn't stop to think if you should.")
                print('\n                                  -Vishwa(DrPinnacle)\n\n ')
                sys.exit()

sys.exit()
