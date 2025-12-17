import os
import aiohttp
import discord
from discord.ext import commands
from utils import find_nitro, is_giveaway

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_GUILD_ID = int(os.getenv("TARGET_GUILD_ID"))
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def send_channel_message(title, description):
    guild = bot.get_guild(TARGET_GUILD_ID)
    if not guild:
        return

    channel = guild.get_channel(TARGET_CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title=title,
        description=description,
        color=0x5865F2
    )

    await channel.send(embed=embed)

@bot.event
async def on_ready():
    print(f"[READY] Logged in as {bot.user}")
    print(f"[INFO] Target Guild: {TARGET_GUILD_ID}")
    print(f"[INFO] Target Channel: {TARGET_CHANNEL_ID}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content

    # Nitro detection
    code = find_nitro(content)
    if code:
        await send_channel_message(
            "🎁 Nitro Detected",
            f"Code: `{code}`\n"
            f"From: {message.author}\n"
            f"Channel: {message.channel.mention}"
        )

    # Giveaway detection
    if is_giveaway(content):
        await send_channel_message(
            "🎉 Giveaway Detected",
            f"{content[:300]}\n\n"
            f"Channel: {message.channel.mention}"
        )

    await bot.process_commands(message)

bot.run(BOT_TOKEN)
