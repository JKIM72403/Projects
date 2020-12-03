#Personality: 'Sassy' 
#IoT Device: Physical Alarm Clock

#The code is divided into three main sections. 1: Room settings. 2: New Toilet Function settings. 3: New interactive shared information function

#1: Has 5 new input variables (user_verification, drink, room_temperature, room_light, want_to_change). Has 5 main if-else(elif) statements. Has 2 lists (known_users, available_caffeine_levels). Has 1 Dictionary of one object (current_settings). Has 2 For Loops.
#2: Has 4 new input variables (seat_warmer, bidet_strength, dryer_strength, verification). Has 4 main if-else(elif) statements. Has 1 Dictionary of one Object (Toilet_settings). Has 2 different For Loops.
#3: Has 1 new input variable (shared_settings). Has 1 main if-else statement. Has 1 For Loop. Has 1 Nested Dictionary of similar objects (user_shared_settings).

print("For all answers please use lowercase letters\n")

#Listing different and new input variables including new material:

#1a: Asking for user's name to allow the Alarm clock to interact better with the user, adding customization
known_users = ['jonathan', 'tyson', 'nathan']
user_verification = input(f"The known users are {known_users}\nYou listed there?: ")
if 'yes' in user_verification:
    user = input("\nWhich one are you: ")
    print(f"Welcome back {user.title()}!\n")
else:
    user = input("\nWhats your name then?: ")
    print(f"HA...I knew your name was {user.title()}! I was just joking earlier...\n")

#1b: Reusing a variable from the q1_final to get more information about the user to create a more realistic conversation
Wake_up_time = input("What time do you need to be up by?: ")
print(f"{Wake_up_time}!? That early?! Putting me to work that early only hurts you, ya know!\n")

#1c: Asking the user if they want coffee. Depending on their answer, they will choose a caffeine percentage or choose if they want water instead.
available_caffeine_level = [5, 10, 30, 50, 70, 80]
drink = input("Hey, do you want some coffee ready when you wake up?: ")
if 'yes' in drink:
    caffeine_level = int(input(f"\nEw...coffee isnt my style...but I digress. The 6 percentages of caffeine I can prepare are {available_caffeine_level}. What percent do you want?: "))
    if caffeine_level <= 30 in available_caffeine_level:
        print(f"Your coffee is set to have {caffeine_level} percent caffeine and will be ready at {Wake_up_time}!\n")
    elif caffeine_level >= 50 in available_caffeine_level:
        print("You might not be able to fall asleep after you drink that amount, but your the boss...\n")
    else:
        print(f"I can't prepare {caffeine_level} percent, Sorry, maybe in my next update.\n")
else:
    new_drink = input("Phew, last time someone used my services, they wanted coffee...ew. Anyways, do you at least want some water?: ")
    if 'yes' in new_drink:
        print(f"It'll be ready for you at {Wake_up_time}!\n")
    else:
        print("Well, you can't say I'm responsible for your dehydration issues... as you wish.\n")

#1d: Inputting current temperature in the user's room.
room_temperature = int(input("Hey what is the current temperature of your room in degrees celcius?: "))
if room_temperature > 20:
    print(f"Just letting you know, according to sleep.com, that temperature is higher than the ideal sleeping temperature.\n")
elif room_temperature <= 15:
    print(f"Thats really cold {user}, like really cold, better layer up!\n")
else:
    print(f"That is the most ideal sleeping temperature according to sleep.com! I guess you'll hate me even more HAHAHA!\n")

#1e: Inputting current light strength level in the user's room.
room_light = int(input("Hey on a scale of 1-10 (10 being the brightest) how bright is your room right now?: "))
if room_light > 5:
    print("Your current room light is too bright for you to have an ideal night's sleep.")
elif room_light <= 2:
    print(f"I just checked and your lights at level {room_light} brightness emit a large amount of blue-light waves which can disrupt your sleep, so I'll turn off the blue-light waves your lights produce.\n")
else:
    print("Your lights, although brighter than I would recommend, are alright to sleep in.\n\n")

#1f: Putting 1b, d, e inside of a dictionary of one object (the room).
current_settings = {
    'current temperature': f'{room_temperature}', 
    'current light strength': f'{room_light}', 
    'current wake up time': f'{Wake_up_time}',
}
#1g: The IoT device rechecks the information inputted by printing out their room's settings.
print(f"{user.title()}, so just to recap what I have so far, your room's ")
for names, current in current_settings.items():
    print(f'{names.title()} is set at {current}.')

