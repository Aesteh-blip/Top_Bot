import random
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def flip_coin():
    coins = ["Heads", "Tails"]
    return random.choice(coins)


def roll_die(sides):
    if sides <= 0:
        sides = 6
    return random.randint(1, sides)


def pick_random(items):
    return random.choice(items)

def get_anime_image_url(keyword):
    url = f'https://api.jikan.moe/v4/anime?q={keyword}&limit=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data'][0]['images']['jpg']['image_url']
    return None

def get_duck_image():
    response = requests.get('https://random-d.uk/api/v2/random')
    if response.status_code == 200:
        data = response.json()
        return data['url']
    else:
        return None
    
def get_cat_image():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        return None

def get_waste_type(waste):
    waste.lower().strip()
    non_recyclable = ['plastic bag', 'styrofoam', 'ceramics', 'diapers', 'cigarette butts', 'plastic utensils', 'plastic straws']
    recyclable = ['paper', 'cardboard', 'glass', 'metal', 'plastic bottle', 'aluminum can', 'plastic container']
    compostable = ['food scraps', 'yard waste', 'paper towels', 'coffee grounds', 'egg shells', 'tea bags']

    if waste in non_recyclable:
        return 'Non-recyclable'
    elif waste in recyclable:
        return 'Recyclable'
    elif waste in compostable:
        return 'Compostable'
    else:
        return 'Unknown waste type'
    
def reduce_waste_tips(how_many):
    tips = [
        "Cobalah untuk menghindari penggunaan barang sekali pakai, seperti gelas dan botol plastik.",
        "Pindah ke e-reader untuk mengurangi konsumsi kertas.",
        "Pilih produk bahan makanan dan makanan ringan dengan kemasan sesedikit mungkin, beli makanan berdasarkan beratnya (tanpa kemasan), dan cobalah beralih ke tas yang dapat digunakan kembali."
        "Cobalah untuk mendaur ulang. Sediakan tempat sampah khusus untuk produk yang dapat didaur ulang dan pindahkan ke tempat daur ulang setelah penuh."
    ]
    return random.choices(tips, k=how_many)
