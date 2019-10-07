import base64
import json
import ConfigParser
import requests
import json

import websocket  # websocket-client==0.44.0

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

msg_received = 0

email = 'youremail@'
password = 'yourpassword'


def on_message(ws, message):
    global msg_received
    print 'onmessage', message
    msg_received += 1
    if msg_received > 10:
        ws.send(json.dumps({"unsubscribe": "/sites/"+Config.get('Global_Var', 'SITE')+"/stats/maps/"+Config.get('Global_Var', 'MAP')+"/clients"}))
        ws.close()


def on_error(ws, error):
    print 'onerror'


def on_close(ws):
    print 'onclose'


def on_open(ws):
    print 'onopen'
    ws.send(json.dumps({"subscribe": "/sites/"+Config.get('Global_Var', 'SITE')+"/stats/maps/"+Config.get('Global_Var', 'MAP')+"/clients"}))


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://api-ws.mist.com/api-ws/v1/stream",
                                header=['Authorization: Basic %s' % base64.encodestring(email + ':' + password)],
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()