import requests, json, urllib, websocket
from bs4 import BeautifulSoup
from selenium import webdriver

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    msg = json.loads(message)
    if msg["lat"] <=50 and msg["lat"]>=48:
        if msg["lon"]<=21 and msg["lon"]>=18:
            print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    ws.send('{"west":-180,"east":180,"north":-90,"south":90}')

if __name__=="__main__":
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://ws2.blitzortung.org:8050/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open)
    ws.run_forever()

driver = webdriver.Chrome()
temp=[]
driver.get("http://91.220.17.198/Zakopane/1")
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
for a in soup.findAll('a', href=True, attrs={'class':'col-xs-6 set text-left'}):
    dzistemp = a.find('div', attrs={'class':'col-xs-12 temp'})
    print(temp.a.append(dzistemp.text))

'''
odpowiedz = urllib.request.urlopen("http://91.220.17.198/data/region/Zakopane")

y = json.loads(odpowiedz.read())

for x in y['data']['stations']:
    print(y["data"]["stations"][x]["name"])
    print(y["data"]["stations"][x]["position"])
'''