#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random  

# Holds string values for the code-dictonary
games = {
    #Holds dictonary values of the code
    "ACTION": [
        {"title": "Grand Theft Auto V", "price": 59.99, "developer": "Rockstar Games"},
        {"title": "Assassin's Creed Odyssey", "price": 49.99, "developer": "Ubisoft"},
        {"title": "Spider-Man", "price": 49.99, "developer": "Insomniac Games"},
        {"title": "Red Dead Redemption 2", "price": 59.99, "developer": "Rockstar Games"},
        {"title": "Mortal Kombat 11", "price": 59.99, "developer": "NetherRealm Studios"},
        {"title": "God of War", "price": 59.99, "developer": "Santa Monica Studio"}
    ],
    "ADVENTURE": [
        {"title": "The Last of Us", "price": 59.99, "developer": "Naughty Dog"},
        {"title": "Zelda: Breath of the Wild", "price": 59.99, "developer": "Nintendo"},
        {"title": "Tomb Raider", "price": 49.99, "developer": "Crystal Dynamics"},
        {"title": "Horizon Zero Dawn", "price": 59.99, "developer": "Guerrilla Games"},
        {"title": "Uncharted 4", "price": 59.99, "developer": "Naughty Dog"},
        {"title": "The Witcher 3: Wild Hunt", "price": 49.99, "developer": "CD Projekt Red"}
    ],
    "RPG": [
        {"title": "Final Fantasy VII Remake", "price": 59.99, "developer": "Square Enix"},
        {"title": "Persona 5", "price": 49.99, "developer": "Atlus"},
        {"title": "The Elder Scrolls V: Skyrim", "price": 39.99, "developer": "Bethesda Game Studios"},
        {"title": "Dark Souls III", "price": 59.99, "developer": "FromSoftware"},
        {"title": "Cyberpunk 2077", "price": 59.99, "developer": "CD Projekt Red"},
        {"title": "Dragon Age: Inquisition", "price": 39.99, "developer": "BioWare"}
    ],
    "SHOOTER": [
        {"title": "Call of Duty: Warzone", "price": 0.00, "developer": "Activision"},
        {"title": "DOOM Eternal", "price": 59.99, "developer": "id Software"},
        {"title": "Overwatch", "price": 39.99, "developer": "Blizzard Entertainment"},
        {"title": "Battlefield V", "price": 59.99, "developer": "EA DICE"},
        {"title": "Apex Legends", "price": 0.00, "developer": "Respawn Entertainment"},
        {"title": "Fortnite", "price": 0.00, "developer": "Epic Games"},
        {"title": "Valorant", "price": 0.00, "developer": "Riot Games"}
    ],
    "STRATEGY": [
        {"title": "Civilization VI", "price": 59.99, "developer": "Firaxis Games"},
        {"title": "Starcraft II", "price": 39.99, "developer": "Blizzard Entertainment"},
        {"title": "Age of Empires IV", "price": 59.99, "developer": "Relic Entertainment"},
        {"title": "Total War: Warhammer III", "price": 59.99, "developer": "Creative Assembly"}
    ]
}

class GamePicker:
    genres = ["ACTION", "ADVENTURE", "RPG", "SHOOTER", "STRATEGY"]
    commands = ["yes", "no", "DONE"]
    
    def __init__(self):
        
        self.cart = []  
        # Create a variable that holds the values above. THe user will select values from above and add it to this list

    def pick_game(self, genre):       

        selected_game = random.choice(games[genre])
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
            # Add the game to the cart if no do not add to cart
            print("Game added to your cart.") 
   #Print game addded_to cart
        elif add_to_cart == "no":
            print("Game not added to your cart.")
            return False
        else:
            print("Please enter a valid command.")
              
#Print game not add to cart
   
        self.show_cart()

    def show_cart(self):
#Method to sow what is inside the cart
        if self.cart:
            
            print("\nYour cart has these games!")
            for item in self.cart: 
                print(item["title"] + " ($" + str(item["price"]) + ")")  
                #Having a title and a price or an item means that it has something into the cart. Therefore, add to cart
        else:
            print("\nThere is nothing inside your cart!")  
#If no price or title inside the cart, nothing is inside thecart.

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