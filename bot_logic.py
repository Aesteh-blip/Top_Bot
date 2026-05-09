import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def flip_coin():
    coins = ["Heads", "Tails"]
    return random.choice(coins)

def roll_die(sides):
    sides = [4, 6, 8, 10, 12, 20]
    return random.randint(1, sides)

def pick_random(items):
    items = ["Bagel", "Croissant", "Muffin", "Donut", "Scone"]
    return random.choice(items)
