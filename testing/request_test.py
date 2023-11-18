import requests
import time
import json
while True:
    requests.post('https://maker.ifttt.com/trigger/upload/with/key/bbjfHVzAJdB9CXZvDVzHJg', data = { "value1" : "A1", "value2" : time.ctime() })
    print("requested")
    r = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1iSyVdRjjzZtXSrmlszfb8sUyUQYhcumKDRL2FXEvuyk/values/time?key=AIzaSyDmzyU8HCx85t0WlN_FAQn3TKELmvAbfGI").text
    print(((json.loads(r)["values"])[0])[0])
    time.sleep(5)