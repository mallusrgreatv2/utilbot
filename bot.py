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

@bot.hybrid_command(name="ping")
async def pingCmd(ctx: commands.Context):
    """Check the bot's ping"""
    await ctx.send(f"{round(bot.latency)}ms ping.")

@bot.hybrid_command(name="google")
@app_commands.describe(
    text = "The text to google"
)
async def googleCmd(ctx: commands.Context, *, text: str):
    """Generate a google link searching for the given text"""
    await ctx.send(f"https://google.com/search?q={parse.quote((''.join(text))).replace('%20', '+')}")

bot.run(config.TOKEN)