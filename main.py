import os

import discord
from discord.ext import commands

from common.logger_config import configure_logger
from common.utils import load_config

config = load_config()


class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=config["bot"]["prefix"],
            intents=discord.Intents.all(),
        )
        self.log = configure_logger()
        self.config = config

        cogs_dir = "cogs"

        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py"):
                cog = f"{cogs_dir}.{filename[:-3]}"
                try:
                    self.load_extension(cog)
                    self.log.info(f"Loaded cog {cog}")
                except Exception as e:
                    self.log.error(f"Failed to load cog {cog}\n{e}")

        self.load_extension("jishaku")
        self.remove_command("help")

    async def on_ready(self):
        self.log.info(f"Logged in as {self.user} (ID: {self.user.id})")
        self.log.info(f"Connected to {len(self.guilds)} guilds")


bot = Bot()
bot.run(config["bot"]["token"])
