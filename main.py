import discord
import os
import requests
import json

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("hello!")

    if message.content.startswith("$motivasi"):
        quote = get_quote()
        await message.channel.send(quote)

# with env
# token = os.getenv("DISCORD_TOKEN")
# client.run(token)

client.run("ODI4MTI0NTYyMDI0OTU1OTI1.YGlBGQ.2c-wk0KnEjmp5sZnYi2ka-GFL0c")
