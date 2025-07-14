import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keepalive import keep_alive

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Change from Client to Bot to support commands
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Tsnip is online as {bot.user}")
    try:
        # Sync slash commands with Discord
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "DHR2207UVI":
        await message.channel.send("Hey! I'm online 🚀")

    # Process commands (important for slash commands to work)
    await bot.process_commands(message)


# Slash command: /test
@bot.tree.command(name="test", description="Check if the bot is running")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("Bot is running! 🚀")


# You can add more slash commands here
@bot.tree.command(name="ping", description="Check bot's latency")
async def ping_command(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! Latency: {latency}ms")


@bot.tree.command(name="info", description="Get bot information")
async def info_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Bot Information",
        description="Tsnip Bot is running smoothly!",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Status", value="Online ✅", inline=True)
    embed.add_field(name="Server", value="EC2 Instance", inline=True)
    await interaction.response.send_message(embed=embed)


# Start Flask keepalive server
keep_alive()

# Run bot
bot.run(TOKEN)
