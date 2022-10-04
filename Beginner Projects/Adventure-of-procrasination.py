#Area: William's Home
#Locations: Kitchen/Dining room, living room, study room
#Objects and characters are shown in the Instances section (line 424)
#Goal: Finish preparation for William's big presentation/ get 10 points and exit to the intersection to finish

#Initial Boolean Variables values used to activate/deactivate certain while loops and actions at the intended time
hasplate = False
noplate = True
begin = True
notplay = True
play = False
brownies_eaten = False
brownies_noteaten = True
wii_on = False
no_controllers = True
has_controllers = False
not_brushed = True
first_throw = True
more_throw = False
angry_dad = True
very_angry_dad = False
first_tutor = True
annoyed_tutor = False
worked_a_little = False
first_time_work = True
eaten = False
not_eaten = True
brushed = False
not_brushed = True

#Preparedness Score Variable
preparescore = 4

#Lists of possible actions
movement = ['a) The Kitchen/Dining Room', 'b) The Living room', 'c) The Study room']
kitchenaction1 = ['a) Talk to the Chef', "b) Talk to William's Mom", "c) Open the refrigerator", "d) Grab the plate", "e) Take the empty seat at the table", "f) Leave back to the intersection"]
kitchenaction2 = ['a) Talk to the Chef', "b) Talk to William's Mom", "c) Open the refrigerator", "d) Take the empty seat at the table", "e) Leave back to the intersection"]
fridgeaction = ['a) Grab and eat the Brownies', 'b) Close the fridge without getting anything']
fridgeaction2 = ['a) Close the fridge without getting anything']
livingaction1 = ['a) Talk to Lucas', 'b) Turn on the Wii', 'c) Walk up to and Pet Bailey', 'd) Grab the Dog Brush', 'e) Throw the Dog Toy', 'f) Leave back to the intersection']
livingaction2 = ['a) Talk to Lucas', 'b) Walk up to and Pet Bailey', 'c) Grab the Dog Brush', 'd) Throw the Dog Toy', 'e) Leave back to the intersection']
gameaction = ['a) Grab the controllers', 'b) Leave the controllers']
studyaction1 = ['a) Talk to Dad', 'b) Talk to the Tutor', 'c) Use the Laptop', 'd) Use the Phone', 'e) Lie down on the couch', 'f) Leave back to the intersection']
laptopaction = ['a) Work on preparation for the presentation', 'b) Play Minecraft', 'c) Scroll through Reddit', 'd) Close the Laptop']
workissue = ['a) Ask Tutor Jerry for help', 'b) Work through the issues on your own']


