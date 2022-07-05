#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
=====================================
BMI Calculator
=====================================
Usage: %prog
:Author: MerhuBerahu, https://github.com/MerhuBerahu
:Date: 03/07/2022
"""


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)