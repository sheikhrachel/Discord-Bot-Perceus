import discord
from discord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def t1(self, ctx):
        await ctx.send("r:runner: RUN IT DOWN BOYS")

    @commands.command()
    async def qt(self, ctx):
        await ctx.send("doot diddly donger cuckarino")

    @commands.command()
    async def nb3(self, ctx):
        await ctx.send("You kappachino")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="Perceus", description="Just a bot, slithering along", color=0x00ffff)
        # give info about you here
        embed.add_field(name="Author", value="Isaac Sheikh")

        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

        embed.add_field(name="$t1", value="Alpha", inline=False)
        embed.add_field(name="$qt", value="Qtpie", inline=False)
        embed.add_field(name="$nb3", value="NightBlue", inline=False)
        embed.add_field(name="$info", value="Info about the bot", inline=False)
        embed.add_field(name="$help", value="This message", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Information(bot))
