import requests, json, urllib, websocket

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
    print('### closed ###')

def on_open(ws):
    ws.send('{"west":-180,"east":180,"north":-90,"south":90}')

def temp():
    req = urllib.request.urlopen("http://91.220.17.198/data/station/Zakopane")
    x = json.loads(req.read())
    print("Temperatura " + str(x['data']['forecast'][0]['date']) + " : " + str(x['data']['forecast'][0]['t']) + " st. C")
    print("Temperatura obecna: " + str(x['data']['measurements']['t']['value']) + " st. C")



if __name__=="__main__":
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://ws2.blitzortung.org:8050/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open)
    temp()
    ws.run_forever()



'''
odpowiedz = urllib.request.urlopen("http://91.220.17.198/data/region/Zakopane")

y = json.loads(odpowiedz.read())

for x in y['data']['stations']:
    print(y["data"]["stations"][x]["name"])
    print(y["data"]["stations"][x]["position"])

'''

