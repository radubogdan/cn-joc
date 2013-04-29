#!/usr/bin/python

"""
Desciption: No GUI version of [C] [N]
Name: main.py
Purpose: Having fun with numbers
Author: Croitoru Radu-Bogdan
""" 

import random

# Event handlers
def random_no():
    # Test if generated number is correct
    global li_b
    rand = random.randint(1000,9999)    
    li_b = [int(i) for i in str(rand)]
    ok = 0
    while ok == 0:
        my_l = list(set(li_b))
        if li_b != my_l:
            rand = random.randint(1000,9999)
            li_b = [int(i) for i in str(rand)]
        else:
            ok = 1
    return li_b        

def init():
    # Initialize game
    global li, number
    print ("[C]entrate - [N]ecentrate!")
    print ("Calculatorul s-a gandit la un numar")
    random_no()

def reset():
    # Reset game button
    print ("")
    print ("Jocul s-a resetat")
    init()

def cn(ls1, ls2):
    # Test for [C], [N]
    global c, n
    n = len([i for i in ls1 if i in ls2])
    c = 0
    for i in range(len(ls1)):
        if ls1[i] == ls2[i]:
            c += 1
            n -= 1
    return str(c) + "[C]" + " " + str(n) + "[N]"
    
def get_input(guess):
    global li_a
    li_a = [int(i) for i in str(guess)]
    ok = 0
    # Test if input is correct    
    while ok == 0:
        my_l = list(set(li_a))
        if li_a != my_l:
            print ("")
            print (int(''.join([ "%d" %x for x in li_a])), "nu este bun!")
            print ("Introduceti alt numar")
            li_a = [int(i) for i in str(guess)]            
            break
        else:
            ok = 1
    
    print (int(''.join([ "%d" %x for x in li_a]))," - ", cn(li_a, li_b))
    if c == 4:
        print ("Felicitari, ai ghicit numarul")
        print ("")
        print ("Joc nou.")
        init()