from tkinter import *
from tkinter import messagebox
import re

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import numpy as np

master = Tk()
master.grid_anchor(anchor=CENTER)

email_pattern = re.compile('^[a-zA-Z0-9.!#$%&\'*+=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')

day_to_index = {
    "Sunday"    : 0,
    "Monday"    : 1,
    "Tuesday"   : 2,
    "Wednesday" : 3,
    "Thursday"  : 4
}

daily_classes = [{}, {}, {}, {}, {}]

def cleanup():
    for i in range(5):
        if(str(i) not in daily_classes[day_to_index[current_day]]):
            daily_classes[day_to_index[current_day]][str(i)] = 'N/A'

current_day = 'Sunday'
current_sec = 'A'

# Email text box
email_label = Label(master, text="Email: ")
email_label.grid(column = 0, row = 0)

email = StringVar()
email_entry = Entry(master, width=15, textvariable=email)
email_entry.grid(column = 1, row = 0)

# Name text box

name_label = Label(master, text = "Name:")
name_label.grid(column = 0, row = 1)

name = StringVar()
name_entered = Entry(master, width=15, textvariable=name)
name_entered.grid(column = 1, row = 1)

# Grade dropdown list
grade_label = Label(master, text = "Grade:")
grade_label.grid(column = 0, row = 2)

grade = 'Grade 8'

def change_grade(value):
    global grade
    grade = value

grade_default = StringVar(master)
grade_default.set('Grade 8')

grade_dropdown = OptionMenu(master, grade_default, 'Grade 8', 'Grade 9', 'Grade 10', command=change_grade)
grade_dropdown.grid(column = 1, row=2)

# Define changing section dropdown list

def change_section(value):
    global current_sec
    current_sec = value

section_label = Label(master, text = "Section:")
section_label.grid(column=0,row=3)

section_default = StringVar(master)
section_default.set("A")

section_dropdown = OptionMenu(master, section_default, "A","B","C","D","E","F","G","ALL", command=change_section)
section_dropdown.grid(column=1, row=3)

# Defining the 5 subject dropdown list

# the labels
first_class_label = Label(master, text = "First class: ")
first_class_label.grid(column = 0, row = 5)
second_class_label = Label(master, text = "Second class: ")
second_class_label.grid(column = 0, row = 6)
third_class_label = Label(master, text = "Third class: ")
third_class_label.grid(column = 0, row = 7)
fourth_class_label = Label(master, text = "Fourth class: ")
fourth_class_label.grid(column = 0, row = 8)
fifth_class_label = Label(master, text = "Fifth class: ")
fifth_class_label.grid(column = 0, row = 9)

# The default text 
first_class_default = StringVar(master)
first_class_default.set("N/A")

second_class_default = StringVar(master)
second_class_default.set("N/A")

third_class_default = StringVar(master)
third_class_default.set("N/A")

fourth_class_default = StringVar(master)
fourth_class_default.set("N/A")

fifth_class_default = StringVar(master)
fifth_class_default.set("N/A")

def change_first_class(value):
    daily_classes[day_to_index[current_day]]['0'] = value
    cleanup()

def change_second_class(value):
    daily_classes[day_to_index[current_day]]['1'] = value
    cleanup()

def change_third_class(value):
    daily_classes[day_to_index[current_day]]['2'] = value
    cleanup()

def change_fourth_class(value):
    daily_classes[day_to_index[current_day]]['3'] = value
    cleanup()

def change_fifth_class(value):
    daily_classes[day_to_index[current_day]]['4'] = value
    cleanup()

# Dropdown list
first_dropdown = OptionMenu(master, first_class_default, "ENGLISH", "BANGLA", "PHYSICS", "CHEMISTRY", "BIOLOGY", "ICT",  "ACCOUNTING", "BUSINESS STUDIES", "ECONOMICS", "GENERAL MATHS", "ADD MATHS", "N/A",  "FRENCH", "AMADS", "COMMERCE", "PE", "Environmental Management", "Pastoral care", "Career counselling", command=change_first_class)
first_dropdown.grid(column = 1, row = 5)

second_dropdown = OptionMenu(master, second_class_default, "ENGLISH", "BANGLA", "PHYSICS", "CHEMISTRY", "BIOLOGY", "ICT", "ACCOUNTING", "BUSINESS STUDIES", "ECONOMICS", "GENERAL MATHS", "ADD MATHS",  "N/A",  "FRENCH", "AMADS", "COMMERCE",  "PE", "Environmental Management", "Pastoral care", "Career counselling", command=change_second_class)
second_dropdown.grid(column = 1, row = 6)

third_dropdown = OptionMenu(master, third_class_default, "ENGLISH", "BANGLA",  "PHYSICS", "CHEMISTRY", "BIOLOGY", "ICT", "ACCOUNTING", "BUSINESS STUDIES", "ECONOMICS",   "GENERAL MATHS", "ADD MATHS",  "N/A",  "FRENCH", "AMADS", "COMMERCE", "PE", "Environmental Management", "Pastoral care", "Career counselling", command=change_third_class)
third_dropdown.grid(column = 1, row = 7)