#Functions
def kitchen_scene():
    print('\nYou have chosen to go to the Kitchen/Dining Room.')
    #I had to specify these boolean and 'score' variable as global so they didnt revert back everytime the function was called.
    global noplate
    global hasplate
    global brownies_eaten 
    global brownies_noteaten 
    global eaten
    global not_eaten
    global preparescore
    while noplate:
        print("\n\nWilliam is now in the Kitchen. William's Mom is sitting at the dinner table, their family chef is hard at work cooking, theres a plate on the counter, the table has an open seat, and the fridge makes a small murmur. Your options are: ")
        for kitchenoption1 in kitchenaction1:
            print(f"{kitchenoption1}")
        kitchen1a = input('What should William do? ').lower()
        if kitchen1a == 'a':
            chef.character_interact_informal()
            print(f'\n"Hey William. I am making Chicken Wings. Itll be done soon. Grab a plate and I will get you some". This did not effect Williams preparedness score. Williams current score is {preparescore}. ')
        elif kitchen1a == 'b':
            mom.character_interact_respectful()
            preparescore = preparescore - 1
            print(f'\n"William, dear, arent you supposed to be doing some of your chores? DO YOUR CHORES NOW!" This interaction forced William to continue some of his seemingly infinite amount of chores which has decreased a point from the Prepareness Score. Williams current score is {preparescore}. ')
        elif kitchen1a == 'c':
            fridge.object_interact()
            while brownies_noteaten:
                print('\n"Wow! Theres so much food!" William seems to be quite tempted to get an unhealthy snack like brownies. There are two options:')
                for fridgeoption in fridgeaction:
                    print(f"{fridgeoption}")
                snack_choice = input('What should William do? ').lower()
                if snack_choice == 'a':
                    preparescore = preparescore - 1
                    print(f"\nWilliam grabs the brownies and shoves them down the hatch. His stomach starts to hurt! This interaction has decreased a point from William's Prepareness Score. Williams current score is {preparescore}. ")
                    brownies_noteaten = False
                    brownies_eaten = True
                    break
                elif snack_choice == 'b':
                    print(f"\nWilliam closes the fridge door. This did not effect William's preparedness score. William's current score is {preparescore}. ")
                    break
                else:
                    print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")  
            while brownies_eaten:
                print("\nWilliam feels ill from his unhealthy snack. There is only one option:")
                for fridgeoption2 in fridgeaction2:
                    print(f"{fridgeoption2}")
                snack_choice = input(f'What should William do? ').lower()
                if snack_choice == 'a':
                    print(f"\nWilliam closes the fridge door. This did not effect William's preparedness score. William's current score is {preparescore}. ")
                    break
                else:
                    print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")                
        elif kitchen1a == 'd':
            plate.object_hold()
            print(f'Perhaps now William can get freshly made food.')
            hasplate = True
            noplate = False
        elif kitchen1a == 'e':
            table.object_interact()
            preparescore = preparescore - 1
            print(f"\nWilliam takes a seat at the empty table. His mom who is also seated there starts to talk about her day. She goes on and on but William feels like just leaving would hurt his Mom's feelings, so he stays. This makes him lose his focus on his presentation and has decreased a point from William's Prepareness Score. William's current score is {preparescore}. ")
        elif kitchen1a == 'f':
            print("\nWilliam heads back to the intersection. ")
            break
        else:
            print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")  
    while hasplate:
        print("\n\nWilliam is in the Kitchen. William's Mom is sitting at the dinner table, their family chef is hard at work cooking, theres a plate on the counter, the table has an open seat, and the fridge makes a small murmur. Your options are: ")
        for kitchenoption2 in kitchenaction2:
            print(f"{kitchenoption2}")
        kitchen1a = input('What should William do? ').lower()
        if kitchen1a == 'a':
            while eaten:
                chef.character_interact_informal()
                print(f'"\nHey William. You already ate. I dont have anymore food to give to you." Williams current score is {preparescore}. ')
                break
            while not_eaten:
                preparescore = preparescore + 2
                chef.character_interact_informal()
                print(f"\nHey William. Bring your plate and come get your Chicken Wings. William was very hungry and couldnt focus. The food has replenished his hunger and focus. This has increased 2 points to his Prepareness Score. Williams current score is {preparescore}. ")
                eaten = True
                not_eaten = False
                break          
        elif kitchen1a == 'b':
            preparescore = preparescore - 1
            mom.character_interact_respectful()
            print(f'\n"William, dear, arent you supposed to be done some of your chores? DO YOUR CHORES NOW!" This interaction has decreased a point from Williams Prepareness Score. Williams current score is {preparescore}. ')
        elif kitchen1a == 'c':
            fridge.object_interact()
            while brownies_noteaten:
                print('\n"Wow! Theres so much food!" William seems to be quite tempted to get an unhealthy snack like brownies. There are two options:')
                for fridgeoption in fridgeaction:
                    print(f"{fridgeoption}")
                snack_choice = input('What should William do? ').lower()
                if snack_choice == 'a':
                    preparescore = preparescore - 1
                    print(f"\nWilliam grabs the brownies and shoves them down the hatch. His stomach starts to hurt! This interaction has decreased a point from William's Prepareness Score. Williams current score is {preparescore}. ")
                    brownies_noteaten = False
                    brownies_eaten = True
                    break
                elif snack_choice == 'b':
                    print(f"\nWilliam closes the fridge door. This did not effect William's preparedness score. William's current score is {preparescore}. ")
                    break
                else:
                    print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")  
            while brownies_eaten:
                print("\nWilliam feels ill from his unhealthy snack. There is only one option:")
                for fridgeoption2 in fridgeaction2:
                    print(f"{fridgeoption2}")
                snack_choice = input(f'What should William do? ').lower()
                if snack_choice == 'a':
                    print(f"\nWilliam closes the fridge door. This did not effect William's preparedness score. William's current score is {preparescore}. ")
                    break
                else:
                    print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")       
        elif kitchen1a == 'd':
            preparescore = preparescore - 1
            table.object_interact()
            print(f"\nWilliam takes a seat at the empty table. His mom who is also seated there starts to talk about her day. She goes on and on but William feels like just leaving would hurt his Mom's feelings, so he stays. This makes him lose his focus on his presentation and has decreased a point from William's Prepareness Score. William's current score is {preparescore}. ")
        elif kitchen1a == 'e':
            print("\nWilliam put the plate back and heads back to the intersection. ")
            break
        else:
            print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")  
