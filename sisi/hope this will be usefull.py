#!/usr/bin/env python3ex
import os
import time
from sys import platform
tasks =[]
###Functions###
def greeter():
    os.system('clear')
    print("\t**********************************************************")
    print("\t***                                                    ***")
    print("\t***                 Good Morning Babyy!                ***")
    print("\t***                                                    ***")
    print("\t**********************************************************")

def menu():
    print("\n Please pick an option from the list below: ")
    print("[1] Task Manager")
    print("[2] Music")
    print("[3] Check the folder")
    print("[q] Quit")
    return input("What would be your choice sweetheart? <3 \n")

def daily_tasks():
    n = int(input("How much tasks would you like to save for now baby? "))
    for i in range(n):
        task = input("What would you like to save for to do task today,honey? ")
        tasks.append(task)

    os.system('clear')
    print("\n")
    print("\n")
    print("\n")
    print("\t Things you gotta do today: ",tasks)
    print("\n")
    print("\n")
    print("\n")

def platforms():
    if platform == 'linux'or platform == 'linux2':
        print(platform)

    elif platform == 'win32':
        print(platform)

    elif platform == 'darwin':
        print(platform)


def music():
    newpath = r'C:\Program Files\sisi'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def music_linux():
    newpath=r'/home/user/sisi'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


####Main Program####
greeter()
choice = ''
while choice != 'q':
    choice = menu()
    if choice == '1':
        daily_tasks()
    elif choice == 'q':
        print("See you soon baby!")
    elif choice == '3':
       if platform == 'win32':
            music()
       elif platform == 'linux':
            music_linux()
    else:
        print("\n Sorry I'm still workin on it baby! <3")
