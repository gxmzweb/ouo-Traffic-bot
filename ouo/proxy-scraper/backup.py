import concurrent.futures
import urllib.request , socket
socket.setdefaulttimeout(8)
# read the list of proxy IPs in proxyList
proxyList = open("proxies.txt","r").readlines()
a = open("workingProxies.txt","a")
a.truncate(0)
a.close()
def is_bad_proxy(pip):   
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
        #sock=urllib.urlopen(req)
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0


def check(item):
    if is_bad_proxy(item):
        #print ("Bad Proxy", item)
        pass
    else:
        print (item, "is working")

        with open("workingProxies.txt","a") as w:
            if "\n" in item:
                w.write(str(item))
            else:
                w.write(str(item)+"\n")


with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
    executor.map(check,proxyList)
    