#The potential IoT device chosen is a 'Sassy' physical Alarm Clock


#listing 10 different input variables with personality-based responses:

#This input variable is useful becuase it adds a "smart" aspect to the alarm clock as it can use this data for further analysis like to detect if the user is getting their targeted amount of sleep
Target_sleep = input("\nWhat is your target number of hours of sleep?: ")
print(f"\nI'm almost 99% sure that {Target_sleep} is not enough, but I mean like who am I to judge, right?.\n")

#This is relevant information because an alarm clock's function is to wake up the user at a specific time.
Wake_up_time = input("\nWhat time do you need to be up by?: ")
print(f"\nHAHAHA, sorry I couldn't hold in my laughter. You need to be awake by {Wake_up_time}?! I feel bad for you, yet at the same time, I don't becuase it couldnt be me...haha.\n")

#Since this is a "smart" alarm clock, it will be able to use this user data for analytical purposes, like finding the average amount of sleep of the user, which adds a layer of personalization for the user.
Sleep_time = input("\nWhat time are you sleeping tonight?: ")
print(f"\nHey, just so you know, I'll be recording your sleep time of {Sleep_time}. I'll be using this data to tell you if you have reached your targeted hours of sleep, although I seriously doubt you will.\n")

#An alarm clock's purpose is to wake up the user, in this case, with sound. Meaning that adding a configurable sound will add a layer of customization for the user. Also this device is connected to the internet, so it can search up the user's specified/personalized genre of music
Alarm_soundtype = input("\nWhat genre of music would you want me to wake you up with?: ")
print(f"\nWhy am I not suprised? I knew you liked {Alarm_soundtype} music. Ill search up {Alarm_soundtype} playlists on spotify and randomize them to be played when you wake up.\n")

#An alarm clock's purpose is to wake up the user, this alarm clock will have the available feature of vibration, in addition to others like sound and light, that will wake up the user. By reciving user data, the alarm clock can configure itself to the preferences of the user which adds customization.
Vibration_power = input("\nA recent feature was added to where I have the feature to vibrate in addition to playing songs. With 10 being maximun power and 0 being off, on a scale from 0-10 how strong do you want the vibrations of the alarm clock to be?:")
print(f"\nI'll set the vibration power level to {Vibration_power}\n")

#An alarm clock's purpose is to wake up the user, this alarm clock will have the available feature of light, in addition to others like sound and vibration, that will wake up the user. By reciving user data, the alarm clock can configure itself to the preferences of the user which adds customization.
Light_strength = input("\nAnother feature was added to where I am connected to your ceiling lights in addition to vibration and playing songs. With 10 being the brightest and 0 being off, on a scale from 0-10 how strong do you want them to be to wake you up?: ")
print(f"\nIll set the light strength to {Light_strength} by the time your alarm sound rings. It'll be a nice 'rise and shine' ya?\n")

#This input variable is useful because alarm clocks use a snooze feature so that the user can get a bit more sleep. The user will most likely use the snooze feature, so knowing exactly how long they want each snooze duration to be will add a layer personalization/customization.
Snooze_duration = input("\nHey, what is the number of minutes you want each snooze to last for?: ")
print(f"\nDang, {Snooze_duration} minutes?! I thought you would put less, but I guess you know yourself better than I do.\n")

#This input variable is useful and relevant because if a snooze function is unlimited, then the user would most likely not wake up for a while. Normally, the snooze feature get hit more than once so having this customized to their preferces will allow them to wake up after their cutomized and personalized amount of snoozes.
Snooze_amount = input("\nHow many times do you want to be able to snooze?: ")
print(f"\nOh my, {Snooze_amount} times? Think you have enough? Haha, sorry that was sarcasm, I'll  set it so that you will have {Snooze_amount} snoozes.\n")

#This input variable is important to the user becuase the input directly effects how effective the alarm clock will be for the user at waking them up
Volume = input("\nWith 10 being the loudest, on a scale from 1-10 how loud does the alarm sound need to be?: ")
print(f"\nGeez at {Volume}, I can already feel my speakers getting sore! Well not that I have a choice but, I'll set it to {Volume} even if it hurts my speakers...\n")

#Setting alarm clocks can be tedious, so having it set for other days automatically creates convience for the user. Normally, people have to wake up at a uniform/consistent time for their work/school meaning that the alarm should be the same.
Repetition = input("\nWhat other days of the week do you want this alarm to be set for?: ")
print(f"\nSounds good. I'll be waking you up on {Repetition} as well...You really are working to my 'bits'\n")


#Input variable list for the user:
User_data = [Target_sleep, Wake_up_time, Sleep_time, Alarm_soundtype, Vibration_power, Light_strength, Snooze_duration, Snooze_amount, Volume, Repetition]


#Final print function to report back to the user:
print(f"\n\nConsise Summary of User Data Collected: \n\tYour targeted hours of sleep is {User_data[0]}\n\tYou want your alarm to wake you up at {User_data[1]}\n\tYou said you will be sleeping by {User_data[2]}\n\tYou want to be woken up by {User_data[3]} music that I will find on a random spotify playlist.\n\tYou want the power level of the vibration feature to be set at {User_data[4]}.\n\tYou want the power level of the light feature to be set at {User_data[5]}.\n\tYou want each snooze to last for {User_data[6]} minutes.\n\tYou want to have {User_data[7]} snoozes.\n\tYou want to the volume of the alarm to be set at {User_data[8]}\n\tYou want this preset alarm to be repeated on {User_data[-1]}")


#Additional List Methods:
del User_data[-1]
Broken_Parts = 'vibration motor'
User_data.remove(User_data[4])
print(f"\n\nThere are some changes that have come to my attention:\n\nThe rest of this week is a holiday and I know you like to sleep in, so I have deleted the days of the week you wanted me to repeat the alarm.\nMy {Broken_Parts.title()} is currently broken, so the feature is unavilable for the time being. I have removed your chosen vibration power level from the list.\n\n")


#Printing out final List (8)
print(User_data)