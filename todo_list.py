# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:38:36 2025

@author: Malena
"""

task_list = []
command_list = ["add", "view", "complete", "remove", "done"]

while True:
    print("========================================================")
    user_input = input("""Which of the following tasks do you want to do? 
Type add, view, complete, remove, done\n""").lower()
    # checks if input is valid command
    if user_input not in command_list:
        print("Unknown command found, please use one of the following: " + str(command_list))
   
    if user_input == "add":
        add_task = input("What task would you like to add?\n")
        task_list.append("[ ] " + add_task)     # adds task to list
        print("Task successfully added!")
  
    if user_input == "view":    
        # checks if list is empty
        if not task_list:
            print("To do list is empty\n")
        for i, task in enumerate(task_list):    # gives index along with actual item
            print(str(i) + ":" + task)
            
    if user_input == "complete":
        completed_task = input("Which task would you like to mark as completed? (by index)\n")
        
        # checks if input is valid
        try:
            current_task = task_list[int(completed_task)]
        except:
            print("Please give a valid index")
            continue
        
        # removes task from list and replaces empty checkbox with marked checkbox
        task_list[int(completed_task)] = "[X]" + task_list[int(completed_task)][3:] # takes string after first 3 characters
        print("Task succesfully marked as completed!")
        
    if user_input == "remove":
        # checks if list is empty
        if not task_list:
            print("To do list is empty\n")
            continue
        remove_task = input("Which task would you like to remove? (by index)\n")
        # checks for valid input
        try:
           current_task = task_list[int(remove_task)]
        except:
           print("Please give a valid index")
           continue
        
        # deletes list item by index
        del task_list[int(remove_task)]
        print("Task succesfully removed!")
    
    # breaks while loop if user types done
    if user_input == "done":
        break
        
        