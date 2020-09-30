import os
from discord.ext import commands

perceus = commands.Bot(command_prefix = '$', description = 'A demo Discord Chat Bot built using Discord.py')
perceus.remove_command('help')
token = ''

for cog in os.listdir('./cogs'):
    if cog.endswith('.py') and not cog.startswith('_'):
        perceus.load_extension(f'cogs.{cog[:-3]}')
        print(f'Loaded {cog[:-3]}')

    else:
        print(f'unable to load {cog[:-3]}')

perceus.run(token)