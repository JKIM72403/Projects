#Theme: Egyptian Tomb Escape Room

#Initial Boolean Variables values used to activate/deactivate certain while loops and actions at the intended time
start = True
treasure_room = False
no_key = True
has_key = False
dusted_paintings = True
not_have_dictionary_painting = True
have_dictionary_painting = False
not_have_coffin_instructions = True
coffin_instructions = False
coffine_opened = False
brush_not_taken = True
treasure_taken = False


#Lists used with For Loops to list options/actions
walkie_talkie_light = ["A. Turn it on", "B. Leave it off"]
brush_item = ["A. Pick up the brush", "B. Leave the brush"]
movement_a = ["A. Study the Door", "B. Touch the details of the engravings", "C. Leave to investigate the other parts of the room"]
movement_b = ["A. Brush the dust off the paintings", "B. Study the paintings"]
movement_c1 = ["A. Open the first one", "B. Open the Second one", "C. Open the Third one", "D. Leave to investigate other parts of the room"]
movement_c2 = ["A. Pick up dictionary", "B. Close drawer"]
movement_d1 = ["A. Stare at the Sarcophagus", "B. Touch the details of the Sarcophagus", "C. Insert Password into Sarcophagus", "D. Leave to investigate other parts of the room"]
movement_d2 = ["A. Take the key", "B. Leave without the key"]
treasure_movement = ["A. Take the King's most prized possession, the diamond necklace", "B. Stare at the diamond necklace", "C. Try to open the closed exit door"]

#Items list with starting item: Flashlight
User_Items = ["Walkie Talkie"]

#Introductory paragraph
print ("""
Welcome! You are currently stuck in the Valley of the Kings in the famous
Pharaoh Tutankhamun's tomb. You do not know how you got here. All you know
is you need to escape out of this place. Its hard to see but you feel a 
plastic rectangular item in your hand. Do you have the smarts, willpower,
and hope to escape?
""")

#Start of the Game
Username = input("Greetings. I am The Guide. I am talking to you through the walkie talkie in your hand. I will be assisting you in your escape from this tomb. How should I refer to you by?: ").lower()

#Turning on Light
print(f"\n{Username.title()}, you currently have a {User_Items[0]}. It is currently pitch black. You feel the walkie talkie in you hand and find an unknown switch. Your options are: ")
while True:
    for begin in walkie_talkie_light:
        print(f"{begin}")
    action_1 = input("What will you do?: ").lower()
    if action_1 == "a":
        print("\nThe switch turned on a small light on the walkie talkie. The room is more visible. You can see outlines of several different objects and some paintings on the wall, but they will require a closer look.")
        break
    elif action_1 == "b": 
        print("\nNothing happened. The room is not visible. You cannot escape from darkness. In order to see, you will need light. Your options are:")
    else:
        print("\nYou have entered in an answer that I do not understand. Sorry, Please answer again. Your options are:")
#Picking up first Item
print("\nWhile testing the small flashlight on your walkie talkie, you see a brush on the ground. Although you do not know its purpose, it may come in handy later on. Your options are:")
while brush_not_taken:
    for brush_option in brush_item:
        print(f"{brush_option}")
    brush = input("What will you do? ").lower()
    if brush == "a":
        User_Items.append("Brush")
        print("\nYour current inventory has:")
        for items in User_Items:
            print(f"- {items}")    
        brush_not_taken = False
    elif brush == "b":
        print("\nJust as you are about to leave, your mind wonders why the brush was on the ground. You feel like it is important to have. Unable to leave it, you single your options to: ")
        brush_item.remove("B. Leave the brush")
    else: 
        print("\nYou have entered an answer that I do not understand. Your options right now are: ")
