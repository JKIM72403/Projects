from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
from tkinter import messagebox #I thought it would be pretty cool to have pop-up warnings when an error happens.

# Note: I could've make "widget creation" process into a function and just run it that way but I found it to be quite pointless.
# I would've had to make most of the widget variables "global" and that would increase the total lines of code by a lot.
# I felt like for this project, starting by just having the code run and create the widgets would be better suited.

# Note: Some of the widgets would let me attach a (".grid(column=1, row=0)") to the end of it without any issues.
# However, sometimes I would find that it wouldn't recognize the widget unless I had (".grid(column=1, row=0)") on
# next line down which explains why there is some inconsistency (for anytime I could, I wanted to reduce my lines of code)

#Tuples and empty list to store forloop-created widgets
abilities = [("Water", "Water"), ("Fire", "Fire")]
upbringing_options = [("Poor", "Poor"), ("Rich", "Rich")]
attitude = [("Compassionate", "Compassionate"), ("Mean", "Mean")]
radio = []
saved_data = [] 
setting_options = ["Cake","Ice Cream",]


#Booleans
check = False

#Start of TKinter Layout 
root = Tk()
mainframe = ttk.Frame(root).grid(column=0, row=0)

#Fonts adn Styles
Biggertitlefont = font.Font(family='Helvetica', size=20, weight='bold')
TitleFont = font.Font(family='Helvetica', size=12, weight='bold')
SubheadingFont = font.Font(family='Helvetica', size=10, weight='bold')
normalFont = font.Font(family='Helvetica', size=10)

style = ttk.Style()
style.configure("TFrame", background="White")
style.configure("1.TLabel", background="White")
style.configure("TButton", background="Black")


#Title Labels
titlelabel1 = ttk.Label(mainframe, text = "Story:", font=Biggertitlefont).grid(column=1, row=0, columnspan=3)
titlelabel2 = ttk.Label(mainframe, text = "Please Select Your Story Options:", font=Biggertitlefont).grid(column=0, row=0)

#Creating the Story Frames and their labels
storyframe1 = ttk.Frame(mainframe, borderwidth=5, relief = "ridge", width=400, height= 600).grid(row=1, column=1, rowspan=25, columnspan=1)
label = ttk.Label(storyframe1, text = "Page 1", font=TitleFont, style = "1.TLabel").grid(column=1, row=1)

storyframe2 = ttk.Frame(mainframe, borderwidth=5, relief = "ridge", width=400, height= 600).grid(row=1, column=2, rowspan=25, columnspan=1)
label2 = ttk.Label(storyframe1, text = "Page 2", font=TitleFont, style = "1.TLabel").grid(column=2, row=1)

storyframe3 = ttk.Frame(mainframe, borderwidth=5, relief = "ridge", width=400, height= 600).grid(row=1, column=3, rowspan=25, columnspan=1)
label3 = ttk.Label(storyframe1, text = "Page 3", font=TitleFont, style = "1.TLabel").grid(column=3, row=1)



#Start of Option Widget Creation
#Name options: Entries
hero_name_title = ttk.Label(mainframe, text = "What do you want to call the hero? (Max. 8 characters)", font= SubheadingFont).grid(column=0, row=1)
hename = StringVar()
hero_name = ttk.Entry(mainframe, textvariable = hename, state = NORMAL, font = normalFont)
hero_name.grid(column=0, row=2)

villan_name_title = ttk.Label(mainframe, text = "What do you want to call the villain? (Max. 8 characters)", font= SubheadingFont).grid(column=0, row=3)
villname = StringVar()
villan_name = ttk.Entry(mainframe, textvariable = villname, state = NORMAL, font = normalFont)
villan_name.grid(column=0, row=4)

#Ability Options: RadioButtons
hero_ability = StringVar()
hero_ability.set("Water")
x=int(6)
h_ability_title = ttk.Label(mainframe, text = "What ability does the Hero have?", font= SubheadingFont).grid(column=0, row=5)
for ability, val in abilities:
    abh = ttk.Radiobutton(mainframe, text=ability, variable=hero_ability, value=val, state = NORMAL)
    abh.grid(column=0, row=x)
    radio.append(abh)
    x += int(1)

