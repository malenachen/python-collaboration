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
        
        self.cart = []  
        # Create a variable that holds the values above. THe user will select values from above and add it to this list
        self.trash = []
        # variable array to store games user says no to so they won't be recommended again

    def pick_game(self, genre):       
        
        keep_game = False   # boolean to keep current game selected if user types something other than provided commands.
        
        while True:
            if not keep_game:   # changes selected game
                selected_game = random.choice(games[genre])
            keep_game = False   # boolean makes game reset next iterative process
            print("========================================================")
            print("Game: " + selected_game["title"]) 
            # Show the game title,price, name of developer
            print("Price: " + str(selected_game["price"])) 
            #Has to be a str value because the team was unable to print an int value other than this fashion.
            print("Developer: " + selected_game["developer"])
    
            # Ask the user if they want to add the game to their cart
            add_to_cart = input("Add this game to your cart? Type yes or no.\n").lower()
            if add_to_cart == "yes":
                # If the user says "yes"
                self.cart.append(selected_game)  
                print("Game added to your cart.") #Print game addded_to cart
                break
            elif add_to_cart == "no":
                print("Game not added to your cart.")
                #Print game not added to cart
                self.trash.append(selected_game)
            else:
                print("Please enter a valid command.")
                keep_game = True  # will keep current selected game when looping back to ask yes/no again
              

   
        self.show_cart()

    def show_cart(self):
        subtotal = 0
#Method to sow what is inside the cart
        if self.cart:
            
            print("\nYour cart has these games!")
            for item in self.cart: 
                print(item["title"] + " ($" + str(item["price"]) + ")")
                subtotal += item["price"]
                #Having a title and a price or an item means that it has something into the cart. Therefore, add to cart
        else:
            print("\nThere is nothing inside your cart!")  
#If no price or title inside the cart, nothing is inside thecart.
        print("Subtotal: $", subtotal)

#==============================================================================

def main():
    picker = GamePicker()  
    
    while True:
        print("========================================================")
        for i in range(len(GamePicker.genres)):  
            # The for loop will loop through the entire list 
            print(str(i+1) + ". " + GamePicker.genres[i]) 
            # Print all the options to the user
            
        # This is a method called pick_game. 
        user_input = input("Pick a game genre, and the computer will recommend you a game. Type done when you are finished adding games.\n").upper()

        # First check if genre is valid
        if user_input == "DONE":
            print("You have finished adding games to your cart.")   # Probably will create a more solidified checkout system later
            picker.show_cart()
            break
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

