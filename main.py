import discord
import os
from dotenv import load_dotenv
from keepalive import keep_alive

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Tsnip is online as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("Hey! I'm online 🚀")


# Start Flask keepalive server
keep_alive()

# Run bot
client.run(TOKEN)
