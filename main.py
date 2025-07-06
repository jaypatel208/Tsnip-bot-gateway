import os
import discord
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

keep_alive()  # start the web server

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Tsnip is online: {client.user}")


client.run(TOKEN)
