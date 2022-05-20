import hikari
import lightbulb

#listenBot = hikari.GuildMessageCreateEvent

bot = lightbulb.BotApp( token='OTc0MjY4NzE2MjE5MDAyOTYw.GRcoRV.trIcl7gAXMkdjnUS-h5ikrKRkHcy-UyXlFfOr4', prefix=('!'))

@bot.listen(hikari.StartedEvent) # Bot startup message
async def starting(event):
    print("Bot is online")

@bot.command
@lightbulb.command('commands', 'Says all commands')
@lightbulb.implements(lightbulb.PrefixCommand) # Make into a group for pages
async def command(ctx):
  await ctx.respond('''**My commands are the following:**
!socials youtube - Displays YouTube link
!socials twitch - Displays Twitch link
!socials website - Displays website link
                    
!add - Does two number addition
''')

@bot.command # Socials command group
@lightbulb.command('socials', 'Socials')
@lightbulb.implements(lightbulb.PrefixCommandGroup) # Makes a sub-command group
async def socials(ctx):
    pass

@socials.child # YouTube
@lightbulb.command('youtube', 'Displays YouTube link')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def subCommand(ctx):
    await ctx.respond('https://www.youtube.com/channel/UCG1u7beWxdvQdpqmP2esb7w')

@socials.child
@lightbulb.command('twitch', 'Displays Twitch link')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def twitch(ctx):
    await ctx.respond('https://www.twitch.tv/goldennuggo')

@socials.child # Website
@lightbulb.command('website', 'Displays website link')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def youtube(ctx):
    await ctx.respond('https://www.goldennuggo.com')

@bot.command # Math
@lightbulb.option('num2', 'Select a second number ', type=int) 
@lightbulb.option('num1', 'Select the first number ', type=int)
@lightbulb.command('add', 'Does simple addition')
@lightbulb.implements(lightbulb.PrefixCommand)
async def math(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


bot.run()