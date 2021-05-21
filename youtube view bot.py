from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from random import randint
from time import sleep

# set proxy

proxy_ip_port = 'IP:Port'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# let's call the browser

driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.get("https://www.youtube.com/watch?v=*************")
sleep(randint(1200, 1800))

# close browser
driver.quit

# Thanks for watching and please subscribe for more :)
#Git code in the description 
# GOOD BYE