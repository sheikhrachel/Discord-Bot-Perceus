import discord
from discord.ext import commands


class System(commands.Cog):
    def __init__(self, perceus):
        self.perceus = perceus

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as: ')
        print(self.perceus.user.name)
        print(self.perceus.user.id)
        print('--------------')

    @commands.command()
    async def load(self, ctx, cogname):
        self.perceus.load_extension(f'cogs.{cogname}')
        await ctx.send(f'Loaded {cogname}')

    @commands.command()
    async def unload(self, ctx, cogname):
        if cogname in ['System']:
            return await ctx.send('You cannot unload system')

        self.perceus.unload_extension(f'cogs.{cogname}')
        await ctx.send(f'Unloaded {cogname}')

    @commands.command()
    async def reload(self, ctx, cogname):
        self.perceus.reload_extension(f'cogs.{cogname}')
        await ctx.send(f'Reloaded {cogname}')
        

def setup(perceus):
    perceus.add_cog(System(perceus))