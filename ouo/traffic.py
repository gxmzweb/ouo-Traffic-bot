from requests import options
from selenium import webdriver
from time import  sleep
import random
url_list =["http://ouo.io/ref/bcNFXpsz", "https://ouo.io/Flv2PDw","https://ouo.io/bMhxSwb"]

options = webdriver.ChromeOptions()




proxyList = open("C:\src\Projects0\ouo\proxy-scraper\workingProxies.txt","r").readlines()

def main(index):
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
    PROXY = proxyList[index]
    print(PROXY)
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,

    "proxyType": "MANUAL",

    }
    
    driver = webdriver.Chrome("C:\src\Projects0\ouo\chromedriver.exe",options=options)
    rSleep = random.randint(1,9)
    rnd = random.randint(0,2)
    url = url_list[rnd]
    print(url)
    driver.get(url)
    sleep(rSleep)
    driver.find_element_by_id("btn-main").click()
    sleep(3)
    sleep(rSleep)
    driver.find_element_by_id("btn-main").click()
    sleep(rSleep)
    driver.quit()



for i in range(len(proxyList)):
    try:
        main(i)
    except:
        pass


        