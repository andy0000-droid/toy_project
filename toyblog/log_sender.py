"""
Send Server log to Discord
"""

import json
from datetime import datetime

# import requests

webhook_url = "https://discord.com/api/webhooks/1277504780272537600/L1l0panclHJQ3qDL-8dDi9xF8GEkKp1As1n7ER2u6aUMkEbAgjgAIgHFVH0-CrKe9f8z"


def send_log(text: str):
    headers = {"Content-Type": "application/json"}
    nowtime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    text = "Time: {}\n{}".format(nowtime, text)
    payload = json.dumps({"content": text})
    r = requests.post(url=webhook_url, data=payload, headers=headers)


if __name__ == "__main__":
    send_log("Testing message")
