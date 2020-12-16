import os
import discord
import csv
from pypexels import PyPexels

bot_token = os.getenv('dog_bot')
pexels_token = os.getenv('pexels_api')

id=[]
links=[]
#print(bot_token)
client = discord.Client()

py_pexels = PyPexels(api_key=pexels_token)

search_results = py_pexels.search(query='Animals', per_page=5)

i = 0
while i < 5:
    for photo in search_results.entries:
        id.append(photo.id)
        l = f"https://images.pexels.com/photos/{photo.id}/pexels-photo-{photo.id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
        links.append(l)
        i+=1
        
#print(links)

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("?cute"):
        for link in links:
            await message.channel.send(link)
client.run(bot_token)
