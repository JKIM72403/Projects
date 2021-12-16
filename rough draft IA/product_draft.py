# I imported a lot of modules/functions. I am still working on the functionality of the program. So in the final draft, this will be simplified to only the modules that I need. 
# But for now, while I am still trying to make the program work, not all the modules imported are necessary.

#IMPORTANT: I did not really focus on the design of the GUI. I only focused on making it work. The final draft will be designed more throughly.
from tkinter import *
import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk
from tkinter import messagebox #I thought it would be pretty cool to have pop-up warnings when an error happens.
import pandas as pd
from tkinter import filedialog
import random
import itertools
import operator 
from operator import itemgetter
from itertools import groupby
from itertools import chain


root = Tk()
mainframe = ttk.Frame(root).grid(column=0, row=0)

#Fonts and Styles
Biggertitlefont = font.Font(family='Helvetica', size=20, weight='bold')
TitleFont = font.Font(family='Helvetica', size=12, weight='bold')
SubheadingFont = font.Font(family='Helvetica', size=10, weight='bold')
normalFont = font.Font(family='Helvetica', size=10)

style = ttk.Style()
style.configure("TFrame", background="White")
style.configure("1.TLabel", background="White")
style.configure("TButton", background="Black")

#I set the index column to the number assigned to the student. I did not set it to the first name because there could be multiple of the same first name
df = pd.read_csv("studentdata.csv", index_col = "number")

#Created lists for destroying widgets and creating radio buttons
child_widgets = []
radio = []
group_choices = [("Random", "Random"), ("Sex", "Sex"), ("Major", "Major")]

#Variables
incorrect_pass = True  
need_to_set_weights = True
first_time = True
set_assignment_number = IntVar()
group_sort = StringVar()
toggle_pass = IntVar()
toggle_pass == 0
num = IntVar()
start = True
to_delete = 0

#Starting Frame
Home_frame = ttk.Frame(mainframe, borderwidth=5, relief = "ridge", width=1000, height= 500).grid(row=1, column=1, rowspan=25, columnspan=15)

#Function to inform of the incomplete parts (regarding the password) of the program 
def wrong_incomplete_password():
    answer_error_check = messagebox.showwarning("Wrong Password.", "The password is currently set to '123'. This message will be changed in the final draft. I plan to let the client choose the password as well.")

#Function to destroy all widgets 
def destroy():
    global child_widgets 
    for widgets in child_widgets:
        widgets.destroy()
    child_widgets *= 0

#Start/password function
def screen1():
    screen1_widgets = []
    global child_widgets
    global incorrect_pass

    enteredpassword = StringVar()
#functions to check if the password is correct and to show *** instead of letters
    def toggle_password():
        if Password.cget('show') == '':
            Password.config(show='*')
            show_password.config(text='Show Password')
        else:
            Password.config(show='')
            show_password.config(text='Hide Password') 

    def passcheck():  
        password = "123" 
        verify = enteredpassword.get()
        if verify == password:
            child_widgets.extend(screen1_widgets)
            destroy()
            homescreen()
        else:
            wrong_incomplete_password()
    
    label1 = ttk.Label(Home_frame, text = "Teacher's Aid", font=Biggertitlefont, style = "1.TLabel")
    label1.grid(column=8, row=1)
    screen1_widgets.append(label1)

    label2 = ttk.Label(Home_frame, text = "Welcome! Please enter your password.", font=TitleFont, style = "1.TLabel")
    label2.grid(column=8, row=2)
    screen1_widgets.append(label2)

    Password = ttk.Entry(mainframe, textvariable= enteredpassword, show='*', font = normalFont)
    Password.grid(column=8, row=7)
    screen1_widgets.append(Password)

    show_password = ttk.Button(mainframe, text='Show Password', width=15, command=toggle_password)
    show_password.grid(column=9, row=7)
    screen1_widgets.append(show_password)

    enter_pass = ttk.Button(mainframe, text='Enter Password', width=15, command = passcheck)
    enter_pass.grid(column=8, row=8)
    screen1_widgets.append(enter_pass)

#This function is one of the main buttons for the user to navigate through the GUI by destroying and returning the user to the home screen
def backbutton():
    destroy() 
    homescreen()

