import os
import random
import asyncio
import discord
import requests
from discord.ext import commands
from settings import setting
from bot_logic import gen_pass, flip_coin, roll_die, pick_random, get_anime_image_url, get_duck_image, get_cat_image

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# --- Commands ---

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command(description="Generates a random password")
async def password(ctx, pass_length: int):
    result = gen_pass(pass_length)
    await ctx.send(f'Your generated password is: {result}')

@bot.command(description="Flips a coin")
async def flip(ctx):
    result = flip_coin()
    await ctx.send(f'The coin landed on: {result}')

@bot.command(description="Rolls a die with a specified number of sides")
async def roll(ctx, sides: int):
    result = roll_die(sides)
    await ctx.send(f'You rolled a {result} on a {sides}-sided die.')

@bot.command(description="Picks a random item from a list")
async def pick(ctx, *items):
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

@bot.command(name='meme')
async def mem(ctx):
    all_local_images = os.listdir('images')
    img_name = random.choice(all_local_images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command(name='duck')
async def duck(ctx):
    duck_url = get_duck_image()
    if duck_url:
        await ctx.send(duck_url)

@bot.command(name='anime')
async def anime(ctx, *, keyword: str):
    anime_url = get_anime_image_url(keyword)
    if anime_url:
        await ctx.send(anime_url)
    else:
        await ctx.send('No anime found with that keyword.')
                       
@bot.command(name='cat')
async def cat(ctx):
    cat_url = get_cat_image()
    if cat_url:             
        await ctx.send(cat_url)
    else:        await ctx.send('Could not fetch a cat image at the moment.')
                       
bot.run(setting["TOKEN"])
