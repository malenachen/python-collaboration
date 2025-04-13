#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
TO DO:
    * make code not be able to recommend same game more than once
    * put games into imported file
    * add actual checkout feature
    * create command to leave category and enter different game genre

'''

import random
from Games import games   # import dictionary with all the games

class GamePicker:
    genres = ["ACTION", "ADVENTURE", "RPG", "SHOOTER", "STRATEGY"]
    commands = ["yes", "no", "DONE"]
    
    def __init__(self):
        
        # Create a variable that holds the values above. The user will select values from above and add it to this list
        self.cart = []  
        
        # variable array to store games user says no to so they won't be recommended again
        self.trash = []
        

    def pick_game(self, genre):       
        
        keep_game = False   # boolean to keep current game selected if user types something other than valid commands.
        
        while True:
            
            if not keep_game:   # changes selected game
                if len(games[genre]) == 0:
                    print("\nThere are no more", genre, "games to recommend.")
                    break
                else:
                    selected_game = random.choice(games[genre])
            keep_game = False   # boolean makes game reset next iterative process
            if selected_game not in self.trash:
                print("========================================================")
                print("Game: " + selected_game["title"]) 
                # Show the game title,price, name of developer
                print("Price: " + str(selected_game["price"])) 
                #Has to be a str value because the team was unable to print an int value other than this fashion.
                print("Developer: " + selected_game["developer"])
                    
                # Ask the user if they want to add the game to their cart
                add_to_cart = input("Add this game to your cart? Type yes or no, or exit to change the genre.\n").lower()
                
                
            # checks whether user wants to add item to cart or exit entered genre
            if add_to_cart == "yes":
                # If the user says "yes"
                self.cart.append(selected_game)  
                print("Game added to your cart.") #Print game addded_to cart
                games[genre].remove(selected_game)
                break
            elif add_to_cart == "no":
                self.trash.append(selected_game)
                games[genre].remove(selected_game)
            elif add_to_cart == "exit":
                break
            else:
                print("Please enter a valid command.")
                keep_game = True  # will keep current selected game when looping back to ask yes/no again


    # method to show what is inside the cart
    def show_cart(self, edit = True):
        subtotal = 0
        if self.cart:
            print("\nYour cart has these games!")
            for i, item in enumerate(self.cart, 1): 
                print(str(i) + ". " + item["title"] + " ($" + str(item["price"]) + ")")
                subtotal += item["price"]
                #Having a title and a price or an item means that it has something into the cart. Therefore, add to cart
            
            # is false when show cart is run in the "done" command
            if edit == False:
                return
            
            # allows user to remove items from cart. does not run if edit = false.
            while True:
                re_add = input("\nIf you would like to add a remove a game from your cart, enter the corresponding number. If not, enter exit\n")
                
                if re_add.lower() == "exit":
                    break
                # checks if input is only digits
                elif re_add.isdigit():
                    index = int(re_add) - 1
                    if 0 <= index < len(self.cart): # makes sure that entered number is valid
                        selected_game = self.cart.pop(index)
                        self.trash.append(selected_game)
                        print(selected_game["title"], "has been removed from your cart.")
                        break
                    else:
                        print("Please enter a valid number.")
                else:
                    print("Please enter a valid command.")
        else:
            print("\nThere is nothing inside your cart!")
            
            
    # method to show what is in the trash      
    def show_trash(self):
        if self.trash:
            print("\nYour trash has these games!")
            for i, item in enumerate(self.trash, 1): 
                print(str(i) + ". " + item["title"] + " ($" + str(item["price"]) + ")")
                
            while True:
                re_add = input("\nIf you would like to add a game back to your cart, enter the corresponding number. If not, enter exit\n")
                
                if re_add.lower() == "exit":
                    break
                # checks if input is only digits
                elif re_add.isdigit():
                    index = int(re_add) - 1
                    if 0 <= index < len(self.trash): # makes sure that entered number is valid
                        selected_game = self.trash.pop(index)
                        self.cart.append(selected_game)
                        print(selected_game["title"], "has been moved to your cart.")
                        break
                    else:
                        print("Please enter a valid number.")
                else:
                    print("Please enter a valid command.")
        else:
            print("\nThere is nothing inside your trash!")

#==============================================================================

def main():
    picker = GamePicker()  
    
    while True:
        print("========================================================")
        
        # loops through genres and prints all of them to user
        for i in range(len(GamePicker.genres)):  
            print(str(i+1) + ". " + GamePicker.genres[i]) 
            
        user_input = input("Pick a game genre, and the computer will recommend you a game. Type cart to view cart, trash to view games you said no to, or done when you are finished adding games.\n").upper()

        # check which command/genre user puts
        if user_input == "DONE":
            print("You have finished adding games to your cart.")
            picker.show_cart(edit = False)
            break
        elif user_input == "CART":      #show cart
            picker.show_cart()
        elif user_input == "TRASH":     # show trash
            picker.show_trash()
        elif user_input not in GamePicker.genres:   # Check if genre is in list of genres.
            print("Please enter a valid genre.")    # If not, asks user for a valid genre.
            continue
        else:
            selected_genre = user_input
                # Create a variable that holds the genre choice
            picker.pick_game(selected_genre)


#==============================================================================

if __name__ == "__main__":
    main()
    
#==============================================================================

