import re
import requests
from colorama import Fore
import discord
from discord.ext import commands as zeenode
from zeenode.load import token
from zeenode.config import nitro_sniper
from datetime import datetime
from zeenode.config import prefix
import time as delay
import ipinfo
import random
time = datetime.now().strftime("%H:%M:%S")
bot = zeenode.Bot(command_prefix=prefix,self_bot=True)
iptoken = 'aa492a02ecb8be'
handler = ipinfo.getHandler(iptoken)
#try:
#except Exception as e:
    #print(type(e))
trollfaces =("https://cdn.shopify.com/s/files/1/1355/1401/products/excited-troll-face-internet-meme-decal-sticker.jpg?v=1570926316","https://i.pinimg.com/736x/cb/7f/cf/cb7fcf56d757f7b9f4ac27ebe1c05001.jpg","https://i.redd.it/rsw0m9m0nvk71.png")

class on_message(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

    @zeenode.Cog.listener()
    async def on_message(self,message):
        delay.sleep(1)
        if str(message.author.id)!="772589373685760041":
            content = message.content
            channel = message.channel
            if content == "<@!772589373685760041>" or '<@!772589373685760041>' in content and "hello" in content or "yo " in content:
                await channel.send("hello <@"+str(message.author.id)+">")
            if "<@!772589373685760041> mic up" in content.lower():
                try:
                    vc = message.author.voice.channel
                    await vc.connect()
                except Exception:
                    pass
            if "<@!772589373685760041> join discord.gg/" in content:
                invite = content.split("discord.gg/")[1].split(" ")[0]
                print(invite)
                requests.post("https://discordapp.com/api/v6/invites/"+invite,headers={'authorization':token})
                await channel.send("joinin server discord.gg/"+invite)
            if content.startswith("<@!772589373685760041>"):
                splitstr = content.split(" ")
                if "get location" in content:
                    try:
                        ipaddress = splitstr[3]
                        details = handler.getDetails(ipaddress)
                        await channel.send(details.city+", "+details.region+". "+"lat/lon: "+details.loc+". "+"zip code: "+details.postal)
                        await channel.send(random.choice(trollfcaes))
                    except Exception:
                        print(Exception)
                if splitstr[1] and splitstr[1]=="nsfw":
                    client = discord.Client()
                    imgpoolguild = self.bot.get_guild(911324607968071690)
                    imgpoolchannel = imgpoolguild.get_channel(911324609448673295)
                    chistory = await imgpoolchannel.history(limit=80).flatten()
                    try:
                        rand = random.choice(chistory)
                        while len(rand.attachments)==0:
                            rand = random.choice(chistory)
                        attachment = rand.attachments[0]
                        await channel.send(attachment.url)
                    except Exception as e:
                        print(type(e))
                        print(e.args)
                        print(e)
                    
    
    def client_headers(self):
        return {
            'Authorization': token,
            'Content-Type': 'application/json',
        }

def setup(bot):
    bot.add_cog(on_message(bot))