def livingroomscene():
    print('\nYou have chosen to go to the Living Room.')
    #I had to specify these boolean and 'score' variable as global so they didnt revert back everytime the function was called.
    global notplay 
    global play 
    global wii_on  
    global no_controllers  
    global has_controllers  
    global brushed 
    global not_brushed 
    global first_throw
    global more_throw 
    global preparescore
    while notplay:
        print("\n\nWilliam is in the Living Room. William's Younger Brother, Lucas, and Dog, Bailey, turn their heads to see who entered. They seem excited. The family Wii is turned off and the dog brush and toy is on the ground. Your options are: ") 
        for livingoption1 in livingaction1:
            print(f"{livingoption1}")
        living_activity1 = input('What should William do? ').lower()  
        if living_activity1 == 'a':
            bro.character_interact_informal()
            while no_controllers:
                print('\n"Bro, you promised to play a game with me. Go get a game and keep your promise!"')
                break
            while has_controllers:
                preparescore = preparescore - 1
                print(f'\n"Yay! We get to finally play! I am going to beat you!" Playing with Lucas hasdecreased a point from the Prepareness Score. Williams current score is {preparescore}. After playing William turns the Wii off.')
                notplay = False
                play = True
                break
        elif living_activity1 == 'b':
            while no_controllers:
                print("\nYou have chosen to turn on the Nintendo Wii. Your options are: ")
                for gameoption in gameaction:
                    print(f"{gameoption}")
                gamechoice = input(' What should William do? ').lower()    
                if gamechoice == 'a':
                    preparescore = preparescore - 1
                    print(f"\nYou have chosen to take the controllers for the Wii, You can now play with Lucas. This interaction has decreased a point from William's Prepareness Score. Williams current score is {preparescore}. ")
                    no_controllers = False
                    has_controllers = True
                    wii_on = True
                elif gamechoice == 'b':
                    print("\nYou have chosen to leave without the controllers. You cannot play the Wii without the controllers, so you turn the Wii back off.")
                    break
                else:
                    print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")
            while has_controllers:
                print("\nYou have the controllers and the Wii is turned on. You can now play with Lucas.")
                break
        elif living_activity1 == 'c':
            print('\nWilliam takes a short moment to pet Bailey. Bailey turns his head to stare at you. "Woof!" It seems Bailey might want to either play or get brushed.')
        elif living_activity1 == 'd':
            brush.object_hold()
            while brushed:
                print("\nWilliam, however, has already brushed Bailey. There is no need to brush him again.")
                break            
            while not_brushed:
                preparescore = preparescore - 1
                print(f"\nWilliam brushes out the tangled knots in Bailey's fur. This takes a long time because she hasn't been brushed in forever. Because brushing Bailey takes up so much time, it decreases a point from William's Prepareness Score. Williams current score is {preparescore}. ")
                not_brushed = False
                brushed = True
                break
        elif living_activity1 == 'e':
            while more_throw:
                print("\nBecause William had already thrown the toy around for a while, Bailey seems tired of playing with the Dog Toy and doesn't react when it is thrown.")
                break            
            while first_throw:
                preparescore = preparescore - 1
                print(f"\nWilliam picks up the Dog Toy on the ground and throws it across the room. Bailey runs to go fetch the toy and bring it back to William. After he returns, William decides that he should continue throwing the toy around. Because he uses his time to play with Bailey a point is decreased from William's Prepareness Score. Williams current score is {preparescore}. ")
                first_throw = False
                more_throw = True
                break
        elif living_activity1 == 'f':
            print("\nWilliam heads back to the intersection. ")
            break
        else:
            print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")  
    while play:
        print("\n\nWilliam is in the Living Room. William's Younger Brother, Lucas, and Dog, Bailey, turn their heads to see who entered. They seem excited. The family Wii is turned off and the dog brush and toy is on the ground. Your options are: ") 
        for livingoption2 in livingaction2:
            print(f"{livingoption2}")
        living_activity1 = input('What should William do? ').lower()  
        if living_activity1 == 'a':
            bro.character_interact_informal()
            print('\n"Hey Bro. Thanks for playing with me earlier. Im really tired now. Im not going to play anymore today."')
        elif living_activity1 == 'b':
            print('\nWilliam takes a short moment to pet Bailey. Bailey turns his head to stare at you. "Woof! Woof!" William is not sure of what he wants.')
        elif living_activity1 == 'c':
            while brushed:
                print("\nWilliam has already brushed Bailey. There is no need to brush him again.")   
                break               
            while not_brushed:
                preparescore = preparescore - 1
                print(f"\nWilliam grabs the Dog Brush and brushes out the tangled knots in Bailey's fur. This takes a long time because she hasn't been brushed in forever. Brushing Bailey has decreased a point from William's Prepareness Score. Williams current score is {preparescore}. ")
                not_brushed = False
                brushed = True
                break
        elif living_activity1 == 'd':
            toy.object_hold()
            while more_throw:
                print("\nBecause William had already thrown the toy around for a while, Bailey seems tired of playing with the Dog Toy and doesn't react when it is thrown.")
                break            
            while first_throw:
                preparescore = preparescore - 1
                print(f"\nWilliam throws the toy across the room. Bailey runs to go fetch the toy and bring it back to William. After he returns, William decides that he should continue throwing the toy around. Because he uses his time to play with Bailey a point is decreased from William's Prepareness Score. Williams current score is {preparescore}. ")
                first_throw = False
                more_throw = True
                break
        elif living_activity1 == 'e':
            print("\nWilliam heads back to the intersection. ")
            break
        else:
            print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer: ")  
