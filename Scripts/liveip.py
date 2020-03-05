import socket

from multiprocessing.dummy import Pool as ThreadPool


red = '\033[91m'
green = '\033[92m'
white = '\033[00m'


def taz(ip):
    try:
        ip = ip.replace('\n', '').replace('\r', '')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, 80))
        if str(result) != '0':
            print red + '[-] Dead -->' + ip + white
        if str(result) == '0':
            print green + '[+] Live Ip -->' + ip + white
            open("Result/LiveIps.txt", "a").write(ip + "\n")
    except:
        pass


ListPass = open(raw_input("Ips List .txt:"), 'r').readlines()
pool = ThreadPool(100)
pool.map(taz, ListPass)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success , Thank you for using Mr Spy Tool")
