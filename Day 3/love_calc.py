#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
=====================================
Love Calculator
=====================================
Usage: %prog
:Author: MerhuBerahu, https://github.com/MerhuBerahu
:Date: 05/07/2022
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


true = ["t","r","u","e"]
love = ["l","o","v","e"]

true_count = 0
love_count = 0

for i in name1:           #for each letter in name
    if i in true:         #if letter in list
        true_count += 1   #increment count
    if i in love:
        love_count += 1

for i in name2:
    if i in true:
        true_count += 1
    if i in love:
        love_count += 1

    

total_count = str(true_count) + str(love_count)
total_as_int = int(total_count)
message = ""

if total_as_int <10 or total_as_int >90:
    message = ", you go together like coke and mentos."
elif total_as_int>= 40 and total_as_int <= 50:
    message = ", you are alright together."
else:
    message = "."

print(f"Your score is {total_count}{message}")

"""Test Case
name1 = "Kanye West"
name2 = "Kim Kardashian"
Your score is 42, you are alright together.

name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Your score is 73.
"""