import discord
import requests
import os
from discord.ext import commands
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def get_gold_price():
    url = "https://api.metals.live/v1/spot"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        for item in data:
            if "gold" in item:
                return item["gold"]
    except:
        return None

@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập: {bot.user}")

@bot.command()
async def gold(ctx):
    price = get_gold_price()
    if price:
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        await ctx.send(f"📈 Giá vàng hiện tại: **{price} USD/oz**\n🕒 Thời gian: {now}")
    else:
        await ctx.send("❌ Không lấy được giá vàng. Vui lòng thử lại sau.")

bot.run(TOKEN)
