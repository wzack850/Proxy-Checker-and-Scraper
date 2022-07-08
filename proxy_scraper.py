import requests
import threading
import time
import re
from bs4 import BeautifulSoup
from colorama import init, Fore

class ProxyHandler():
    def __init__(self, filename: str):
        self.filename = filename
        self.proxies = []

    def scrape_proxies(self):
        urls = """
https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt
http://globalproxies.blogspot.com/
http://www.cybersyndrome.net/plz.html
http://www.cybersyndrome.net/plr5.html
http://biskutliat.blogspot.com/
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html
http://www.cybersyndrome.net/pla5.html
http://vipprox.blogspot.com/2013_06_01_archive.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html
http://vipprox.blogspot.com/p/blog-page_7.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html
http://vipprox.blogspot.com/2013_02_01_archive.html
http://alexa.lr2b.com/proxylist.txt
http://vipprox.blogspot.com/2013_03_01_archive.html
http://browse.feedreader.com/c/Proxy_Server_List-1/449196260
http://browse.feedreader.com/c/Proxy_Server_List-1/449196258
http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html#comment-form
http://browse.feedreader.com/c/Proxy_Server_List-1/449196251
http://free-ssh.blogspot.com/feeds/posts/default
http://browse.feedreader.com/c/Proxy_Server_List-1/449196259
http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html
http://proxyfirenet.blogspot.com/
https://www.javatpoint.com/proxy-server-list
https://openproxy.space/list/http
http://proxydb.net/
https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/http.txt
https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/https.txt
https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt
https://raw.githubusercontent.com/Natthanon823/steam-account-checker/main/http.txt
http://olaf4snow.com/public/proxy.txt
http://westdollar.narod.ru/proxy.htm
https://openproxy.space/list/socks4
https://openproxy.space/list/socks5
http://tomoney.narod.ru/help/proxi.htm
http://sergei-m.narod.ru/proxy.htm
http://rammstein.narod.ru/proxy.html
http://greenrain.bos.ru/R_Stuff/Proxy.htm
http://inav.chat.ru/ftp/proxy.txt
http://johnstudio0.tripod.com/index1.htm
http://atomintersoft.com/transparent_proxy_list
http://atomintersoft.com/anonymous_proxy_list
http://atomintersoft.com/high_anonymity_elite_proxy_list
http://atomintersoft.com/products/alive-proxy/proxy-list/3128
http://atomintersoft.com/products/alive-proxy/proxy-list/com
http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/
http://atomintersoft.com/products/alive-proxy/socks5-list
http://atomintersoft.com/proxy_list_domain_com
http://atomintersoft.com/proxy_list_domain_edu
http://atomintersoft.com/proxy_list_domain_net
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt
http://atomintersoft.com/proxy_list_domain_org
http://atomintersoft.com/proxy_list_port_3128
http://atomintersoft.com/proxy_list_port_80
http://atomintersoft.com/proxy_list_port_8000
http://atomintersoft.com/proxy_list_port_81
http://hack-hack.chat.ru/proxy/allproxy.txt
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
http://hack-hack.chat.ru/proxy/anon.txt
http://hack-hack.chat.ru/proxy/p1.txt
http://hack-hack.chat.ru/proxy/p2.txt
http://hack-hack.chat.ru/proxy/p3.txt
http://hack-hack.chat.ru/proxy/p4.txt
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
https://free-proxy-list.net/
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt
https://www.us-proxy.org/
https://free-proxy-list.com/
https://sunny9577.github.io/proxy-scraper/proxies.txt
https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all
https://spys.one/
https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all
"""

        def pattern_one(url):
            ip_port = re.findall("(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})", url)

            if not ip_port: 
                pattern_two(url)
            else:
                for i in ip_port:
                    self.proxies.append(i)

        def pattern_two(url):
            ip = re.findall(">(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<", url)
            port = re.findall("td>(\d{2,5})<", url)

            if not ip or not port: 
                pattern_three(url)
            else:
                for i in range(len(ip)):
                    self.proxies.append(i)

        def pattern_three(url):
            ip = re.findall(">\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})", url)
            port = re.findall(">\n[\s]+(\d{2,5})\n", url)

            if not ip or not port: 
                pattern_four(url)
            else:
                for i in range(len(ip)):
                    self.proxies.append(i)

        def pattern_four(url):
            ip = re.findall(">(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<", url)
            port = re.findall(">(\d{2,5})<", url)

            if not ip or not port:
                pattern_five(url)
            else:
                for i in range(len(ip)):
                    self.proxies.append(i)

        def pattern_five(url):
            ip = re.findall("(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})", url)
            port = re.findall("(\d{2,5})", url)

            for i in range(len(ip)):
                    self.proxies.append(i)

        def start(url):
            try:
                headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
                req = requests.get(url, headers=headers).text
                pattern_one(req)
                print(Fore.CYAN + f"Scraped proxies from: {Fore.MAGENTA + url}" + "\n")
            except:
                pass

        threads = list()
        for url in urls.splitlines():
            if url:
                x = threading.Thread(target=start, args=(url, ))
                x.start()
                threads.append(x)

        for th in threads:
            th.join()
        
    def check(self, proxylist):
        for proxy in proxylist:
            try:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
                requests.get("https://httpbin.org/ip", headers=headers, proxies={"http": proxy,"https": proxy}, timeout=1)
                
                print(Fore.GREEN + "SUCCESS: " + proxy + "\n")

                with open(self.filename, "a") as f:
                    f.write(proxy + "\n")
            except:
                print(Fore.RED + "FAIL   : " + proxy + "\n")

    def check_proxies(self):
        open(self.filename, "w").close()

        self.scrape_proxies()

        time.sleep(10)
        print(Fore.GREEN + "\n" + f"Scraped {len(self.proxies)}")
        time.sleep(0.5)
        print(Fore.BLUE + "Starting checking process...\n")
        time.sleep(2)

        self.optimize_proxies()

        for i in self.proxies:
            threading.Thread(target=self.check, args=(i,)).start()
    
    def optimize_proxies(self):
        n = 0
        l = 0

        while round(n) != len(self.proxies)//100:
            l += 1
            n = len(self.proxies) // l
        
        self.proxies = [self.proxies[x:x+n] for x in range(0, len(self.proxies), n)]

    def cleanup(self):
        contents = open(self.filename, "r").readlines()
        new_proxies = []

        for i, v in enumerate(contents):
            if v == "":
                contents.pop(i)

        for x in contents:
            if not x in new_proxies:
                new_proxies.append(x)

        open(self.filename, "w").close()

        with open(self.filename, "a") as f:
            f.write("".join(new_proxies))

init(convert=True)
handler = ProxyHandler("proxylist.txt")
handler.check_proxies()