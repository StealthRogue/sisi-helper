#!/usr/bin/env python3ex
import os
import time
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
    return input("What would be your choice sweetheart? <3")

def daily_tasks():
    n = int(input("How much tasks would you like to save for now baby? "))
    for i in range(n):
        task = input("What would you like to save for to do task today,honey? ")
        tasks.append(task)
    print(tasks)



####Main Program####
greeter()
choice = ''
while choice != 'q':
    choice = menu()
    if choice == '1':
        daily_tasks()
    elif choice == 'q':
        print("See you soon baby!")
    else:
        print("\n Sorry I'm still workin on it baby! <3")
