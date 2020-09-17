import random
def main():

  dice_rolls = 0
  dice_sum = 0

  dice_rolls = int(input('How many dice to roll? '))
  dice_size = int(input('How many faces on the dice? '))

  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    if roll == 1:
      print(f'You rolled a {roll}! Critical fail!')
    elif roll == dice_size:
      print(f'Whoa, a {roll}')
    else:
      print(f'You rolled a {roll}')
    dice_sum = dice_sum + roll
  print(f'Total sum: {dice_sum}')

if __name__== "__main__":
  main()