#Start of movement/investigation choices
while start:
    movement = input(f"\n{Username.title()}, from your current position, in front of you, you see a locked door. To your left you see a wall painting. To your right you see a drawer. You take a look behind you and you see a Sarcophagus (Egyptian Coffin). Which direction will you investigate? \nA. Foward\nB. Left\nC. Right\nD. Backward\n ").lower()
    #Movement FOWARD to the locked door
    if movement == "a":
        while no_key:
            print("\nYou are investigating the locked door infront of you. Your options right now are: ")
            for option1 in movement_a:
                print(f"{option1}")            
            Door_to_treasure = input("What will you do? ").lower()
            if Door_to_treasure == "a":
                print("\nYou notice how tall the doors are. Laced with yellow and white gold, there seems to be engravings on it. ")
            elif Door_to_treasure == "b":
                print("\nThe door's engravings are intricate and detailed. You can tell that they are engravings forming a shape similar to a human, but you dont understand what its for. You feel the small hole underneath the handle and notice how it is the shape of a deep keyhole. ")  
            elif Door_to_treasure == "c":
                break
            else:
                print("\nYou have entered an answer that I do not understand. ")
        while has_key:
            print("\nYou are investigating the door that was infront of you. Your option right now are: ")
            for option1 in movement_a:
                print(f"{option1}")      
            Door_to_treasure = input("What will you do? ").lower()
            if Door_to_treasure == "a":
                print("\nYou notice how tall the doors are. Laced with yellow and white gold, there seems to be engravings on it. You also notice a little hole near the handle, perhaps a key would fit. ")
            elif Door_to_treasure == "b":
                print("\nThe door's engravings are intricate and detailed. You can tell that they are engravings forming a shape similar to a human, but you dont understand what its for. You feel the small hole underneath the handle and notice how it is the shape of a deep keyhole.")  
            elif Door_to_treasure == "c":
                break
            elif Door_to_treasure == "d":
                print("\nThe key fits prfectly. You push the door open! ")
                treasure_room = True
                start = False
                break
            else:
                print("\nYou have entered an answer that I do not understand. ")
    #Movement LEFT to the wall paintings
    elif movement == "b":
        while dusted_paintings:
            print("\nYou are investigating the wall paintings to your left. You shine the small flashlight on your walkie talkie to see the paintings better. Your options right now are: ")
            for option2 in movement_b:
                print(f"{option2}")            
            wall_painting = input("What will you do? ").lower()
            if wall_painting == "a":
                print("\nYou brushed the dust off the wall paintings. They are more visible now. ")
                dusted_paintings = False
                movement_b.append("C. Leave to investigate other parts of the room")
            elif wall_painting == "b":
                print("\nThe painting is covered in dust. Perhaps brushing the dust away will help you see the paintings.")
            else:
                print("\nYou have entered an answer that I do not understand.")
        while not_have_dictionary_painting:
            print("\nYou are investigating the wall paintings to your left. You shine the small flashlight on your walkie talkie to see the paintings better. Your options right now are: ")
            for option2 in movement_b:
                print(f"{option2}")            
            wall_painting = input("What will you do? ").lower()
            if wall_painting == "a":
                print("\nThere is no more dust covering the painting. You are still at the painting.")
            elif wall_painting == "b":
                print("\nThe paintings are visible now. However, you cannot make sense of what the painting means. Maybe a dictionary will help you decipher the painting.")
            elif wall_painting == "c":
                break
            else:
                print("\nYou have entered an answer that I do not understand.")
        while have_dictionary_painting:
            print("\nYou are investigating the wall paintings to your left. You shine the small flashlight on your walkie talkie to see the paintings better. Your options right now are: ")
            for option2 in movement_b:
                print(f"{option2}")            
            wall_painting = input("What will you do? ").lower()
            if wall_painting == "a":
                print("\nThere is no more dust covering the painting and you have the dictionary you can use to understand the painted hieroglyphs. You are still at the painting.")
            elif wall_painting == "b":
                print("\nYou understand the egyptian hieroglyphs now. The Hieroglyphs state 'in order to open the Sarcophagus, you need to enter the password: 'TutIsTheBest''")
            elif wall_painting == "c":
                break
            else:
                print("\nYou have entered an answer that I do not understand.")
    #Movement RIGHT to the drawer
    elif movement == 'c':
        while not_have_dictionary_painting:
            have_dictionary_painting = False
            print("\nYou are investigating the drawer to your right. There are a three closed compartments. Your options are: ")
            for option3 in movement_c1:
                print(f"{option3}")    
            drawer_choice = input("What do you want to do? ").lower()
            if drawer_choice == "a":
                print("\nThere seems to be nothing inside, so you close it.")
            elif drawer_choice == "b":
                print("\nUnfortunately there seems to be nothing inside this drawer, so you close it back up.")    
            elif drawer_choice == "c":
                print("\nThere is a thick dictionary of Egyptian hieroglyphs to english inside of this drawer. Your options are: ")
                for option4 in movement_c2:
                    print(f"{option4}")  
                dictionary_choice = input("What do you wish to do? ").lower()    
                if dictionary_choice == "a":
                    User_Items.append("Dictionary")
                    print("\nYour current inventory has:")
                    for items in User_Items:
                        print(f"- {items}")
                    print("\nYou can now decipher some of the wall paintings that use these Egyptian hieroglyphs!")
                    not_have_dictionary_painting = False
                    have_dictionary_painting = True
                elif dictionary_choice == "b":
                    print("\nYou have closed the drawer. Without taking the Dictionary.")
                else:
                    print("\nYou have entered an answer that I do not understand. You have closed the drawer.")
            elif drawer_choice == "d":
                break
            else:
                print("\nYou have entered an answer that I do not understand.")
        while have_dictionary_painting:
            print("\nYou are investigating the drawer to your right. There are a three closed compartments. Your options are: ")
            for option3 in movement_c1:
                print(f"{option3}")
            drawer_choice = input("What do you want to do? ").lower()
            if drawer_choice == "a":
                print("\nThere seems to be nothing inside, so you close it. Your options are:")
            elif drawer_choice == "b":
                print("\nUnfortunately there seems to be nothing inside this drawer, so you close it back up. Your options are:")
            elif drawer_choice == "c":
                print("\nThe drawer is empty because you have taken the dictionary already. Your options are: ")
            elif drawer_choice == "d":
                break
            else:
                print("\nYou have entered an answer that I do not understand. Your options right now are: ")
    #Movement BACKWARD to the Sarcophagus/coffin
    elif movement == "d":
        while not_have_coffin_instructions:
            print("\nYou are at the Sarcophagus behind your original position. Your options are to:")
            for option5 in movement_d1:
                print(f"{option5}")
            coffin_choice = input("What would you like to do? ").lower()
            if coffin_choice == "a":
                print("\nYou are staring at the closed Sarcophagus. You notice how there is jeweled letters spelling out 'Tut'. You notice a lock system with a password. Maybe theres something in the room that contains the unknown password.")
            elif coffin_choice == "b":
                print("\nAs you touch the fancily decorated Sarcophagus, you notice how the lock system has a keyboard. Perhaps the Password uses words.")
            elif coffin_choice == "c":
                password = input("\nPassword: ")
                if password == "TutIsTheBest":
                    coffine_opened = True
                    print("\nYou have opened the locked coffin.")
                    break
                else:
                    print("\nThe Password you have entered is incorrect. You leave the coffin area and go to your original position.")
                    break
            elif coffin_choice == "d":
                break
            else:
                print("\nYou have entered an answer that I do not understand. ")
        while coffine_opened:
            print("\nYou see a mummy inside with a key tied around its neck. Your options are:")
            for option6 in movement_d2:
                print(f"{option6}")
            mummy_action = input("What would you like to do? ").lower()
            if mummy_action == "a":
                print("\nYou have taken the key, maybe it'll unlock something...")
                User_Items.append("Key")
                print("\nYour current inventory has:")
                for items in User_Items:
                    print(f"- {items}")
                has_key = True
                no_key = False
                movement_a.append("D. Insert key into keyhole")
                coffine_opened = False
                coffin_instructions = True
                not_have_coffin_instructions = False
            elif mummy_action == "b":
                print("\nYou have not taken the key.")
                break
            else:
                print("\nYou have entered an answer that I do not understand. ")
        while coffin_instructions:
            print("\nYou are at the Sarcophagus behind your original position. You see the opened coffin with the mummy inside it. There is nothing else to do here, so you leave.")
            break
    else: 
        print("\nYou have entered an answer that I do not understand. ")
