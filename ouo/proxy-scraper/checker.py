import requests
text = open("proxies.txt","r").readlines()
working = open("workingProxies.txt","w")
url = "https://www.google.com/"
i = 0

for i in range(len(text)):
    prx = text[i]
    print(prx)
    proxies = {
    'http': 'http://'+prx,
    'https': 'http://'+prx,
    'socks4':'socks4://'+prx,
    'socks5':'socks5://'+prx
}
    try:
        r = requests.get(url,proxies=proxies,timeout=3000).status_code
        if r == 200:
            working.write(prx)
        else:
            pass
    except:
        print("not working")

pool = ThreadPool(500)
pool.map(is_bad_proxy)
pool.close()
pool.join()