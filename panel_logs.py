# Packages
import os
import requests
import random
from dotenv import load_dotenv
load_dotenv()

# Discord BOT Token
token = os.getenv("BOT_TOKEN")

# Panel Log Channels
logChannels = [
    "1043793587013427200",
    "1043595564169842759"
]

# Random Color Generator
def randomColor():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number = f"#{hex_number[2: ]}"

    value = hex_number.lstrip("#")
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

print(randomColor())

# Claim
def Claim(botData):
    embed = {
        "title": "Select List Panel",
        # "color": "0xff0000",
        "fields": [{
            "name": "Application/Bot",
            "value": f"{botData.username} (<@{botData.bot_id}>)"
        }, {
            "name": "Action",
            "value": "Claimed"
        }, {
            "name": "Reason/Notes",
            "value": "Reason cannot be supplied, for the Claim action!"
        }, {
            "name": "Moderator",
            "value": "Metro Reviews"
        }]
    }

    for channel in logChannels:
        requests.post(
            url=f"https://discord.com/api/v9/channels/{channel}/messages", 
            headers={
                "Authorization": f"Bot {token}",
                "Content-Type": "application/json"
            },
            json={
                "embeds": [embed]
            }
        )

# Unclaim
def Unclaim(botData, reason):
    embed = {
        "title": "Select List Panel",
        # "color": "0xff0000",
        "fields": [{
            "name": "Application/Bot",
            "value": f"{botData.username} (<@{botData.bot_id}>)"
        }, {
            "name": "Action",
            "value": "Unclaimed"
        }, {
            "name": "Reason/Notes",
            "value": reason
        }, {
            "name": "Moderator",
            "value": "Metro Reviews"
        }]
    }

    for channel in logChannels:
        requests.post(
            url=f"https://discord.com/api/v9/channels/{channel}/messages", 
            headers={
                "Authorization": f"Bot {token}",
                "Content-Type": "application/json"
            },
            json={
                "embeds": [embed]
            }
        )

# Approve
def Approve(botData, reason):
    embed = {
        "title": "Select List Panel",
        # "color": "0xff0000",
        "fields": [{
            "name": "Application/Bot",
            "value": f"{botData.username} (<@{botData.bot_id}>)"
        }, {
            "name": "Action",
            "value": "Approved"
        }, {
            "name": "Reason/Notes",
            "value": reason
        }, {
            "name": "Moderator",
            "value": "Metro Reviews"
        }]
    }

    for channel in logChannels:
        requests.post(
            url=f"https://discord.com/api/v9/channels/{channel}/messages", 
            headers={
                "Authorization": f"Bot {token}",
                "Content-Type": "application/json"
            },
            json={
                "embeds": [embed]
            }
        )

# Deny
def Deny(botData, reason):
    embed = {
        "title": "Select List Panel",
        # "color": "0xff0000",
        "fields": [{
            "name": "Application/Bot",
            "value": f"{botData.username} (<@{botData.bot_id}>)"
        }, {
            "name": "Action",
            "value": "Denied"
        }, {
            "name": "Reason/Notes",
            "value": reason
        }, {
            "name": "Moderator",
            "value": "Metro Reviews"
        }]
    }

    for channel in logChannels:
        requests.post(
            url=f"https://discord.com/api/v9/channels/{channel}/messages", 
            headers={
                "Authorization": f"Bot {token}",
                "Content-Type": "application/json"
            },
            json={
                "embeds": [embed]
            }
        )
