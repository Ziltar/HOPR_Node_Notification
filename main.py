from settings import TELEGRAM_TOKEN, TELEGRAM_ID, NODES, ON_CHANGE
import requests, time

URL = "https://network.hoprnet.org/api/getNodes?env=36"
stats = {}

while True:
    response = requests.request("GET", URL)
    msg = ""
    change = False
    for node in response.json():
        if node["peerId"] in NODES:
            if ON_CHANGE:
                if node["peerId"] in stats:
                    if stats[node["peerId"]] != node["availability24h"]:
                        change = True
                else:
                    stats[node["peerId"]] =  node["availability24h"]
                    change = True

            msg += "Node: " + node["peerId"] + "\nAvailability: " + str(node["availability"]*100) + "\nAvailability 24h: " + str(node["availability24h"]*100) + "%\nLatency:" + str(node["latencyAverage"]) + "\nLastSeen:" + node["lastSeen"] + "\n\n"
    
    if (not ON_CHANGE) or (ON_CHANGE and change):
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_ID}&parse_mode=HTML&text=<code>{msg}</code>"
        requests.get(url).json()
    
    time.sleep(3600)