def studyroomscene():
    print('\nYou have chosen to go to the Study Room.')
    #I had to specify these boolean and 'score' variable as global so they didnt revert back everytime the function was called.
    global angry_dad
    global very_angry_dad
    global first_tutor
    global annoyed_tutor
    global worked_a_little
    global first_time_work
    global preparescore
    while True:
        print("\n\nWilliam is in the Study Room. In the room, William's dad is working hard, the tutor Jerry patiently waits for William to start working, his laptop and phone are on the desk and the counch looks very comfortable. Your options are:")
        for studyoption1 in studyaction1:
            print(f"{studyoption1}")
        studyactivity = input('What should William do? ').lower()
        if studyactivity == 'a':
            dad.character_interact_respectful()
            while very_angry_dad:
                print('\n"WHY ARE YOU STILL TALKING TO ME? NOT ONLY AM I WORKING, BUT YOU SHOULD BE TOO!" This conversation has made William feel even more guilty. This might increase productivity later on.')
                break            
            while angry_dad:
                print('\n"William!! I told you that this presentation is very important. Why are you not working right now?!" This interaction seems to have made William feel guilty. This guilt might increase productivity. ')
                angry_dad = False
                very_angry_dad = True
                break
        elif studyactivity == 'b':
            tutor.character_interact_respectful()
            while annoyed_tutor:
                print('\n"Are you kidding me right now?! Your laptop is right there. Why wont you start working on your presentation?! Stop procrasinating!"')
                break            
            while first_tutor:
                print('\n"Hey William, you should probably start working on your presentation. Thats why I am here after all."')
                first_tutor = False
                annoyed_tutor = True
                break
        elif studyactivity == 'c':
            print("\nWilliam sits down and opens his laptop. There are several options on his laptop. The options are: ")
            for laptopoption in laptopaction:
                print(f"{laptopoption}")    
            laptopoption = input('What should William Do? ').lower()
            if laptopoption == 'a':
                print("\nWilliam pulls up his document and starts to work on preparing for his presentation. While working on his presentation, he starts to run into problems with grammar and structure. The options are:")
                for worksolution in workissue:
                    print(f"{worksolution}") 
                helpoption = input("What should William Do? ").lower()
                while first_time_work:
                    if helpoption == 'a':
                        preparescore = preparescore + 2
                        print(f"\nWilliam asks Tutor Jerry for help. Jerry helps him work through the problems quickly. This has added 2 points to the Preparedness Score. Williams current score is {preparescore}. ")
                        worked_a_little = True
                        first_time_work = False
                    elif helpoption == 'b':
                        preparescore = preparescore + 1
                        print(f"\nWilliam starts to work through the problems alone. He is able to correct his structure and grammar, however, takes a long time to do so. This has added 1 point to the Preparedness Score. Williams current score is {preparescore}. ")
                        worked_a_little = True
                        first_time_work = False
                    else:
                        print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer:")
                        break
                while worked_a_little:
                    if helpoption == 'a':
                        preparescore = preparescore + 2
                        print(f"\nWilliam asks Tutor Jerry for help. Jerry helps him work through the problems quickly. This has added another 2 points to the Preparedness Score. Williams current score is {preparescore}. ")
                        break
                    elif helpoption == 'b':
                        preparescore = preparescore + 1
                        print(f"\nWilliam decides to work through the problems by himself. He is able to correct his structure and grammar, however, takes a long time to do so. This has added 1 point to the Preparedness Score. Williams current score is {preparescore}. ")
                        break
                    else:
                        print("\nYou have entered something that I do not understand. Please re-read the options and re-enter your answer:")
            elif laptopoption == 'b':
                while angry_dad:
                    preparescore = preparescore - 2
                    print(f'\nWilliam opens the application Minecraft. He decides to call some of his friends to play aswell. He plays for a while. This has decreased 2 points from his Preparedness Score. Williams current score is {preparescore}. ')
                    break
                while very_angry_dad:
                    print(f"\nWhile opening the application, William remembers the guilt that he felt while his Dad got mad at him. He decides its best not to get distracted and closes the application.")
                    break
            elif laptopoption == 'c':
                while angry_dad:
                    preparescore = preparescore - 2
                    print(f'\nWilliam opens the website Reddit. He decides to scroll through several sub-reddits. This has decreased 2 points from his Preparedness Score. Williams current score is {preparescore}. ')
                    break
                while very_angry_dad:
                    print(f"\nWhile opening the website, William remembers the guilt that he felt while his Dad got mad at him. He decides its best not to get distracted and exits out of the website.")
                    break
            elif laptopoption == 'd':
                print("\nWilliam closes the laptop.")
            else: 
                print("\nSorry, I do not understand what you entered. William has gone back to the intersection. Please re-read the options and re-enter your answer:")
                break
        elif studyactivity == 'd':
            phone.object_interact()
            while angry_dad:
                preparescore = preparescore - 1
                print(f'\nHe decides to text a bunch of his friends and starts to call with them. This has decreased a point from his Preparedness Score. Williams current score is {preparescore}. ')
                break
            while very_angry_dad:
                print(f"\nIn the middle of texting his friends, William remembers the guilt that he felt while his Dad got mad at him. He decides its best not to get distracted and puts his phone down.")
                break
        elif studyactivity == 'e':
            couch.object_interact()
            while first_time_work:
                preparescore = preparescore - 1
                print(f"\nDespite not being tired from working, William takes some time on the couch. He stays unproductive. This has decreased a point from his Preparedness Score. Williams current score is {preparescore}. ")
                break
            while worked_a_little:
                preparescore = preparescore + 1
                print(f"\nWilliam decides to set an alarm for a short nap on the couch so he doesn't lose his focus. The nap helps his mind reset which adds a point to his Preparedness Score. Williams current score is {preparescore}. ")
                break
        elif studyactivity == 'f':
            print("\nWilliam heads back to the intersection. ")
            break
        else:
            print('\nYou have entered something that I do not understand, please re-enter your answer: ') 