villan_ability = StringVar()
villan_ability.set("Water")
z=int(9)
v_ability_title = ttk.Label(mainframe, text = "What ability does the Villain have?", font= SubheadingFont).grid(column=0, row=8)
for ability, val in abilities:
    abv = ttk.Radiobutton(mainframe, text=ability, variable=villan_ability, value=val, state = NORMAL)
    abv.grid(column=0, row=z)
    radio.append(abv)
    z += int(1)

#Setting Option: ComboBox
settinglabel = ttk.Label(mainframe, text = "What is your favorite dessert of the options below?", font= SubheadingFont).grid(column=0, row=11)
sett = StringVar()
setting = ttk.Combobox(mainframe, value = setting_options, textvariable=sett, state = "readonly")
setting.current(1)
setting.grid(column=0,row=12)

#Hero Upbringing Option: Radiobutton
hero_upbringing = StringVar()
hero_upbringing.set("Poor")
x=int(14)
h_upbringing_title = ttk.Label(mainframe, text = "How did the hero grow up?", font= SubheadingFont).grid(column=0, row=13)
for upbringing, status in upbringing_options:
    uph = ttk.Radiobutton(mainframe, text=upbringing, variable=hero_upbringing, value=status, state = NORMAL)
    uph.grid(column=0, row=x)
    radio.append(uph)
    x += int(1)

#Attitude/personality Options: Radiobutton
hero_attitude = StringVar()
hero_attitude.set("Compassionate")
j=int(17)
h_attitude_title = ttk.Label(mainframe, text = "What is the Hero's personality?", font= SubheadingFont).grid(column=0, row=16)
for chosen_attitude, personality in attitude:
    atth = ttk.Radiobutton(mainframe, text=chosen_attitude, variable=hero_attitude, value=personality, state = NORMAL)
    atth.grid(column=0, row=j)
    radio.append(atth)
    j += int(1)

villan_attitude = StringVar()
villan_attitude.set("Mean")
y=int(20)
v_attitude_title = ttk.Label(mainframe, text = "What is the Villain's personality?", font= SubheadingFont).grid(column=0, row=19)
for chosen_attitude, personality in attitude:
    attv = ttk.Radiobutton(mainframe, text=chosen_attitude, variable=villan_attitude, value=personality, state = NORMAL)
    attv.grid(column=0, row=y)
    radio.append(attv)
    y += int(1)

#Importing Images and making them into Variables
image_1 = PhotoImage(file="image1.png")
image_2 = PhotoImage(file="image2.png")
image_3 = PhotoImage(file="image3.png")
image_4 = PhotoImage(file="image4.png")
image_5 = PhotoImage(file="image5.png")
image_6 = PhotoImage(file="image6.png")
image_7 = PhotoImage(file="image7.png")
image_8 = PhotoImage(file="image8.png")
image_9 = PhotoImage(file="image9.png")
image_10 = PhotoImage(file="image10.png")
image_11 = PhotoImage(file="image11.png")
image_12 = PhotoImage(file="image12.png")

