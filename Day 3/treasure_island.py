#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
=====================================
Treasure Island Adventure Game
=====================================
Usage: %prog
:Author: MerhuBerahu, https://github.com/MerhuBerahu
:Date: 05/07/2022
"""

import os
from time import sleep

#welcome

print('''
                        
    ▀▀█▀▀ █▀▀█ █▀▀ █▀▀█ █▀▀ █░░█ █▀▀█ █▀▀ 　 ▀█▀ █▀▀ █░░ █▀▀█ █▀▀▄ █▀▀▄ 
    ░▒█░░ █▄▄▀ █▀▀ █▄▄█ ▀▀█ █░░█ █▄▄▀ █▀▀ 　 ▒█░ ▀▀█ █░░ █▄▄█ █░░█ █░░█ 
    ░▒█░░ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀ ░▀▀▀ ▀░▀▀ ▀▀▀ 　 ▄█▄ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀░
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Waiting for 4 seconds to clear the screen
sleep(4)
# Clearing the Screen
os.system('cls')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You stand with a lagoon to your left and a beach stretching out to the right.")
print("Do you want to go left to the lagoon or right to walk along the beach?")
direction1 = input("Type Left or Right :>")

if direction1 in ["left","Left","L"]:
    direction2 = input("You walk over to the lagoon, it's cool blue green water seemingly calm. Do you want to swim across straight away or wait a while?")
    if direction2 in ["swim", "Swim"]:
        print("You start a leisurely swim across and as you reach the middle of the lagoon you feel a painful tug in your leg. Something has bitten you and drags you under, as you sink lower you see a giant fish powerfully dragging you to the cold darkness below. You fight and flail but to no avail.")
        print("you Die")
        print("Game Over!")
    elif direction2 in ["wait", "Wait"]:
        print("You sit and wait a while, in the stillness you see a giant fish attack another, it likely would have attacked you had you not waited")
        print("After a while fromthe corner of you eye you notice something, a little ways up the beach stands 3 doors")
    
elif direction1 in ["right", "Right","R"]:
    print("You start walking across the beach, you dont make it very far when you feel the ground give under you. You fall into a pit, sharpened branches piercing through your body.")
    print("you Die")
    print("Game Over!")