def end():
    print("\nCongraduations! You helped William be fully prepared for his presentation. You went past the massive number of distractions in his house, and helped his prepare mentally and physcially. Thank you for playing the Adventure of Procrastination!")

#Classes
class Character:
    def __init__(self, role, effect):
        self.role = role
        self.effect = effect

    def character_interact_informal(self):
        print(f'''\n"Hey {self.role}! Whatsup?" You have interacted with {self.role}. Theres a chance that this could have a {self.effect} effect on William's Preparedness Score. ''')

    def character_interact_respectful(self):
        print(f'''\n"Hello {self.role}. How are you?" You have interacted with {self.role}. Theres a chance that this could have a {self.effect} effect on William's Preparedness Score. ''')
class Object:
    def __init__(self, thing, thingeffect):
        self.thing = thing
        self.thingeffect = thingeffect

    def object_interact(self):
        print(f"\nYou made William use the {self.thing}. Theres a chance that this could lead to a {self.thingeffect} effect on William's Preparedness Score. ")

    def object_hold(self):
        print(f"\nYou made William pick up the {self.thing}. Theres a chance that this could lead to a {self.thingeffect} effect on William's Preparedness Score.")

#Instances
#Characters
mom = Character('Mom', 'negative')
chef = Character('The Chef', 'positive')

