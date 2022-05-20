from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "!"
OWNER_ID = [PUT YOUR DISCORD ID HERE]

class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.guild = None # Remove later if going to multiple servers
    self.scheduler = AsyncIOScheduler()
    
    super().__init__(command_prefix=PREFIX, owner_ids=OWNER_ID)
    
  def run(self, version):
    self.VERSION = version

    with open ("./lib/bot/token.0", "r", encoding="utf-8") as tf:
      self.TOKEN = tf.read()

      print("Running Bot...")
      super().run(self.TOKEN, reconnect=True)

  async def on_connect(self):
    print("Bot Connected")

  async def on_disconnect(self):
    print("Bot Disconnected")

  async def on_ready(self):
    if not self.ready:
      self.ready = True
      self.guild = self.get_guild(PUT SERVER ID HERE)
      print("Bot Ready")

    else:
      print("Bot Reconnected")

  async def on_mesage(self, message):
    pass

bot = Bot()