#Start of main 'page' functions
def homescreen(): 
    homescreen_widgets = []
    global to_delete
    global child_widgets
    global need_to_set_weights
    global first_time
    global set_assignment_number
    student_search_name = StringVar()

#The first function will remain in the final draft, but the second is only for the rough (to inform about incomplete functions)
    def popup():
        answer_error_check = messagebox.showwarning("Something Went Wrong", "You entered something incorrect, please start over and properly fill out the options!")
    def popup_incomplete():
        answer_error_check = messagebox.showwarning("This feature is not available yet :(", "This function is incomplete and will be completed with the final draft. ")        

#Student Data page
    def student_data_frame():
        destroy() 
        def edit_student_data_function(): 
            popup_incomplete()

            #This function is incomplete/a work in progress. Please ignore this. This will be used to verify if the student is serached, so that the student's data can be edited
            def check_name_in_file():
                searched_student = (df[df["first"] == student_search_name.get()])

                sdlabel2 = ttk.Label(Home_frame, text = f"Name: {searched_student}", style = "1.TLabel")
                sdlabel2.grid(column=8, row=10)
                homescreen_widgets.append(sdlabel2)

                what_to_change = ttk.Radiobutton(mainframe, text='W', width=15, command = check_name_in_file)
                what_to_change.grid(column=8, row=8)
                homescreen_widgets.append(what_to_change)

        sdlabel1 = ttk.Label(Home_frame, text = "Your Current Students' Data", font=Biggertitlefont, style = "1.TLabel")
        sdlabel1.grid(column=8, row=1)
        homescreen_widgets.append(sdlabel1)

        sdlabel2 = ttk.Label(Home_frame, text = f"You currently have {len(df.index)} Students", font=TitleFont, style = "1.TLabel")
        sdlabel2.grid(column=8, row=2)
        homescreen_widgets.append(sdlabel2)

        edit_student_data = ttk.Button(mainframe, text='Edit Student Data', width=15,  command = edit_student_data_function)
        edit_student_data.grid(column=7, row=4)
        homescreen_widgets.append(edit_student_data)

        go_back = ttk.Button(mainframe, text='Go Back', width=15, command = backbutton)
        go_back.grid(column=7, row=6)
        homescreen_widgets.append(go_back)

        enter_student_data = ttk.Button(mainframe, text='Input Data', width=15, command = popup_incomplete)
        enter_student_data.grid(column=9, row=6)
        homescreen_widgets.append(enter_student_data)

        child_widgets.extend(homescreen_widgets)
    def group_generation_frame():
        destroy() 
        #Rough draft function for explaining why the program prints groups in list form/in brakcets. Will be changed in final draft.
        def brackets(): 
            answer_error_check = messagebox.showwarning("Please be Wary", "Generated groups will not be printed in the correct format. They will be shown in brackets which will be changed in the final draft. ") 
        def generate_student_group(): 
#I was not able to do entrybox validation -- was not able to get it done on time (only letting integers be typed in the box). I will add this feature in the final draft. Thus, typing any other value like a letter or a symbol will result in a ValueError.
            global radio
            generate_groups["state"] = DISABLED
            if len(group_numbers.get()) == 0:
                popup()  
            elif group_numbers.get() == '0': 
                popup()
            else:         
                list_of_names = df['first'].to_list() 

                num_of_students = len(list_of_names)
                int_num_of_students = int(num_of_students) + 1

                num = number_of_students_chosen.get()
                
                int_answer = int(num)
