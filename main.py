import discord
from discord.ext import commands


TOKEN = "bot_token" 
USER_IDS = [123456789012345678, 987654321098765432]  
EMOJI = "<:cool:123456789012345678>" 


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[Bot] Logged in as {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

   
    if message.author.id in USER_IDS:
        try:
          
            await message.add_reaction(EMOJI)
        except Exception as e:
            print(f"Failed to react to {message.author}: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
