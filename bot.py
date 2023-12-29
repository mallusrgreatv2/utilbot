from colorama import Fore
from urllib import parse
import discord
from discord import app_commands
import config
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), owner_id=1121747852918521937)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{Fore.GREEN}[ONLINE] {Fore.CYAN}{bot.user.name}#{bot.user.discriminator} {Fore.GREEN}is online.")
    bot.get_guild(1123240630844395671).get_member(1145729748803272815).add_roles(1123250542794244157)

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"`{error.param.name}` is missing.", ephemeral=True)
        return

@bot.hybrid_command(name="ping")
@commands.is_owner()
async def pingCmd(ctx: commands.Context):
    """Check the bot's ping"""
    await ctx.send(f"{round(bot.latency)}ms ping.")

@bot.hybrid_command(name="google")
@commands.is_owner()
@app_commands.describe(
    text = "The text to google"
)
async def googleCmd(ctx: commands.Context, *, text: str = commands.parameter(description="The text to google")):
    """Generate a google link searching for the given text"""
    await ctx.send(f"https://google.com/search?q={parse.quote((''.join(text))).replace('%20', '+')}")

@bot.hybrid_command(name="say")
@commands.is_owner()
@app_commands.describe(
    text = "The text to say"
)
async def sayCmd(ctx: commands.Context, *, text: str = commands.parameter(description="The text to say")):
    """Say something"""
    if ctx.interaction:
        await ctx.reply(ephemeral=True, content="Ok")
        await ctx.channel.send(content=''.join(text))
    else:
        await ctx.message.delete()
        await ctx.send(content=''.join(text))

bot.run(config.TOKEN)