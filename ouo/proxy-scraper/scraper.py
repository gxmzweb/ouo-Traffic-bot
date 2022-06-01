import requests


print("scraping...")
text = open("proxies.txt","a")
text.truncate(0)

urls =["https://api.openproxylist.xyz/http.txt","https://api.openproxylist.xyz/socks5.txt","https://api.openproxylist.xyz/socks4.txt","https://www.proxy-list.download/api/v1/get?type=socks5","https://www.proxy-list.download/api/v1/get?type=socks4","https://www.proxy-list.download/api/v1/get?type=http","https://api.proxyscrape.com/?request=getproxies","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt","http://alexa.lr2b.com/proxylist.txt","http://www.proxylists.net/http_highanon.txt","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt","http://olaf4snow.com/public/proxy.txt","http://inav.chat.ru/ftp/proxy.txt","http://hack-hack.chat.ru/proxy/allproxy.txt","http://hack-hack.chat.ru/proxy/anon.txt", "http://hack-hack.chat.ru/proxy/p1.txt", "http://hack-hack.chat.ru/proxy/p2.txt", "http://hack-hack.chat.ru/proxy/p3.txt", "http://hack-hack.chat.ru/proxy/p4.txt","https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt","https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt","https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt","https://api.proxyscrape.com/v2/?request=getproxies&timeout=10000&country=all&ssl=all&anonymity=alll"]
for i in range(len(urls)-1):
    a = requests.get(urls[i]).text
    
    text.write(a)

text.close()


