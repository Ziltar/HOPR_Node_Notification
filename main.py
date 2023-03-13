from settings import TELEGRAM_TOKEN, TELEGRAM_ID, NODES, ON_CHANGE, STAKE_WALLETS, ON_REWARD_CHANGE
import requests, time
import pandas

URL = "https://network.hoprnet.org/api/getNodes?env=36"
REWARD_URL = "https://stake.hoprnet.org/api/getRewards?peerId="
stats = {}
reward = 0

while True:
    try:
        response = requests.request("GET", URL)
        msg = ""
        change = False
        for node in response.json()['nodes']:
            if node["peerId"] in NODES:
                if ON_CHANGE:
                    if node["peerId"] in stats:
                        if stats[node["peerId"]] != node["availability24h"]:
                            change = True
                    else:
                        change = True
                    stats[node["peerId"]] =  node["availability24h"]    

                msg += "Node: " + node["peerId"] + "\nAvailability: " + str(node["availability"]*100) + "\nAvailability 24h: " + str(node["availability24h"]*100) + "%\nLatency:" + str(node["latencyAverage"]) + "\nLastSeen:" + str(pandas.to_datetime((node["lastSeen"]), unit='ms')) + "\n\n"
        total_reward = 0
        for address in STAKE_WALLETS:
            response = requests.request("GET", REWARD_URL+address)
            total_reward += (response.json()[0][0]['rewards'])
      
        msg+= "\n💸Reward:" + str(total_reward) + " HOPR"
        if (not ON_CHANGE) or (ON_CHANGE and change):
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_ID}&parse_mode=HTML&text=<code>{msg}</code>"
            requests.get(url)
        elif (ON_REWARD_CHANGE and (reward  != total_reward)):
            msg = "💸Reward:" + str(total_reward) + " HOPR"
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_ID}&parse_mode=HTML&text=<code>{msg}</code>"
            requests.get(url)
            reward = total_reward

    except Exception as e:
        print(str(e))
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_ID}&parse_mode=HTML&text=<code>Something went wrong!</code>"
        requests.get(url)        
    time.sleep(1800)
