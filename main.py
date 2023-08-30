import nextcord
from nextcord.ext import commands
import wavelinkcord as wavelink
from config import *


class MyClient(commands.Bot):
    def __init__(self):
        intents = nextcord.Intents.default()
        intents.message_content = True

        super().__init__(intents=intents, command_prefix=PREFIX)

    async def on_ready(self):
        print(f"The bot is logged in as {self.user}")

    async def setup_hook(self):
        node: wavelink.Node = wavelink.Node(uri="localhost:2333", password=LAVALINK_PASSWORD)
        await wavelink.NodePool.connect(client=self, nodes=[node])


bot = MyClient()
bot.run(TOKEN)