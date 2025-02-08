# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:38:36 2025

@author: Malena
"""

task_list = []
command_list = ["add", "view", "complete", "remove", "done"]

while True:
    user_input = input("""Which of the following tasks do you want to do? 
Type add, view, complete, remove, done\n""").lower()
    if user_input not in command_list:
        print("Unknown command found, please use one of the following: " + str(command_list))
    if user_input == "add":
        add_task = input("What task would you like to add?\n")
        task_list.append("[ ] " + add_task)
        print("Task successfully added!")
    if user_input == "view":
        for i, task in enumerate(task_list):
            print(str(i) + ":" + task)
    if user_input == "complete":
        completed_task = input("Which task would you like to mark as completed? (by index)\n")
        task_list[int(completed_task)] = "[X]" + task_list[int(completed_task)][3:]
        try:
            int(completed_task)
        except:
            print("Please give a valid index")
            continue
        print("Task succesfully marked as completed!")
    if user_input == "remove":
        remove_task = input("Which task would you like to remove? (by index)\n")
        try:
           int(remove_task)
        except:
           print("Please give a valid index")
           continue
        del task_list[int(remove_task)]
        print("Task succesfully removed!")
    if user_input == "done":
        break
        
        