#Main Story Function
def story():
    tie_w = False
    tie_f = False
    h_win = False
    v_win = False
    global one_1
    global two_1
    global three_1
    global check
    global saved_data

    #This list has to be underneath the created Widgets
    saved_data = [
        hename.get(),  
        villname.get(),  
        hero_ability.get(),  
        villan_ability.get(),   
        sett.get(),  
        hero_upbringing.get(),    
        hero_attitude.get(),     
        villan_attitude.get(), 
        ]

    #Variables that are used in many options (Used to save space and reduce the amount of times I would have to repeat the same text)
    start_story2 = f"One Day, {saved_data[0].title()} walked to his favorite {saved_data[4]} shop \nbut his {saved_data[7]} rival {saved_data[1].title()} wanted the \nshop destroyed."
    sameability = f"{start_story2} Both have the same ability of {saved_data[3]}. \nThey fought but neither could finish the other off."
    diffability = f"{start_story2} {saved_data[0].title()} has the {saved_data[2]} ability \nwhile {saved_data[1].title()} has the {saved_data[3]} ability."

    if saved_data[6] == "Compassionate":
        att1 = ",\nbut you need to be caring for others no matter what"
        att2 = "the importance of caring for"
        if saved_data[7] == "Compassionate":
            att3 = "were \nable to sort out their differences because \nthey cared for each other. They lived in peace."
            if saved_data[5] == "Rich":
                upbringing3 = f"This taught the hero that he needed \nto always workhard and care for the \nless fortunate."
            elif saved_data[5] == "Poor":
                upbringing3 = f"This taught the hero that despite having \nhumble origins, caring for others is important."
        elif saved_data[7] == "Mean":
            att3 = "were \nunable to sort out their different personalities \nbut gained mutual respect for each other and \ndecided to not cause any more conflict."
            if saved_data[5] == "Rich":
                upbringing3 = f"This taught the hero that he needed \nto always workhard and care for the \nless fortunate."
            elif saved_data[5] == "Poor":
                upbringing3 = f"This taught the hero that despite having \nhumble origins, caring for others is important."
    elif saved_data[6] == "Mean":
        att1 = "\nand that survival is the most important thing"
        att2 = "that he was better than"    
        if saved_data[7] == "Compassionate":
            att3 = "were \nunable to sort out their different personalities \nbut gained mutual respect for each other and \ndecided to not cause any more conflict."
            if saved_data[5] == "Poor":
                upbringing3 = f"This taught the hero that life is hard \nand because of that, you need to work your hardest!"
            elif saved_data[5] == "Rich":
                upbringing3 = f"This reaffirmed the hero's belief \nthat he was chosen to be the best."   
        elif saved_data[7] == "Mean":
            att3 = "were \nunable to sort out their differences. \nThey remained enemies forever, unwilling to be compassionate\nto each other."
            if saved_data[5] == "Poor":
                upbringing3 = f"This taught the hero that life is hard \nand because of that, you need to work your hardest!"
            elif saved_data[5] == "Rich":
                upbringing3 = f"This reaffirmed the hero's belief \nthat he was chosen to be the best \nbecause he didnt lose." 
            
    #This variable has to be placed here because it contains the variable "att3" above.
    attitudeimpact3 = f"The {saved_data[6]} hero and {saved_data[7]} villain {att3}"
    
    #Spliting First Story Page by Value of Upbringing option
    if saved_data[5] == "Poor":
        one_1 = ttk.Label(storyframe1, image = image_1, compound= "top", style = "1.TLabel", text= f"There once was a Hero named {saved_data[0].title()} \nwho grew up in the slums of town. \nHe learned that life is hard{att1}.", font=normalFont)
        one_1.grid(column = 1, row = 1, rowspan=30, padx = 50, pady = 50)
        check = True
    elif saved_data[5] == "Rich":
        one_1 = ttk.Label(storyframe1, image = image_2, compound= "top", style = "1.TLabel", text=f"There once was a Hero named {saved_data[0].title()} \nwho grew up with a loving family in the \nweathly part of town. He learned \n{att2} the less fortunate.", font=normalFont)
        one_1.grid(column = 1, row = 1, rowspan=30, padx = 50, pady = 50)
        check = True

    #Splitting Second Story Page by Value of Abilities
    if saved_data[2] == "Water":
        if saved_data[3] == "Water":
            two_1 = ttk.Label(storyframe2, image = image_6, compound= "top", text = f"{sameability}", style = "1.TLabel", font=normalFont)
            two_1.grid(column=2, row=1, rowspan=30, padx = 50, pady = 50)
            tie_w = True
        elif saved_data[3] == "Fire":
            two_1 = ttk.Label(storyframe2, image = image_7, compound= "top", style = "1.TLabel", text = f"{diffability} \nThey fought and because {saved_data[2]}\nbeats {saved_data[3]}, {saved_data[0].title()} won.", font=normalFont)
            two_1.grid(column=2, row=1, rowspan=30, padx = 50, pady = 50)
            h_win = True
    elif saved_data[2] == "Fire":
        if saved_data[3] == "Water":
            two_1 = ttk.Label(storyframe2, image = image_8, compound= "top", style = "1.TLabel",text = f"{diffability} \nThey fought and because {saved_data[3]}\nbeats {saved_data[2]}, {saved_data[0].title()} lost.", font=normalFont)
            two_1.grid(column=2, row=1, rowspan=30, padx = 50, pady = 50)
            v_win = True
        elif saved_data[3] == "Fire":        
            two_1 = ttk.Label(storyframe2, image = image_5, compound= "top", style = "1.TLabel", text = f"{sameability}", font=normalFont)
            two_1.grid(column=2, row=1, rowspan=30, padx = 50, pady = 50)
            tie_f = True

    #Splitting Third Story Page by value of Setting and outcome of the Second Story Page
    if tie_f:
        if saved_data[4] == "Ice Cream":
            three_1 = ttk.Label(storyframe3, image = image_3, compound= "top", style = "1.TLabel", text = f"The {saved_data[4]} shop was \ndestroyed in the fire vs. fire fight. \n{attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50)
        elif saved_data[4] == "Cake":
            three_1 = ttk.Label(storyframe3, image = image_4, compound= "top", style = "1.TLabel", text = f"The {saved_data[4]} shop was \ndestroyed in the fire vs. fire fight. \n{attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50)
    elif tie_w:
        if saved_data[4] == "Ice Cream":
            three_1 = ttk.Label(storyframe3, image = image_9, compound = "top", style = "1.TLabel", text = f"The {saved_data[4]} shop was \nflooded in the water vs. water fight.\nIt, however, was not destroyed. \n{attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50) 
        elif saved_data[4] == "Cake":
            three_1 = ttk.Label(storyframe3, image = image_10, compound = "top", style = "1.TLabel", text = f"The {saved_data[4]} shop was \nflooded in the water vs. water fight.\nIt, however, was not destroyed. \n{attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50)       
    elif h_win:
        if saved_data[4] == "Ice Cream":
            three_1 = ttk.Label(storyframe3, image = image_11, compound="top", style = "1.TLabel", text = f"The {saved_data[4]} shop was not \ndestroyed in the fight. The hero arrested the villain. \n{attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50)
        elif saved_data[4] == "Cake":
            three_1 = ttk.Label(storyframe3, image = image_12, compound="top", style = "1.TLabel", text = f"The {saved_data[4]} shop was not \ndestroyed in the fight. The hero arrested the villain. \n{attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50)
    elif v_win:
        if saved_data[4] == "Ice Cream":
            three_1 = ttk.Label(storyframe3,image = image_11, compound="top", style = "1.TLabel", text = f"The {saved_data[4]} shop was not \ndestroyed in the fight. The villain successfully escaped after \nwinning. {attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50)
        elif saved_data[4] == "Cake":
            three_1 = ttk.Label(storyframe3,image = image_12, compound="top", style = "1.TLabel", text = f"The {saved_data[4]} shop was not \ndestroyed in the fight. The villain successfully escaped after \nwinning. {attitudeimpact3} \n{upbringing3}", font=normalFont)
            three_1.grid(column=3, row=1, rowspan=30, padx = 50, pady = 50) 

#Error pop up Function
def popup():
    answer_error_check = messagebox.showwarning("Something Went Wrong", "You entered something incorrect, please start over and properly fill out the options!")
    submit_button.grid_forget()

#These disable and Enable functions had to include these for loops to DISABLE the radiobuttons created from For loops
def disable():
    global radio
    hero_name["state"] = DISABLED
    villan_name["state"] = DISABLED
    setting['state'] = DISABLED
    for rad in radio:
        rad["state"] = DISABLED
def enable():
    global radio
    hero_name["state"] = NORMAL
    villan_name["state"] = NORMAL
    setting['state'] = "readonly"
    for rad in radio:
        rad["state"] = NORMAL

# The only solution that I found for limiting the Characters in an entry box was through this way.
# I researched a little bit and came up with this method - Thats why it includes *args when we never learned it
def char_limit(*args):
    char_count = hename.get()
    char_count2 = villname.get()
    if len(char_count) >= 9: 
        popup()
        disable()
    elif len(char_count) == 0:
        popup()
        disable()
    elif len(char_count2) >= 9:
        popup()
        disable()
    elif len(char_count2) == 0:
        popup()
        disable()
    else:
        story()
        disable()
        submit_button.grid_forget()

def restart():
    global check
    global saved_data
    if check:
        enable()
        childwidgets = [
            one_1, two_1, three_1,
        ]        
        hero_name.delete(0, "end")
        villan_name.delete(0, "end")
        submit_button.grid(column=0, row=23)
        for widget in childwidgets:
            widget.destroy()
        check = False
    else: 
        enable()
        hero_name.delete(0, "end")
        villan_name.delete(0, "end")
        submit_button.grid(column=0, row=23)
        

# Create Story Button: Had to put it down here because the function/command it uses needs to be above it.
submit_button = ttk.Button(mainframe, text="Create Story", command=char_limit)
submit_button.grid(column=0, row=23)

start_over = ttk.Button(mainframe, text="Start Over", command = restart)
start_over.grid(column=0, row=24)


root.mainloop()
