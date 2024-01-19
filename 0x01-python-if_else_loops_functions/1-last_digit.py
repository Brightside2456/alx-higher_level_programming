#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
final_string = f"Last digit of {number} is {-1 * last_digit if number < 0 else last_digit} "

if number % 10 > 5:
    final_string += "and is greater than 5"
elif number % 10 == 0:
    final_string += "and is 0"
elif (number % 10 < 6) and (number % 10 != 0):
    final_string += "and is less than 6 ad not 0"

print(final_string)
