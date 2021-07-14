import os
import discord
import requests
import json
import praw


#instance of a client that talks to discord
client = discord.Client()

#return quote from ZenQuotes API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random/")
  #convert response to json
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

#create read-only Reddit instance
reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
)
#print(reddit.read_only)




@client.event #registers event
#Print to console that Smile Bot is logged in
async def on_ready():
  print('{0.user}'.format(client) + ' smiles upon you. :)') 
  #0 is replaced ith client

@client.event
async def on_message(message): 
  #triggers each time a message is recieved from user
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
    #send message back to channel
  
  if message.content.startswith('$inspire me'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.environ['SMILE_BOT_TOKEN'])


