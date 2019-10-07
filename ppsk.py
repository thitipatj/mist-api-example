import ConfigParser
import requests
import json

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

url = "https://api.mist.com/api/v1/sites/"+Config.get('Global_Var', 'SITE')+"/psks"

guest_name = raw_input("Enter your name : ")
t = guest_name.split(" ")
#print t[1]

d = {}
d["name"] = t[1]
d["passphrase"] = t[1]
d["ssid"] = "Mist-PPSK"
d["usage"] = "multiple"

#print json.dumps(d, ensure_ascii=False)

payload = json.dumps(d, ensure_ascii=False)

headers = {
    'Content-Type': "application/json",
    'Authorization': "Token "+Config.get('Global_Var', 'TOKEN'),
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "2eb28a83-192f-4eae-b892-30dfc7c79557,eda81e38-9ab8-46e7-a2fb-dbf092e9b186",
    'Host': "api.mist.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "106",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)