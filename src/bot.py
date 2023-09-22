import os
import random

import discord
from discord import app_commands

import src


def run_discord_bot():
  # # For use outside of replit
  # load_dotenv()
  # TOKEN = os.getenv("DISCORD_TOKEN")
  # GUILD_ID = os.getenv('GUILD_ID')
  # WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

  # For use within replit
  TOKEN = os.environ['DISCORD_TOKEN']
  GUILD_ID = os.environ['GUILD_ID']
  WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)
  tree = app_commands.CommandTree(client)

  @client.event
  async def on_ready():
    guild_count = 0

    print(f'{client.user} is now running!')

    for guild in client.guilds:
      await tree.sync(guild=discord.Object(id=guild.id))
      print(f'{guild.name}(id: {guild.id})')
      guild_count += 1
    print(f'{client.user} is in {guild_count} guilds.')

  @tree.command(name="hello",
                description="Just being polite",
                guild=None)
  async def first_command(interaction):
    await interaction.response.send_message("Croak.")
    pass

  @tree.command(name="roll",
                description="Roll some dice",
                guild=discord.Object(id=GUILD_ID))
  @app_commands.describe(dice="Number of dice to roll.",
                         sides="Type of dice to roll.")
  async def roll_dice(ctx, dice: int, sides: int):
    if dice <= 0 or sides <= 0:
      await ctx.response.send_message(
          "Both the number of dice and dice size must be greater than zero.",
          ephemeral=True)
      return
    if dice > 100 or sides > 100:
      await ctx.response.send_message(
          "Both the number of dice and dice size must be 100 or less.",
          ephemeral=True)
      return
    rolls = [random.randint(1, sides) for _ in range(dice)]
    total = sum(rolls)
    await ctx.response.send_message(
        f"Rolled {dice}d{sides}: {', '.join(map(str, rolls))}. Total: {total}")
    pass

  @tree.command(name="weather",
                description="What's the weather?",
                guild=discord.Object(id=GUILD_ID))
  @app_commands.describe(city="What city would you like the weather for?")
  async def weather(ctx, city: str):
    text, is_ephemeral = src.get_weather(city, WEATHER_API_KEY)
    if is_ephemeral:
      await ctx.response.send_message(text, ephemeral=True)
    else:
      await ctx.response.send_message(text)
    pass

  @tree.command(name="frogfact",
                description="Give me a frog fact",
                guild=discord.Object(id=GUILD_ID))
  async def frogfact(ctx):
    fact = src.get_frogfact('resources/responses.txt')
    await ctx.response.send_message(fact)
    pass

  @tree.command(name="choose",
                description="Chose between 2 options",
                guild=discord.Object(id=GUILD_ID))
  async def choose(ctx, option1: str, option2: str):
    options = [option1, option2]
    choice = random.choices(options, k=1)
    await ctx.response.send_message(
        f"Between {option1} and {option2}, I choose: {choice[0]}")
    pass

  client.run(TOKEN)
