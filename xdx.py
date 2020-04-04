# give params in cosole to role a die
# EX python xdx.py 3d10 => rolls 3 ten-sided die

import sys
from random import randint as randy

def roll_baby_roll(left, size):
    for i in range(left):
      yield i, randy(1,size)

def main():
    dice = sys.argv[1].split('d')
    total = 0
    for massons_special_var in roll_baby_roll(int(dice[0]), int(dice[1])):
        print("Role %d: %d" % massons_special_var)
        total += massons_special_var[1]
    print("Sum: ", total)

if __name__ == "__main__":
    main()
