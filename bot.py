from colorama import Fore
from urllib import parse
import discord
from discord import app_commands
import config
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{Fore.GREEN}[ONLINE] {Fore.CYAN}{bot.user.name}#{bot.user.discriminator} {Fore.GREEN}is online.")

@bot.hybrid_command(name="ping", description="Check the bot's ping")
async def pingCmd(ctx: commands.Context):
    await ctx.send(f"{round(bot.latency)}ms ping.")

@bot.hybrid_command(name="google", description="Google")
@app_commands.describe(
    text = "The text to google"
)
async def googleCmd(ctx: commands.Context, text: str):
    await ctx.send(f"https://google.com/search?q={parse.urlencode(text.replace(' ', '+'))}")

bot.run(config.TOKEN)