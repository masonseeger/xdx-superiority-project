# give params in cosole to role a die
# EX python xdx.py 3d10 => rolls 3 ten-sided die

import sys
from random import randint as randy

def roll_baby_roll(left, size):
    if left < 1:
        return 0
    elif left == 1:
        return randy(1, size)
    else:
        return roll_baby_roll(left-1, size) + randy(1, size)

def main():
    dice = sys.argv[1].split('d')
    print(roll_baby_roll(int(dice[0]), int(dice[1])))

if __name__ == "__main__":
    main()
