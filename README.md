# HOPR Node Notification
Simple script to get the status of a node via Telegram. 

## Telegram bot Node Notification

This bot checks the availability of the node (or multiple nodes) every hour and sends a notification about the status of the node(s). A notification can be sent always or only when the availability changes. 

## Installation

1. Clone the repository : <br> `git clone https://github.com/Ziltar/HOPR_Node_Notification.git && cd HOPR_Node_Notification` 
2. Install requirements:  <br> `pip install requirements.txt `
3. Edit the *settings.py* File: <br>
<b>NODES:</b> HOPR Node Address(es)<br>
*Example:*<br> `NODES = ["16Uiu2HAmH3RhgTDN6cwysRnMtMf4jfzsvKuyuKPu5iDRZUZiVsqx", "16Uiu2HAkuTsuFSak6UJeF2w3KV2uzoNSpuGNFKC2vyLt63BpwuDC"]`<br>
<b>TELEGRAM_TOKEN</b><br>
*Example:* <br>`TELEGRAM_TOKEN  =  "5475148206:ABBc0fhQSwfBjKioPwbaZ9uxEPkpsgqbgi"`<br>
You can get your token here: https://t.me/BotFather <br>
<b>TELEGRAM_ID</b><br>
You can use a bot to find out your ID: https://t.me/userinfobot<br>
*Example:*<br> `TELEGRAM_ID  =  "15915301634711"`<br>
<b>ON_CHANGE</b><br>
If True, the bot sends a notification only when the availability changes (24 hours). If False, a notification is sent every hour.<br>
*Example:* <br>`ON_CHANGE  =  True`<br>
<b>ON_REWARD_CHANGE</b><br>
If True, the bot sends a notification when reward changes.<br>
*Example:* <br>`ON_REWARD_CHANGE  =  True`<br>
<b>STAKE_WALLETS:</b> For reward status:<br>
*Example:*<br> `STAKE_WALLETS = ["0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000001"]`<br>
## Usage
Run main.py: `python3 main.py` <br><br>


