import os
import discord
import csv

bot_token = os.getenv('dog_bot')

#print(bot_token)
client = discord.Client()

filename = "links.csv"

rows = []

# reading csv file 
with open(filename, 'r') as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            link = str(row[0])
            line_count += 1
#print(link)

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("?cute"):
        await message.channel.send(link)
client.run(bot_token)
