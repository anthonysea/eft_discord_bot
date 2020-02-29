import os

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.group()
def eft(ctx):
    if ctx.invoked_subcommands is None:
        await ctx.send('No subcommand passed.')


@eft.command(name='map')
def _map(ctx, map_name: str) -> None:
    '''Fetches the map image for the given map'''


@eft.command(name='ammo')
def _ammo(ctx, ammo_type: str) -> None:
    '''Responds with the ammo chart for the given ammo type'''

bot.run(TOKEN)