from espn_api.basketball import League
import requests
import json
import os
import discord
import time

swid  = '{99418C0E-6F17-430B-B359-3974432C9F55}'
espn_s2 = 'AEBaL8rj2SyjuZqBWkPss2cSw%2F537QrgJsgIsBNh3R%2FlEs7EVpvXfokrGYAMt4a4K1xBNzi%2Br6TqU0OrD2yOOZUEXw%2BOuWnW880imHNSBf9y0T1WSnal4ZRYyKJeqo2uzX4PdzjoEz90MT8VCIB%2FqjoB443TvYxi2LVLiZLteFEWwc24Rb%2BxreKN3Mz1BET7To%2BP3JKV%2FIEXUsXrtl8v4i9tVA%2BSteyTOfdqr5o4GbOFvv8youyjlVu8b%2Brwl13I69uyrBScdPebsrgqzLJeBPcC'
league_id = '479409196'

league = League(league_id=479409196, year=2023, espn_s2= espn_s2, swid=swid)
class DiscordException(Exception):
    pass

class DiscordBot(object):
    # Creates Discord Bot to send messages
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def __repr__(self):
        return "Discord Webhook Url(%s)" % self.webhook_url

    def send_message(self, text):
        # Sends a message to the chatroom
        message = "```{0}```".format(text)
        template = {
            "content": message #limit 3000 chars
        }

        headers = {'content-type': 'application/json'}

        if self.webhook_url not in (1, "1", ''):
            r = requests.post(self.webhook_url,
                              data=json.dumps(template), headers=headers)

            if r.status_code != 204:
                print(r.content)
                raise DiscordException(r.content)

            return r
        
class PostedMessage(str):
    # Object that keeps track of last posted message
    def __init__(self):
        self.message = str
        
def send_message():
    try:
        discord_webhook_url = 'https://discord.com/api/webhooks/1032399519767339153/sa6Dun-8gd7xHJEaMutuPKZZA0Dik70eZFonn2XvldU1Db7sfMmCiU8uZSyEXF3lAHA4'
        str_limit = 3000
    except KeyError:
        discord_webhook_url = 1

    message_to_send = get_latest_transaction()
    discord_bot = DiscordBot(discord_webhook_url)
    discord_bot.send_message(message_to_send)
    
  
    return print('Message Sent')

def get_latest_transaction():
    activity = league.recent_activity()
    latest_transaction = str(activity[0])
    
    return latest_transaction        

def main():
    last_posted_message = None
    while True:
        latest_transaction = get_latest_transaction()
        if(last_posted_message == latest_transaction):
            print('No update.')
        else: 
            send_message()
            last_posted_message = latest_transaction
            print(latest_transaction)
            print(last_posted_message)
        time.sleep(15) # Sleep for 30 seconds
        
main()