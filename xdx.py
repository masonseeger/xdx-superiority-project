# give params in cosole to role a die
# EX python xdx.py 3d10 => rolls 3 ten-sided die

import sys
from random import randint as randy

def roll_baby_roll(left, size):
	for i in range(left):
		yield randy(1,size)


def main():
    dice = sys.argv[1].split('d')
    tot = 0
    for dice in roll_baby_roll(int(dice[0]), int(dice[1])):
        print(dice)
        tot += dice
    print("Sum: ", tot)

if __name__ == "__main__":
    main()