#Start of second room (treasure room)
while treasure_room:
    print(f"\n{Username.title()}, you are in King Tut's treasure room! The only things in this room is the pedistool with the King's most prized possession (a diamond necklace) on it and the closed exit to leave the escape room. Your options are: ")
    for option7 in treasure_movement:
        print(f"{option7}")
    treasure_choice = input("What will you do? ").lower()
    if treasure_choice == "a":
        print(f"\nYou have taken the diamond necklace. As soon as you do so the exit door opens. Perhaps the pedistool was weight sensitive and opens the door when there is no weight on it.")
        User_Items.append("Diamond Necklace")
        print("\nYour current inventory has:")
        for items in User_Items:
            print(f"- {items}")
        treasure_room = False
        treasure_taken = True        
        break    
    elif treasure_choice == "b":
        print("\nYou look at the huge diamond and notice how clear and beautiful it is.")  
    elif treasure_choice == "c":
        print("\nYou walk up to the closed exit and try to pry it open. It wont budge no matter what. There has to be a way to exit this without using force. ")
    else: 
        print("\nYou have entered an answer that I do not understand. ")    
while treasure_taken:
    print(f"\n{Username.title()}, you are still in King Tut's treasure room! You have taken the necklace. The only thing left in the room is the empty pedistool and the exit to leave the escape room. Your options are: \nA. Leave the Escape Room\nB. Stay in the Escape Room")
    treasure_choice = input("There's not much choice... but what option will you choose? ").lower()
    if treasure_choice == "a":
        print(f"\nCongradulations {Username.title()}, your determination, selflessness, willpower and intellect have guided you through this challenge! Thanks for playing!")
        break
        #Game finished. User forced to pick 'A' to exit the program and loop.
    elif treasure_choice == "b":
        print("\nYou do not leave the Escape room. You should leave because you have finished all of the puzzles and have taken the prize of the necklace.")
    else: 
        print("\nYou have entered an answer that I do not understand. ")  