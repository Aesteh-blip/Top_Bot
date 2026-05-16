import discord
import random
import asyncio
from discord.ext import commands
from settings import setting

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description="Generates a random password")
async def gen_pass(ctx, pass_length: int):
    from bot_logic import gen_pass
    password = gen_pass(pass_length)
    await ctx.send(f'Your generated password is: {password}')

@bot.command(description="Flips a coin")
async def flip_coin(ctx):
    from bot_logic import flip_coin
    result = flip_coin()
    await ctx.send(f'The coin landed on: {result}')

@bot.command(description="Rolls a die with a specified number of sides")
async def roll_die(ctx, sides: int):
    from bot_logic import roll_die
    result = roll_die(sides)
    await ctx.send(f'You rolled a {result} on a {sides}-sided die.')

@bot.command(description="Picks a random item from a list")
async def pick_random(ctx, *items):
    from bot_logic import pick_random
    if not items:
        await ctx.send('Please provide a list of items to choose from.')
        return
    result = pick_random(items)
    await ctx.send(f'I picked: {result}')

@bot.command(name='guess')
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit() and m.channel == ctx.channel

    answer = random.randint(1, 10)

    try:
        guess_msg = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {answer}.')

    if int(guess_msg.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')

bot.run(setting["TOKEN"])
