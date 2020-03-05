import os
import re
from multiprocessing.dummy import Pool as ThreadPool

import requests
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

red = '\033[91m'
green = '\033[92m'
white = '\033[00m'

req_proxy = RequestProxy()
os.system('cls' if os.name == 'nt' else 'clear')
logo = '''  
______                               ___________   _                 _                
| ___ \                             |_   _| ___ \ | |               | |               
| |_/ /_____   _____ _ __ ___  ___    | | | |_/ / | |     ___   ___ | | ___   _ _ __  
|    // _ \ \ / / _ \ '__/ __|/ _ \   | | |  __/  | |    / _ \ / _ \| |/ / | | | '_ \ 
| |\ \  __/\ V /  __/ |  \__ \  __/  _| |_| |     | |___| (_) | (_) |   <| |_| | |_) |
\_| \_\___| \_/ \___|_|  |___/\___|  \___/\_|     \_____/\___/ \___/|_|\_\\__,_| .__/ 
                                                                               | |    
Mister Spy Tool View Dns Unlimited 

'''

print red + logo + white


def taz(i):
    try:
        i = i.replace('\n', '').replace('\r', '')
        api = 'https://viewdns.info/reverseip/?host=' + i + '&t=1'
        while True:
            request = req_proxy.generate_proxied_request(api)
            if '.com' in request.text:
                mrspy = re.findall('</tr><tr> <td>(.*?)</td><td align="center">', request.text)
                for i in mrspy:
                    if i.startswith("http//"):
                        print 'http://'+i
                        open('Grabbed.txt', "a").write('http://'+i + "\n")
                    elif i.startswith("https//"):
                        print 'http://'+i
                        open('Grabbed.txt', "a").write('http://'+i + "\n")
                    else:
                        print 'http://'+i
                        open('Grabbed.txt', "a").write('http://'+i + "\n")
                break
    except:
        pass
        print 'Maybe Your Internet Too Bad Or Not Working Contact Mr Spy'


ListPass = open(raw_input("Ips List .txt:"), 'r').readlines()
pool = ThreadPool(100)
pool.map(taz, ListPass)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success , Thank you for using Mr Spy Tool --> Grabbed.txt")