fourth_dropdown = OptionMenu(master, fourth_class_default, "ENGLISH", "BANGLA",  "PHYSICS", "CHEMISTRY", "BIOLOGY", "ICT", "ACCOUNTING", "BUSINESS STUDIES", "ECONOMICS",   "GENERAL MATHS", "ADD MATHS", "N/A", "FRENCH", "AMADS", "COMMERCE",  "PE", "Environmental Management", "Pastoral care", "Career counselling", command=change_fourth_class)
fourth_dropdown.grid(column = 1, row = 8)

fifth_dropdown = OptionMenu(master, fifth_class_default, "ENGLISH", "BANGLA",  "PHYSICS", "CHEMISTRY", "BIOLOGY", "ICT",  "ACCOUNTING", "BUSINESS STUDIES", "ECONOMICS",    "GENERAL MATHS", "ADD MATHS", "N/A", "FRENCH", "AMADS", "COMMERCE", "PE",  "Environmental Management", "Pastoral care", "Career counselling", command=change_fifth_class)
fifth_dropdown.grid(column = 1, row = 9)


# Define changing day dropdown list

def refresh():
    global first_class_default, second_class_default, third_class_default, fourth_class_default, fifth_class_default
    first_class_default.set('N/A')
    second_class_default.set('N/A')
    third_class_default.set('N/A')
    fourth_class_default.set('N/A')
    fifth_class_default.set('N/A')

def import_settings(dict):
    global first_class_default, second_class_default, third_class_default, fourth_class_default, fifth_class_default
    first_class_default.set(dict['0'])
    second_class_default.set(dict['1'])
    third_class_default.set(dict['2'])
    fourth_class_default.set(dict['3'])
    fifth_class_default.set(dict['4'])


def change_day(value):
    global current_day
    current_day = value
    if (not daily_classes[day_to_index[current_day]]):
        refresh()
    else:
        import_settings(daily_classes[day_to_index[current_day]])
        

day_label = Label(master, text = "Day:")
day_label.grid(column=0,row=4)

day_default = StringVar(master)
day_default.set("Sunday")

day_dropdown = OptionMenu(master, day_default, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", command=change_day)
day_dropdown.grid(column=1,row=4)

def submit_button():
    # check if all the days have been filled in
    if (name.get() == ''):
        messagebox.showinfo('Error', 'Please fill in your name')
        return
    if (email.get() == ''):
        messagebox.showinfo('Error', 'Please fill in your email')
        return
    if (not email_pattern.match(email.get())):
        messagebox.showinfo('Error', 'Invalid email')
        return
    for i in daily_classes:
        if (not i):
            messagebox.showinfo('Error', 'Please fill in your routine for every day')
            return
    excel_sheet = pd.DataFrame({
            'EMAIL': [email.get(),'','','',''],
            'NAME': [name.get(),'','','',''],
            'GRADE': [grade,'','','',''],
            'SECTION': [current_sec,'','','',''],
            'SUNDAY': [daily_classes[day_to_index['Sunday']]['0'],daily_classes[day_to_index['Sunday']]['1'],
                       daily_classes[day_to_index['Sunday']]['2'],daily_classes[day_to_index['Sunday']]['3'],
                       daily_classes[day_to_index['Sunday']]['4']],
            'MONDAY': [daily_classes[day_to_index['Monday']]['0'],daily_classes[day_to_index['Monday']]['1'],
                       daily_classes[day_to_index['Monday']]['2'],daily_classes[day_to_index['Monday']]['3'],
                       daily_classes[day_to_index['Monday']]['4']],
            'TUESDAY': [daily_classes[day_to_index['Tuesday']]['0'],daily_classes[day_to_index['Tuesday']]['1'],
                       daily_classes[day_to_index['Tuesday']]['2'],daily_classes[day_to_index['Tuesday']]['3'],
                       daily_classes[day_to_index['Tuesday']]['4']],
            'WEDNESDAY': [daily_classes[day_to_index['Wednesday']]['0'],daily_classes[day_to_index['Wednesday']]['1'],
                       daily_classes[day_to_index['Wednesday']]['2'],daily_classes[day_to_index['Wednesday']]['3'],
                       daily_classes[day_to_index['Wednesday']]['4']],
            'THURSDAY': [daily_classes[day_to_index['Thursday']]['0'],daily_classes[day_to_index['Thursday']]['1'],
                       daily_classes[day_to_index['Thursday']]['2'],daily_classes[day_to_index['Thursday']]['3'],
                       daily_classes[day_to_index['Thursday']]['4']]
        })
    writer = ExcelWriter('test.xlsx')
    excel_sheet.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    messagebox.showinfo('Done!', 'Your excel sheet has been generated!')
    master.quit()
    return

submit_day_button = Button(master, text="Confirm day's routine", command=submit_button)
submit_day_button.grid(column=0, row=10)

master.mainloop()