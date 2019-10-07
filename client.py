import ConfigParser
import requests
import json

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
#print (Config.get('Global_Var', 'ORG'))


url = "https://api.mist.com/api/v1/sites/"+Config.get('Global_Var', 'SITE')+"/stats/clients"

headers = {
    'Content-Type': "applicantion/json",
    'Authorization': "Token "+Config.get('Global_Var', 'TOKEN'),
    'cache-control': "no-cache",
    'Postman-Token': "9db0e494-9517-4dec-9bcd-3fc31f046ef2"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

#for element in data:
#    print element

for element in data:
    print "Host Name: "+element['hostname']
    print "IP Address: "+element['ip']
    print "Location: x = "+str(element['x'])+" y = "+str(element['y'])
    print "RSSI: "+str(element['rssi'])
    print "---------------------------------------------------------------------"
