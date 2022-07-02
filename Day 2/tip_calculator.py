#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
=====================================
Tip Generator
=====================================
Usage: %prog
:Author: MerhuBerahu, https://github.com/MerhuBerahu
:Date: 02/07/2022
"""


print("Welcome to the Tip Calculator")
total = int(input("What was the total bill?"))
party = int(input("How many to split the bill?"))
percentage = int(input("What percentage of tip would you like to pay, 10, 12 or 15?"))

#calc
tip_to_pay = str((total /100 * percentage) / party)

print("Tip per person needs to pay is "+ tip_to_pay)


