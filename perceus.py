import discord
from discord.ext import commands

perceus = commands.bot(command_prefix = '$', description = 'A demo Discord Chat Bot built using Discord.py')
token = ''

@perceus.event
async def on_ready():
    print('Logged in as: ')
    print(perceus.user.name)
    print(perceus.user.id)
    print('--------------')

@bot.command()
async def t1(ctx):
    await ctx.send("r:runner: RUN IT DOWN BOYS")

@bot.command()
async def qt(ctx):
    await ctx.send("doot diddly donger cuckarino")

@bot.command()
async def nb3(ctx):
    await ctx.send("You kappachino")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Perceus", description="Just a bot, slithering along", color=0x00ffff)
    # give info about you here
    embed.add_field(name="Author", value="Isaac Sheikh")

    await ctx.send(embed=embed)

perceus.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$t1", value="Alpha", inline=False)
    embed.add_field(name="$qt", value="Qtpie", inline=False)
    embed.add_field(name="$nb3", value="NightBlue", inline=False)
    embed.add_field(name="$info", value="Info about the bot", inline=False)
    embed.add_field(name="$help", value="This message", inline=False)

    await ctx.send(embed=embed)

perceus.run(token)