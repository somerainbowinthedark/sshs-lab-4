import random
from flask import Flask, Blueprint

damage = Blueprint('damage', __name__)
# creates the starting webpage
@damage.route('/start', methods=['GET', 'POST'])
def start():
    return 'HI!'
# creates the page that tells you to roll the dice
@damage.route('/roll', methods=['GET'])
def roll():
    return 'Roll the dice!'
# sets up the random function for when we roll the dice
def roll_dice():
    return random.randint(1, 20)
# uses the random function to get the number we "rolled" and tells us what maount of damage we give
@damage.route('/damage', methods=['GET'])
def roll_for_damage():
    roll_result = roll_dice()
    if roll_result == 20:
        return 'Critical Hit!!'
    elif roll_result == 1:
        return 'Critical Miss!' 
    else:
        return 'You swing for {roll_result} damage!'

# "rolls" two random number and then returns the lesser number
@damage.route('/disadvantage', methods=['GET', 'POST'])
def roll_for_disadvantage():
    roll1 = roll_dice()
    roll2 = roll_dice()
    return 'You dealt {min(roll1, roll2)} damage'

# "rolls" two random number and then returns the greater number
@damage.route('/advantage', methods=['GET', 'POST'])
def roll_for_advantage():
    roll1 = roll_dice()
    roll2 = roll_dice()
    return 'You dealt {max(roll1, roll2)} damage'