#1h: Iot device allows the user to change one of their inputted values if they so choose. And then prints out the new dictionary of information. Or allows the user to not change any of the inputted information.
want_to_change = input("\nDo you want to change any one of these?: ")
if 'yes' in want_to_change:
    changed = input("Which one of the three do you want to change (Please type: 'current temperature', 'current light strength', or 'current wake up time')?: ")
    if "current temperature" in changed:
        new_temp = int(input("What do you want your new temperature celcius degree to be?: "))
        current_settings["current temperature"] = new_temp
        print(f"\n{user.title()}, so after your changes, your new room's ")
        for names, current in current_settings.items():
            print(f"{names.title()} is now set at {current}.")
    elif "current light strength" in changed:
        new_light = int(input("What do you want you new light strength level to be?: "))
        current_settings["current light strength"] = new_light
        print(f"\n{user.title()}, so after your changes, your new room's ")
        for names, current in current_settings.items():
            print(f"{names.title()} is now set at {current}.")
    elif "current wake up time" in changed:
        new_wake_up_time = int(input("What do you want you new wake up time to be?: "))
        current_settings["current wake up time"] = new_wake_up_time
        print(f"\n{user.title()}, so after your changes, your new room's ")
        for names, current in current_settings.items():
            print(f"{names.title()} is now set at {current}.")
    else: print("You have mistyped the setting you wanted to change, sorry.")
else: print("Alright sounds good!")

#2a: Introducing the new function that the IoT device has access to a toilet that it can optimize for the user.
print(f"\n\n{user.title()}, you just got a new japanese toilet that I am connected to, even though I don't want to be...yuck. Anyways, this toilet has several functions that I'll need you to set up so that it'll be all ready for your morning buisness.")

#2b: Inputting the wanted seat warmth of the toilet seat. 
seat_warmer = int(input("\nThe new toilet's first feature is a seat warmer. With 10 being the hottest setting I can set and 1 being off, on a scale of 1-10 how hot do you want your seat to be?: "))
if seat_warmer >= 7:
    print(f"{user.title()}, that's really hot, it might just burn ya!\n")
elif seat_warmer <= 6:
    print(f"Ill set the seat to level {seat_warmer} for you.\n")
elif 1 in seat_warmer:
    print("Alright, I'll turn it off for you!")
else:
    print(f"C'mon now, {seat_warmer} is out of my range, I'm sorry.\n")

#2c: Inputting the wanted Bidet strength of the toilet.
bidet_strength = int(input("The second feature is with the automatic bidet, It'll find where it needs to go, you just need to set how strong it'll come out... With 10 with the strongest and 1 being off, on a scale of 1-10 how strong do you want it to be?: "))
if bidet_strength >= 7:
    print("I know bidets are supposed to be strong, but isn't that overkill, or rather overspray?...Sorry my puns need a software update.\n")
elif bidet_strength <= 6:
    print(f"{user.title()}, I'll be set at level {bidet_strength}.\n")
elif 1 in bidet_strength:
    print("Ill be sure to turn it off for you!")
else:
    print(f"Sorry {user.title()}, I'm not able to set it at {bidet_strength} level, its out of my range.")

#2d: Inputting the wanted dryer strength of the toilet.
dryer_strength = int(input("The last feature is the dryer that... dries a recently cleaned area... with 10 being the strongest and 1 being off, on a scale of 1-10 how strong do you want the dryer to be?: "))
if dryer_strength >= 7:
    print(f"{user.title()} thats so strong it just might just blow your socks off!\n")
elif dryer_strength <= 6:
    print(f"I'll set your dryer strength to {dryer_strength}.")
elif 1 in dryer_strength:
    print("Ill be sure to turn it off for you.")
else: 
    print(f"Sorry {user.title()}, that is not in my range of capabilities, maybe it'll be added in my next patch!\n")

#2e: Putting 2b, c, d input variables into a dictionary of one object (the toilet)
toilet_settings = {
    'current seat warmth': f"{seat_warmer}",
    'current bidet strength': f"{bidet_strength}",
    'current dryer strength': f"{dryer_strength}",
}
#2f: Allowing the User to recheck through their inputted information by printing out the ditionary.
print("\nSince this is a new feature, I want to recheck through your information. Your...")
for function, setting in toilet_settings.items():
    print(f"{function.title()} is set at {setting}/10.")