#The processes for these if elif else statements are explained in Criteria C. I think there is a more elegant way to acomplish the same thing, but this was the method I thought of.
                if group_sort.get() == "Random":
                    random.shuffle(list_of_names)
                    grouped_student = [list_of_names[i:i+int_answer] for i in range(0, len(list_of_names), int_answer)]
                    brackets()
                    gglabel4 = ttk.Label(Home_frame, text = f"Your groups are generated: {grouped_student}", style = "1.TLabel")
                    gglabel4.grid(column=1, row=10, columnspan=15)
                    homescreen_widgets.append(gglabel4)

                    child_widgets.extend(homescreen_widgets)
                elif group_sort.get() == "Sex":   
                    list_of_sex = df['sex'].to_list()
                    tuplelist = list(zip(list_of_names, list_of_sex))

                    random.shuffle(tuplelist)
                    tuplelist.sort(key=itemgetter(1))

                    sorted_sex = [[x for x,y in g]
                        for k,g in groupby(tuplelist,key=itemgetter(1))]

                    females = df[df['sex'] == 'f']
                    total_female = (len(females))
                    int_female = int(total_female) 
                    
                    organized_list = (list(chain.from_iterable(sorted_sex))) 
    
                    del organized_list[int_female:int_num_of_students]

                    male_organized_list = (list(chain.from_iterable(sorted_sex))) 
                    del male_organized_list[0:int_female]

                    grouped_female_students = [organized_list[i:i+int_answer] for i in range(0, len(organized_list), int_answer)]
                    grouped_male_students = [male_organized_list[i:i+int_answer] for i in range(0, len(male_organized_list), int_answer)]
                    brackets()
                    gglabel4 = ttk.Label(Home_frame, text = f"Your groups are generated: {grouped_female_students}", style = "1.TLabel")
                    gglabel4.grid(column=1, row=10, columnspan=15)
                    homescreen_widgets.append(gglabel4)

                    gglabel5 = ttk.Label(Home_frame, text = f"Your groups are generated: {grouped_male_students}", style = "1.TLabel")
                    gglabel5.grid(column=1, row=11, columnspan=15)
                    homescreen_widgets.append(gglabel5)

                    child_widgets.extend(homescreen_widgets)
                else: # because there is no need for another elif -- the radiobuttons only have 3 options
#Regarding the Majors: The majors in the .CSV file are Math and English. These will most likely be changed to "Major1" and "Major2" in the final draft.
                    list_of_major = df['major'].to_list()

                    tuplelist_major = list(zip(list_of_names, list_of_major))

                    random.shuffle(tuplelist_major)
                    tuplelist_major.sort(key=itemgetter(1))

                    sorted_major = [[x for x,y in g]
                        for k,g in groupby(tuplelist_major,key=itemgetter(1))]
                    sorted_major.reverse()  #After sorting the list, the groupby function put the 'math' majors after the 'english' majors. The program is designed for the math majors to be sorted in front of the english majors, so I needed to reverse the list.

                    math = df[df['major'] == 'math']
                    total_math = (len(math))
                    int_math = int(total_math)
                    
                    organized_math_major_list = (list(chain.from_iterable(sorted_major))) 
                    del organized_math_major_list[int_math:int_num_of_students]

                    organized_english_major_list = (list(chain.from_iterable(sorted_major))) 
                    del organized_english_major_list[0:int_math]
               
                    grouped_math_students = [organized_math_major_list[i:i+int_answer] for i in range(0, len(organized_math_major_list), int_answer)]
                    grouped_english_students = [organized_english_major_list[i:i+int_answer] for i in range(0, len(organized_english_major_list), int_answer)]
                    brackets()
                    gglabel4 = ttk.Label(Home_frame, text = f"Your math groups are generated: {grouped_math_students}", style = "1.TLabel")
                    gglabel4.grid(column=1, row=10, columnspan=15)
                    homescreen_widgets.append(gglabel4)

                    gglabel5 = ttk.Label(Home_frame, text = f"Your english groups are generated: {grouped_english_students}", style = "1.TLabel")
                    gglabel5.grid(column=1, row=11, columnspan=15)
                    homescreen_widgets.append(gglabel5)

                    child_widgets.extend(homescreen_widgets)
