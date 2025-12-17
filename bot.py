import json
import os
import aiohttp
import discord
from discord.ext import commands
from utils import find_nitro, is_giveaway

BOT_TOKEN = os.getenv("BOT_TOKEN")

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def send_webhook(title, description):
    if not config["webhook_url"]:
        return
    payload = {"embeds": [{"title": title, "description": description, "color": 0x5865F2}]}
    async with aiohttp.ClientSession() as session:
        await session.post(config["webhook_url"], json=payload)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content

    code = find_nitro(content)
    if code and config["log_nitro"]:
        await send_webhook("Nitro Detected", f"Code: `{code}`")

    if is_giveaway(content) and config["log_giveaways"]:
        await send_webhook("Giveaway Detected", content[:300])

    await bot.process_commands(message)

bot.run(BOT_TOKEN)
