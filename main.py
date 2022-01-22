import discord
import os
import random

from replit import db



client = discord.Client()

#crypto_words = ["crypto", "btc", "lightning"]

def add_pic(img):
  pictures = db["pics"]
  pictures.append(img)
  db["pics"] = pictures
  
  

def delete_pic(index):
  pictures = db["pics"]
  if len(pictures) > index:
    del pictures[index]
  db["pics"] = pictures


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$icecream'):
    await message.channel.send("I like ice cream and I am retarded")

  if msg.startswith('$pic'):
    await message.channel.send(random.choice(db["pics"]))

  if msg.startswith('$new'):
    image_link = msg.split("$new ", 1)[1]
    add_pic(image_link)
    await message.channel.send("New picture added!")

  if msg.startswith('$del'):
   pictures = []
   if "pics" in db.keys():
     index = int(msg.split("del",1)[1])
     delete_pic(index)
     pictures = db["pics"]
   await message.channel.send(pictures)
   


my_secret = os.environ['TOKEN']

#client.run(my_secret)