#Setting variables and lists to random, and creating the 'page' widgets:
        group_sort.set("Random")
        number_of_students_chosen = StringVar()

        gglabel1 = ttk.Label(Home_frame, text = "Group Generation", font=Biggertitlefont, style = "1.TLabel")
        gglabel1.grid(column=8, row=1)
        homescreen_widgets.append(gglabel1)

        gglabel2 = ttk.Label(Home_frame, text = "Please select how you want the groups to be made.", font=TitleFont, style = "1.TLabel")
        gglabel2.grid(column=8, row=2)
        homescreen_widgets.append(gglabel2)

        gglabel7 = ttk.Label(Home_frame, text = "Catagories", font=TitleFont, style = "1.TLabel")
        gglabel7.grid(column=6, row=3, columnspan=3)
        homescreen_widgets.append(gglabel7)

        x=int(4)
        for catagory, chosen_catagory in group_choices:
            ggradio = ttk.Radiobutton(mainframe, text=catagory, variable=group_sort, value=chosen_catagory, state = NORMAL)
            ggradio.grid(column=6, row=x, columnspan=3)
            x += int(1)
            radio.append(ggradio)
            homescreen_widgets.append(ggradio)
        for rad in radio:
            homescreen_widgets.append(rad)

        gglabel3 = ttk.Label(Home_frame, text = "Number of students:", font=TitleFont, style = "1.TLabel")
        gglabel3.grid(column=8, row=3, columnspan=3)
        homescreen_widgets.append(gglabel3)

        group_numbers = ttk.Entry(mainframe, textvariable= number_of_students_chosen, font = normalFont, state= NORMAL)
        group_numbers.grid(column=8, row=4, columnspan=3)
        homescreen_widgets.append(group_numbers)

        go_back = ttk.Button(mainframe, text='Go Back', width=15, command = backbutton)
        go_back.grid(column=7, row=7)
        homescreen_widgets.append(go_back)

        generate_groups = ttk.Button(mainframe, text='Generate Groups', width=15, command = generate_student_group, state = NORMAL)
        generate_groups.grid(column=9, row=7)
        homescreen_widgets.append(generate_groups)

        child_widgets.extend(homescreen_widgets)

    def predicted_grade_frame(): # ALL THE CODE IN THIS FUNCTION IS A 'WORK IN PROGRESS'. THERE IS NO FUNCTIONALITY.
        destroy()
        num_of_columns = len(df.columns)
        num_of_assignments = num_of_columns - 7
        int_num_of_assignments = int(num_of_assignments)
       
        pglabel1 = ttk.Label(Home_frame, text = "Predicted Grade Calculation", font=Biggertitlefont, style = "1.TLabel")
        pglabel1.grid(column=1, row=1, columnspan=15)
        homescreen_widgets.append(pglabel1)
        pglabelcap = ttk.Label(Home_frame, text = "Number of Assignments", font=TitleFont, style = "1.TLabel")
        pglabelcap.grid(column=6, row=4)
        homescreen_widgets.append(pglabelcap)

        pglabelcap2 = ttk.Label(Home_frame, text = "Weightage (%)", font=TitleFont, style = "1.TLabel")
        pglabelcap2.grid(column=9, row=4)
        homescreen_widgets.append(pglabelcap2)
        y = int(1)
        x=int(5)
        for z in range(int_num_of_assignments):
            pglabel6 = ttk.Label(Home_frame, text = f"{y}", font=TitleFont, style = "1.TLabel")
            pglabel6.grid(column=6, row=x)

            pgentry = ttk.Entry(mainframe, font = normalFont)
            pgentry.grid(column=9, row=x)
            y += int(1)
            x += int(1)
            homescreen_widgets.append(pglabel6)
            homescreen_widgets.append(pgentry)

        if need_to_set_weights == True:
            pglabel2 = ttk.Label(Home_frame, text = f"You need to set the grade weights of your assignments to continue. You currently have {int_num_of_assignments} assignments", font=TitleFont, style = "1.TLabel")
            pglabel2.grid(column=1, row=2, columnspan=15)
            homescreen_widgets.append(pglabel2)

            go_back = ttk.Button(mainframe, text='Go Back', width=15, command = backbutton)
            go_back.grid(column=2, row=20)
            homescreen_widgets.append(go_back)

