#!/usr/bin/python
#rev 0.1
#Last modified 11/9/2019
#writen by Kevin Burkeland
#imports random
import random
#define four sided dice
def roll_d4(number_of_dice):
	rolls = []
	for _ in range(number_of_dice):
		roll = random.randint(1,4)
		rolls.append(roll)
	return rolls
#define six sided dice
def roll_d6(number_of_dice):
	rolls = []
	for _ in range(number_of_dice):
		roll = random.randint(1,6)
		rolls.append(roll)
	return rolls
#define eight sided dice
def roll_d8(number_of_dice):
	rolls = []
	for _ in range(number_of_dice):
		roll = random.randint(1,8)
		rolls.append(roll)
	return rolls
#define ten sided dice
def roll_d10(number_of_dice):
	rolls = []
	for _ in range(number_of_dice):
		roll = random.randint(1,10)
		rolls.append(roll)
	return rolls
#define 12 sided dice
def roll_d12(number_of_dice):
	rolls = []
	for _ in range(number_of_dice):
		roll = random.randint(1,12)
		rolls.append(roll)
	return rolls
#define 20 sided dice
def roll_d20(number_of_dice):
	rolls = []
	for _ in range(number_of_dice):
		roll = random.randint(1,20)
		rolls.append(roll)
	return rolls