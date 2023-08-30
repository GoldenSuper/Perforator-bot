import nextcord
from nextcord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1146477324695519322)
        await channel.send(f'Welcome, {member.mention}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1146477324695519322)
        await channel.send(f'Goodbye, {member.mention}')

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('test')
