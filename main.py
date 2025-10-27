import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# ====== CONFIG ======
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN") or "bot_token" # it is adviced to use environmental variables (.env) to store your token for safety

USER_IDS = {123456789012345678, 987654321098765432}  # IDs of users to react to
EMOJI = "<:cool:123456789012345678>"  # Custom emoji
# =====================

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[Bot] Logged in as {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    # Check if the author is one of the target users
    if message.author.id in USER_IDS:
        try:
            # Try to add the emoji reaction
            await message.add_reaction(EMOJI)
        except Exception as e:
            print(f"Failed to react to {message.author}: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