bro = Character('Lucas', 'negative')
dog = Character('Bailey', 'negative')

tutor = Character('Tutor Jerry', 'positive')
dad = Character('Dad', 'positive')

#Objects
fridge = Object('Fridge', 'negative')
plate = Object('Plate', 'positive')
table = Object('Empty seat at the Table', 'negative')

wii = Object('Nintendo Wii', 'negative')
brush = Object('Dog Brush', 'negative')
toy = Object('Dog Toy', 'negative')

laptop = Object('Laptop', 'positive')
couch = Object('Couch', 'negative and positive')
phone = Object('Phone', 'negative')

#Introductory paragraph
print ("""
You are controlling the 17 year old William Smith. William is currently
inside of his uppermiddle class suburban home. He is currently preparing
for the biggest presentation of his life. There are three main 
locations in his home. The first is the kitchen/dining room. Here his mom 
is sat at the dinner table and their family chef is ready to cook. This 
room has a fridge, plate and table. The second is the living room. Here 
his younger brother, Lucas, and dog, Bailey, are both bored out of their minds. 
This room has a Nintendo Wii, dog brush, and the dog toy. The last is the study room. 
Here his tutor, Jerry, is ready to help him and his Dad is hard at his own work. 
This room has a couch and William's Laptop and phone. William has a Preparedness 
Score. He is currently at 4 points. In order for him to be prepared for his 
presentation, he needs at least 10 points and must return to the intersection 
between the rooms. With the distractions all over his house, can you help 
William finish the preparation for his presentation?
""")

#Start of code
while begin:
    if (preparescore >= 10):
        end()
        break
    print("You are standing at the intersection between three rooms: The Kitchen/Dining Room, Living room, and Study room. Where do you want to go?")
    for room in movement:
        print(f"{room}")
    start = input('Where should William go? ').lower()
    if start == 'a':
        kitchen_scene()
    elif start == 'b':
        livingroomscene()
    elif start == 'c':
        studyroomscene()
    else: 
        print('\nYou have entered something that I do not understand, please re-read the options and re-enter your answer.')
