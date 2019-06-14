#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#!Python3 Learning Tutorial

# print("Hello World")

# _VariableName;

# use Object to call, cannot be " from xxx import *"

# __VariableName(private)

# __init__() Constructor


# print("Hy"); print("是猪");

# In PEP8, ";" is not recommended to part statement in a single row;

# if True:
#     print("HYYYY")
#     print("TRUE")
# else:
#     print("FALSE")
#   print("H")

#   Python use strict indentation to part code block
#   File "/home/hachiko/PycharmProjects/PythonTutorial/Demo.py", line 23
#     print("H")
#              ^
# IndentationError: unindent does not match any outer indentation level

# total = 1 + \
#         2 + \
#         3
#
# print(total)
#
# _first = 'This is first'
# _second = "This is second"
# _third = """ This is third"""
#
# print(_first, _second, _third)

# Use "\" to part line,  string declaration

# test = input("\n")
# print(test)

# in python3.x, use input to get user's input

# counter = 100
# ctime = 100.0
# name = "hyyyyy"
#
# print(isinstance(counter, int))
# print(isinstance(ctime, float))
# print(type(name))

# Use isinstance(v,t) to determine the type of variable

# 6 standard data types
# 1. Number
# 2. String我
# 3. List
# 4. Tuple
# 5. Dictionary
# 6. Set

# 4 number types
#
# 1.int
# 2.bool
# 3.float
# 4.complex

# a, b, c, d = 1, 1.0, True, 4+3j
#
# print(type(a), type(b), type(c), type(d))

# str = 'abcdefghij'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + "TEST")  # 连接字符串

# letter = ['1', '1', '2', '2', '3', '3', '4','4']
#
# print(letter[0:7:4])

# The third parameter is step
import math


# def quadratic(a, b, c):
#     if not (isinstance(a, (int, float, bool)) and \
#             isinstance(b, (int, float, bool)) and \
#             isinstance(c, (int, float, bool))):
#         raise TypeError("Bad input")
#     _c = b * b - 4 * a * c
#     print("c : %d" % _c)
#     if _c < 0:
#         return
#     else:
#         return (-b+math.sqrt(_c))/(2 * a), (-b-math.sqrt(_c))/(2 * a)
#
#
# print(quadratic(1, 3, -4))


def _parameter(name, sex, country = 'China', *telephone, **habits):

    print("Name:%s" % name)
    print("Sex:%s" % sex)
    print("Country:%s" % country)
    print("telephone: {0} ".format(telephone))
    print("Habits: {0} ".format(habits))


_h = {'interst': 'fishing'}

_parameter('John', 'Male', 'US', 181, 125,'lkajslfdkj', sexyadd= 'female', inte ='fishing')

