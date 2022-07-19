# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re #re will be used to ensure the correct combination is used on the lock.

def help():
    print("This game has several commands that will be of use to you:")
    print("EXAMINE [X], USE [X] ON [Y], GO SOUTH, GO NORTH, GO EAST, GO WEST")
    print("Movement may be attempted at any time, but you must choose previously mentioned objects to EXAMINE or USE.")
    print("Make sure that your commands are in CAPITAL LETTERS.")

#The southern room function
def south():
    global key
    global bLight
    south = "True"
    while south == "True":
        print("\nEntering the room to the south, you see lining the walls are several empty BOOKSHELVES.")
        print("Covering the floor is an ornate RUG with the design of a birdcage.")
        schoice = input("\nWhat will you do? ")
        if schoice == "GO SOUTH":
            print("There is no room this direction.")
        elif schoice == "GO NORTH":
            south = "False"
        elif schoice == "GO EAST":
            print("There is no room this direction.")
        elif schoice == "GO WEST":
            print("There is no room this direction.")
        elif schoice == "EXAMINE RUG":    
            print("Underneath the rug you find a small KEY. You decide to take it with you.")
            key = 1
        elif schoice == "EXAMINE BOOKSHELVES":
            print("The strangest thing about these shelves is that there's nothing here.")
            print("They must be here for some reason, but what?")
        elif schoice == "USE BLACKLIGHT ON BOOKSHELVES" and bLight == 1:
            print("You shine the BLACKLIGHT on the BOOKSHELVES.")
            print("A hidden message appears! '9 _ _'")
            print("There's room for two more numbers, but where would they be?")
        elif schoice == "USE BLACKLIGHT ON BOOKSHELVES" and bLight == 0:
            print("You don't have a BLACKLIGHT to USE.")
        elif schoice == "HELP":
            help()
        else:
            print("Invalid Input.")
    
#the eastern room function
def east():
   global key
   east = "True"
   while east == "True":
       print("\nThe interior of this room is humid, as if it was some sort of menagerie.")
       print("hanging from the ceiling are several colorful ropes with wooden blocks connecting them")
       print("among the ropes lies a brass BIRDCAGE.")
       echoice = input("\nWhat will you do? ")
       if echoice == "GO SOUTH":
           print("There is no room this direction.")           
       elif echoice == "GO NORTH":
            print("There is no room this direction.")
       elif echoice == "GO EAST":
            print("There is no room this direction.")
       elif echoice == "GO WEST":
            east = "False"
       elif echoice == "EXAMINE BIRDCAGE":    
            print("Within the BIRDCAGE you see a pigeon, or perhaps an approximation of one.")
            print("The bird lies completely still upon its perch; A taxidermy of a beloved pet?")
            print("Upon its leg is a holster for carrying messages, with a slip of PAPER still inside.")
            print("Attempting to open the cage reveals that it is locked, and a key is necessary to open it.")
       elif echoice == "USE KEY ON BIRDCAGE":
           if key == 1:               
               print("You use the small key to open the BIRDCAGE. You now have access to the PAPER within.")
               paper = 1
           else:
               print("You don't seem to have a KEY on you.")
       elif echoice == "EXAMINE PAPER" and paper ==1:
           print("Examining the slip of paper, you find it says, '_ 2 _'")
           print("There's room for two more numbers, but where would they be?")
           print("You return the paper to the cage, having gotten the information you need.")
       elif echoice == "EXAMINE PAPER" and paper ==0:
           print("You can't reach the paper inside the birdcage.")
       elif echoice == "HELP":
           help()
       else:
           print("Invalid Input.")
            
