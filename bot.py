from email import message

import discord
import bot_logic
from bot_logic import gen_pass 
from bot_logic import gen_emodji 
from bot_logic import flip_coin
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$check'):
        await message.channel.send("test")
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$emoji'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$pass'):
        await message.channel.send("Password: " + gen_pass(10))
        
client.run("")