#2g: Allowing the user to choose if they want to change some of the inputted information and then listing the new settings if they changed it.
verification = input("Is you information inputted correctly?: ")
if 'yes' in verification:
    print("Alright Ill have it set up ready for you when you wake up.")
else:
    changed_toilet_setting = input("Which one of the three features do you want to change (Please type: 'current seat warmth', 'current bidet strength', or 'current dryer strength'): ")
    if 'current seat warmth' in changed_toilet_setting:
        new_warmth = input("Out of 10, what would you like to change your level to?: ")
        toilet_settings['current seat warmth'] = new_warmth
        print(f"\n\n{user.title()}, so after your changes, your new toilet settings are...")
        for function, setting, in toilet_settings.items():
            print(f"{function.title()} is now set at {setting}/10.")
    elif 'current bidet strength' in changed_toilet_setting:
        new_bidet_strength = input("Out of 10, what would you like to change your strength level to?: ")
        toilet_settings['current bidet strength'] = new_bidet_strength
        print(f"\n\n{user.title()}, so after your changes, your new toilet settings are...")
        for function, setting, in toilet_settings.items():
            print(f"{function.title()} is now set at {setting}/10.")
    elif 'current dryer strength' in changed_toilet_setting:
        new_dryer_strength = input("Out of 10, what would you like you new")
        toilet_settings['current dryer strength'] = new_dryer_strength
        print(f"\n\n{user.title()}, so after your changes, your new toilet settings are...")
        for function, setting, in toilet_settings.items():
            print(f"{function.title()} is now set at {setting}/10.")
    else: 
        print("You have mistyped the name of the function, sorry I'm not that advanced yet.")

#3a: Creating a nested dictionary of 'Jonathan's' user settings and the user's user settings (similar objects)
user_shared_settings = {
    'jonathan': {
        'set wake up time' : '9',
        'set temperature' : '21',
        'set light strength' : '3',
    },
    f"{user}": {
        'set wake up time' : current_settings['current wake up time'],
        'set temperature' : current_settings['current temperature'],
        'set light strength' : current_settings['current light strength']
    }
}
#3b: Introducing the new function of the IoT device to allow users to compare their room settings to other users. If user chooses 'yes' the different settings will be printed out so they can view the differences. If the user chooses anything else, they will not take part in this new function.
shared_settings = input(f"\n\nHey {user.title()}, a new feature of mine is my connection to other 'smart alarm clocks'. Users can request to compare their data with other known users. A previous user named Jonathan has requested to view and compare your room's settings to his. Would you like to participate in the comparison?: ")
if 'yes' in shared_settings:
    print("\n\nHere are his and your settings: ")
    for username, interaction_info in user_shared_settings.items():
        print(f"\nName of User: {username.title()}\n\tThe set wake up time is set at {interaction_info['set wake up time']} \n\tThe set temperature is {interaction_info['set temperature']} degrees celcius. \n\tThe set light strength is set at level {interaction_info['set light strength']}.")
else:
    print("Ill decline Jonathan's request to view and compare your data.\n")

#Provide a summary response paragraph where the IoT’s personality clearly shows its opinions about 4-5 of the user’s answers:
print(f"""
So {user}, as just a mere alarm clock, I shouldn't give my opinion, but by golly some of
your settings really weird me out... Like your Wake up time is way to early for my liking.
Ya know, for it to be set at {Wake_up_time} means I need to wake up earlier than you! Geez, 
working me down to my gears... Also your room's light at {room_light} is way to strong for me.
I'm not solar powered! It'd be more useful just to turn it off, geez. Not to mention your room's
temperature...I can almost feel myself sweating, maybe its the electricity flowing through me, but
your {room_temperature} degree room isn't helping me. Alright, I've been lecturing you for a bit but
there's one more thing I can't really understand... your toilet warmth feature. Now {seat_warmer} 
isn't as bad as some of your other settings but is that really necessary? A {seat_warmer} just seems
like wasted electricity that couldv'e been used to power me... Sorry for going on for so long...I 
guess I was just programmed this way.
""")

#The success criteria states that I need to list a list, dictionary of similar and of one object. Since I had multiple lists and dictionaries, I only printed out one of each.
print(available_caffeine_level, current_settings, user_shared_settings)