#the western room function    
def west():
    global bLight
    west = "True"
    while west == "True":
        print("\nEntering the room to the west, you find a strange sight:")
        print("The WALLS are completely covered with writing, black upon white.")
        print("BOOKS are strewn across the floor, making it difficult to navigate.")
        wchoice = input("\nWhat will you do? ")
        if wchoice == "GO SOUTH":
            print("There is no room this direction.")
        elif wchoice == "GO NORTH":
            print("There is no room this direction.")
        elif wchoice == "GO EAST":
            west = "False"
        elif wchoice == "GO WEST":
            print("There is no room this direction.")
        elif wchoice == "EXAMINE BOOKS":    
            print("You examine the scattered books for any potential leads, but they all seem to lack any text or titles.")
            if input("Continue searching? (Y/N)") == "Y":
                print("""You continue searching more and more books, until you find a book that is glued shut.
After forcing it open, you come to the realization that this book had been repurposed 
as a container for a BLACKLIGHT! You add it to your inventory.""")
                bLight = 1      
        elif wchoice == "EXAMINE WALLS":
            print("You examine the text on the walls.")
            print("Printed over and over are numbers, endlessly wrapping around the room.")
            print("913546208239846210251632103165489520134259683101569845632101345689...")
            print("You can't make heads or tails of it, as if the numbers were written at random.")
            print("Is there something you're missing?")
        elif wchoice == "USE BLACKLIGHT ON WALLS" and bLight == 1:
            print("You point the BLACKLIGHT at the WALLS.")
            print("A message appears!")
            print("It says: Something is missing. The Final piece of the puzzle. The final number isn't on the wall.")
            print("Maybe you should take another look at the walls...")
        elif wchoice == "USE BLACKLIGHT ON WALLS" and bLight == 0:
            print("You don't have a BLACKLIGHT to USE.")
        elif wchoice == "HELP":
            help()
        else:
            print("Invalid Input.")
    
#dungeon crawl: The actual output of the file begins here.
print("This game has several commands that will be of use to you:")
print("EXAMINE [X], USE [X] ON [Y], GO SOUTH, GO NORTH, GO EAST, GO WEST")
print("Movement may be attempted at any time, but you must choose previously mentioned objects to EXAMINE or USE.")
print("Make sure that your commands are in CAPITAL LETTERS.")
input("type anything to start: ")
Begin = "OK"
Door = "Closed" #state of the final door
key = 0 #key inventory, either have or dont have.
bLight = 0 #blacklight inventory, either have or dont have.
while Begin == "OK": #the main loop of the program, if this loop ends the game ends.
    print("\nYou stand within a stark white room. In front of you to the NORTH is a door locked with a rusty PADLOCK.")
    print("To the SOUTH, EAST and WEST are doorways to other rooms.")
    choice = input("\nWhat will you do? ") #user's input entered into a variable which is checked in if-else
    if choice == "GO SOUTH":
        south() #user enters southern room
    elif choice == "GO NORTH": 
        if Door == "Open": #checks state of final door
            print("You open the door and finally escape the room.")
            input("YOU WIN!") #gives the user a second to see they actually won the game. input is unimportant.
            break #ends the game
        else:
            print("The PADLOCK on the door bars your path. If only you knew how to remove it...")
    elif choice == "GO EAST":
        east() #user enters eastern room    
    elif choice == "GO WEST":
        west() #user enter western room    
    elif choice == "EXAMINE PADLOCK":
        print("Upon further inspection, the padlock requires a 3 number combination.")
        print("Once you've found the combination, USE the combination on the PADLOCK.")
        print("There are three surrounding rooms, and three numbers. Perhaps one number per room?")
    elif choice == "quit": #dev quit button
        Begin = "STOP" #another way of ending the loop, changing the begin variable.
    elif choice == "HELP": #provides helpful text
        help()
    elif re.search('USE ... ON PADLOCK', choice): #checks if a 3 character combination is in place of dots
        if choice == "USE 927 ON PADLOCK":
            print("You enter the combination 927 into the PADLOCK and...\n\n")
            print("The PADLOCK comes loose, falling to the floor! Now the path forward is open.")
            Door = "Open"
        elif choice == "USE KEY ON PADLOCK" and key == 1:           
            print("Upon further inspection, there is no keyhole on the PADLOCK.")
            print("This padlock requires a three number combination.")
        elif choice == "USE KEY ON PADLOCK" and key == 0: 
            print("You don't seem to have a KEY on you.")
        else:
            print("It doesn't seem to work...")
    else:
        print("Invalid Input.")