#Command will be made later
            confirm_assignment_num =  ttk.Button(mainframe, text='Confirm?', width=15, command = popup_incomplete)
            confirm_assignment_num.grid(column=14, row=20)
            homescreen_widgets.append(confirm_assignment_num)

            child_widgets.extend(homescreen_widgets)
        elif need_to_set_weights == False: 
            pglabel2 = ttk.Label(Home_frame, text = "You can check your student's predicted grade or change the weightages", font=TitleFont, style = "1.TLabel")
            pglabel2.grid(column=1, row=2, columnspan=15)
            homescreen_widgets.append(pglabel2)

            go_back = ttk.Button(mainframe, text='Go Back', width=15, command = backbutton)
            go_back.grid(column=2, row=20)
            homescreen_widgets.append(go_back)
            
            #Command will be made later
            confirm_assignment_num =  ttk.Button(mainframe, text='Confirm?', width=15)
            confirm_assignment_num.grid(column=3, row=20)
            homescreen_widgets.append(confirm_assignment_num)

            child_widgets.extend(homescreen_widgets)

    def attendance_tracker_frame(): # ALL THE CODE IN THIS FUNCTION IS A 'WORK IN PROGRESS'. THERE IS NO FUNCTIONALITY.
        destroy() 
        atlabel1 = ttk.Label(Home_frame, text = "Attendance Tracker", font=Biggertitlefont, style = "1.TLabel")
        atlabel1.grid(column=1, row=1, columnspan=15)
        homescreen_widgets.append(atlabel1)

        atlabel2 = ttk.Label(Home_frame, text = "Please fill in the 'concerning' percentage of attendance. This will show you all your students who have a conerning percentage. \nIf you wish to see the details of one student, please confirm their name.", font=TitleFont, style = "1.TLabel")
        atlabel2.grid(column=1, row=2, columnspan=15)
        homescreen_widgets.append(atlabel2)

        atlabel3 = ttk.Label(Home_frame, text = "Concerning level (%):", font=TitleFont, style = "1.TLabel")
        atlabel3.grid(column=1, row=3, columnspan=10)
        homescreen_widgets.append(atlabel3)

        conern_level = ttk.Entry(Home_frame, font = normalFont, state= NORMAL)
        conern_level.grid(column=5, row=3, columnspan=10)
        homescreen_widgets.append(conern_level)
#Command will be made later
        confirm_percentage = ttk.Button(mainframe, text='Confirm?', width=15, command = popup_incomplete)
        confirm_percentage.grid(column=9, row=3, columnspan=10)
        homescreen_widgets.append(confirm_percentage)

        name_combobox = df["first"].tolist()
        combobox_name = ttk.Combobox(Home_frame, value = name_combobox, state= "readonly")
        combobox_name.grid(column=1, row=4, columnspan=10)
        homescreen_widgets.append(combobox_name)
#Proper Command will be made later
        search_student = ttk.Button(mainframe, text='Search Student', width=15, command = popup_incomplete)
        search_student.grid(column=5, row=4, columnspan=10)
        homescreen_widgets.append(search_student)

        go_back = ttk.Button(mainframe, text='Go Back', width=15, command = backbutton)
        go_back.grid(column=2, row=20)
        homescreen_widgets.append(go_back)

        child_widgets.extend(homescreen_widgets)
#Home Screen widgets
    hlabel1 = ttk.Label(Home_frame, text = "Teacher's Aid Homepage", font=Biggertitlefont, style = "1.TLabel")
    hlabel1.grid(column=8, row=1)
    homescreen_widgets.append(hlabel1)

    hlabel2 = ttk.Label(Home_frame, text = "Please select the section you would like to go", font=TitleFont, style = "1.TLabel")
    hlabel2.grid(column=8, row=2)
    homescreen_widgets.append(hlabel2)

    student_data = ttk.Button(mainframe, text='Student Data', width=15,  command = student_data_frame)
    student_data.grid(column=7, row=4)
    homescreen_widgets.append(student_data)

    group_generation = ttk.Button(mainframe, text='Group Generation', width=15, command = group_generation_frame)
    group_generation.grid(column=9, row=4)
    homescreen_widgets.append(group_generation)

    predicted_grade = ttk.Button(mainframe, text='Predicted Grades', width=15, command = predicted_grade_frame)
    predicted_grade.grid(column=7, row=6)
    homescreen_widgets.append(predicted_grade)

    attendance_tracker = ttk.Button(mainframe, text='Attendence Warning', width=15, command = attendance_tracker_frame)
    attendance_tracker.grid(column=9, row=6)
    homescreen_widgets.append(attendance_tracker)

    child_widgets.extend(homescreen_widgets)

#Start of the program
screen1()

root.mainloop()