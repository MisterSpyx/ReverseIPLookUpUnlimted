from multiprocessing.pool import ThreadPool
import requests

red = '\033[91m'
green = '\033[92m'
white = '\033[00m'


def cms(url):
    try:
        url = url.replace('\n', '').replace('\r', '')
        if url.startswith('http://'):
            url = url.replace('http://', '')
        elif url.startswith("https://"):
            url = url.replace('https://', '')
        else:
            pass
        op = requests.get('http://' + url + '/admin/', timeout=10)
        op2 = requests.get('http://' + url + '/administrator/index.php', timeout=10)
        op3 = requests.get('http://' + url + '/wp-login.php', timeout=10)
        op4 = requests.get('http://' + url + '/user/login', timeout=10)
        op5 = requests.get('http://' + url, timeout=10)
        if ("dashboard" or "opencart") in op.text:
            print green + "[+] OPencarte http://" + url + white + '\n'
            open("Cms/Opencarte.txt", "a").write('http://' + url + '\n')
        elif "Joomla" in op2.text:
            print green + "[+] Joomla http://" + url + white + '\n'
            open("Cms/Joomla.txt", "a").write('http://' + url + '\n')
        elif "WordPress" in op3.text:
            print green + "[+] Wordpress http://" + url + white + '\n'
            open("Cms/wordpress.txt", "a").write('http://' + url + '\n')
        elif "sites/default" in op4.text:
            print green + "[+] Drupal http://" + url + white + '\n'
            open("Cms/drupal.txt", "a").write('http://' + url + '\n')
        elif "PrestaShop" in op5.text:
            print green + "[+] Prestashop http://" + url + white + '\n'
            open("Cms/drupal.txt", "a").write('http://' + url + '\n')

        else:
            print '[-] Cms Not Found --> http://' + red + url + '\n'

    except:
        pass


ListPass = open(raw_input("Sites List .txt:"), 'r').readlines()
pool = ThreadPool(100)
pool.map(cms, ListPass)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success , Thank you for using Mr Spy Tool --> Result/Grabbed.txt")
