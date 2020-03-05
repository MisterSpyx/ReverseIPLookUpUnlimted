import os
from platform import system

red = '\033[91m'
green = '\033[92m'
white = '\033[00m'
os.system('cls' if os.name == 'nt' else 'clear')

logo = ''' 

______                               ___________   _                 _                
| ___ \                             |_   _| ___ \ | |               | |               
| |_/ /_____   _____ _ __ ___  ___    | | | |_/ / | |     ___   ___ | | ___   _ _ __  
|    // _ \ \ / / _ \ '__/ __|/ _ \   | | |  __/  | |    / _ \ / _ \| |/ / | | | '_ \ 
| |\ \  __/\ V /  __/ |  \__ \  __/  _| |_| |     | |___| (_) | (_) |   <| |_| | |_) |
\_| \_\___| \_/ \___|_|  |___/\___|  \___/\_|     \_____/\___/ \___/|_|\_\\__,_| .__/ 
                                                                               | |    
                                                                               |_|    
Reverse IP Lookup By Mister Spy  , Done better then perfect                                   
--------------------------------------------------------------
- 1) Remove Duplicated Lines  
- 2) Get Ips From Domains
- 3) Live Ip Checker
- 4) Range List ips 1 - 255
- 5) zone-h grabber
- 6) Mass Reverse Ip Unlimited
----------------------------------------------------------------

'''

print red + logo + white

choice = raw_input('Enter Your Choice : ')

if choice == '1':
    from Scripts import dup
elif choice == '2':
    from Scripts import ipfromdomain
elif choice == '3':
    from Scripts import liveip
elif choice == '4':
    from Scripts import ranger
elif choice == '5':
    from Scripts import zone
elif choice == '6':
    if system() == 'Linux':
        os.system("chmod +x viewdns.py && python viewdns.py")
    if system() == 'Windows':
        os.system('viewdns.py')
else:
    print 'Wrong Choice Contact : https://www.facebook.com/007MrSpy'