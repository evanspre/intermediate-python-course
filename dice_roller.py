import random
def main():

  dice_rolls = 3
  dice_sum = 0

  for i in range(0, dice_rolls):

    roll = random.randint(1, 6)

    if roll == 1:
      print(f'You rolled a {roll}! Critical fail!')
    elif roll == 6:
      print(f'Whoa, a {roll}')
    else:
      print(f'You rolled a {roll}')

    dice_sum = dice_sum + roll
  print(f'Total: {dice_sum}')

if __name__== "__main__":
  main()