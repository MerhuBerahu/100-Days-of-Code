#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
=====================================
Rock, Paper, Scissors Game
=====================================
Usage: %prog
:Author: MerhuBerahu, https://github.com/MerhuBerahu
:Date: 06/07/2022
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors")
print("Rock --> Scissors")
print("Paper --> Rock")
print("Scissors --> Paper")
legal_moves = ["rock","Rock","r","R","paper","Paper","p","P","scissors","Scissors","s", "S"]

move = input("Which do you choose, Rock, Paper or Scissors?")

if move in legal_moves:
    print