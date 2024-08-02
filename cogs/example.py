from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
	self.log = bot.log


def setup(bot):
    bot.add_cog(Example(bot))
