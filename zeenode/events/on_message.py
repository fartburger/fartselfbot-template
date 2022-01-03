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

bot = zeenode.Bot(command_prefix=prefix, self_bot=True)
botid = <ID of bot account> #must be int
stargetid = ""
stalkmode = False

class on_message(zeenode.Cog):

    def __init__(self, bot):
        self.bot = bot

    @zeenode.Cog.listener()
    async def on_message(self, message):
        conten = await message.channel.history(limit=1).flatten()
        content = conten[0].content
        channel = message.channel
        if "discord.gg/" in content:
            with open("C:\\Users\\campbell\\Desktop\\fartselfbot\\zeenode\\logs\\invites.txt",'a') as file:
                file.write("Scraped invite from user: "+message.author.name+" in server: "+message.guild.name+", channel: \n"+message.channel.name+": "+content+"\nmessage link: "+message.jump_url+"\n\n")
        global stalkmode,stargetid
        if stalkmode and str(message.author.id) == str(stargetid):
            print(message.author.name+" spotted sending messages in: "+message.guild.name)
            with open("C:\\Users\\campbell\\Desktop\\fartselfbot\\zeenode\\logs\\stalking.txt",'a') as file:
                file.write(message.author.name+" ["+str(conten[0].created_at)+" UTC]: "+content+"\n")
                print(content)
                if len(conten[0].attachments) > 0:
                    file.write("("+str(len(conten[0].attachments))+" attachments)\n")
            if len(conten[0].attachments) > 0:
                now = datetime.now()
                time = now.strftime("%m.%d.%Y, %H.%M.%S %Z")
                for att in conten[0].attachments:
                    await att.save("stalked "+time+""+str(att.filename[-4:]))
                    print("saved attachment "+att.filename)
        if str(message.author.id) != str(botid):
            splitstr = content.split(" ")
            for men in message.mentions:
                if men.id == botid and len(content.split(" "))<=1:
                    await channel.send("hello <@" + str(message.author.id) + ">")
                    break
            if "<@!"+str(botid)+"> mic up" in content.lower():
                try:
                    vc = message.author.voice.channel
                    await vc.connect()
                except Exception:
                    pass
            try:
                if "nsfw" in content and splitstr[0] == "<@!"+str(botid)+">":

                    #### YOUR BOTS ACCOUNT MUST BE IN RAM RANCH DISCORD SERVER FOR THIS TO WORK, CAUSE IM NOT DOWNLOADING ANY OF THE HORRENDOUS SHIT IN THAT CHANNEL
                    
                    if "nodelete" in content:
                        nodelete = True
                    else:
                        nodelete = False
                    client = discord.Client()
                    imgpoolguild = self.bot.get_guild(911324607968071690)
                    imgpoolchannel = imgpoolguild.get_channel(911324609448673295)
                    chistory = await imgpoolchannel.history(limit=80).flatten()
                    rand = random.choice(chistory)
                    while len(rand.attachments) == 0 or not ".mp4" in rand.attachments[0].filename:
                        rand = random.choice(chistory)
                    attachment = rand.attachments[0]
                    GROSS = await channel.send(attachment.url)
                    if not channel.is_nsfw() and not nodelete:
                        await GROSS.delete(delay=30.0)
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)
            try:
                if len(splitstr)>=2 and "stalk" == splitstr[1] and str(message.author.id)=="872543618391490560":
                    stargetid = splitstr[2]
                    stalkmode = True
                    await message.channel.send("stalking user with id "+stargetid)
            except Exception as e:
                print("ignore")
            try:
                if len(splitstr)>=2 and "endstalk" == splitstr[1] and stalkmode == True and str(message.author.id) == "872543618391490560":
                    stalkmode = False
                    await message.channel.send("no longer stalking user with id "+stargetid)
            except Exception as e:
                print("ignore")
            try:
                if splitstr[0]=="<@!"+str(botid)+">":
                    if len(splitstr) >= 2:
                        if splitstr[1] and splitstr[1] == "spam":
                            amount = int(splitstr[2])
                            spammsg = ""
                            try:
                                for i in range(3, len(splitstr)):
                                    spammsg = spammsg + splitstr[i] + " "
                                for i in range(amount):
                                    await channel.send(spammsg)
                            except Exception as e:
                                print(type(e))
                                print(e.args)
                                print(e)
                        elif splitstr[1]=="thcspam":
                            for i in range(30):
                                serverin = message.guild
                                for channelin in serverin.text_channels:
                                    try:
                                        for i in range(10):
                                            await channelin.send("@everyone THUG HOLE CHOCOLATE!!! YEAAAAAHHHHHH!!!! https://media.discordapp.net/attachments/909343520752533537/915809545589260298/caption-2.gif :troll:")
                                            #delay.sleep(0.05)
                                    except Exception as e:
                                        print(type(e))
                                        print(e.args)
                                        print(e)
                        elif splitstr[1]=="gsearch":
                            amount = int(splitstr[2])
                            searchq = ""
                            try:
                                for i in range(3, len(splitstr)):
                                    searchq = searchq + splitstr[i] + " "
                                #gsearch(searchq)
                            except Exception as e:
                                print(type(e))
                                print(e.args)
                                print(e)
                        
                        elif splitstr[1]=="help":
                            #### if you'd like to add a feature and dont know how to implement it yourself, let me know and ill add it
                            helpmsg = """```
                            prefix: ping the bot
                            current commands:
                            help
                            get location <ip address>
                            nsfw <(optional) nodelete> - without nodelete flag, image will be automatically removed in 30 seconds unless in an nsfw channel.
                            spam <amount> <message> - sends <message> <amount> times
                            harass <target user's id(mentions dont work)> <message count> <message .. >
                            
                            more commands to be added..
                            ```
                            """
                            print("sent help")
                            await channel.send(helpmsg+"g")
                    elif len(splitstr) > 3:
                        if "get location" in content:
                            try:
                                ipaddress = splitstr[3]
                                details = handler.getDetails(ipaddress)
                                await channel.send(details.city + ", " + details.region + ". " + "lat/lon: " + details.loc + ". " + "zip code: " + details.postal)
                                await channel.send(random.choice(trollfaces))
                            except Exception as e:
                                print(type(e))
                                print(e.args)
                                print(e)
                                await channel.send("invalid ip address idiot")
                            
            except Exception as error:
                print(type(error))
                print(error.args)
                print(error)

    def client_headers(self):
        return {
            'Authorization': token,
            'Content-Type': 'application/json',
        }


def setup(bot):
    bot.add_cog(on_message(bot))
