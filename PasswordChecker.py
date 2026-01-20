import tkinter as tk
from tkinter import ttk
from collections import Counter 

##### Password Checker
def password_check(password):
    global has_uppercase, has_lowercase, has_symbols, has_numbers, is_unique, passlength
    #####   Allowed symbols
    symbols = "!@#$%&"
    #####   Strong Password Conditions
    has_uppercase = False
    has_lowercase = False
    has_symbols = False
    has_numbers = False
    is_unique = False
    passlength = False
    #####   Password length check
    if len(password) == 0:
        return "Blank Password!"
    elif len(password) < 12:
            return "Please enter a longer password, minimum 12 characters."
    else:
         passlength = True
    #####   Check for too many repeating characters
    count = Counter(password)
    if len(count) >= 5 and max(count.values()) <=3:
         is_unique = True
    else:
         is_unique = False
    ##### Other Conditions Check
    for char in password:
        if char.isupper(): 
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
             has_numbers = True
        if char in symbols:
                has_symbols = True
    ##### Final Check
    if has_uppercase and has_lowercase and has_symbols and has_numbers and is_unique:
         return "Good Password!"
    elif has_uppercase != True:
         return "Add uppercase characters."
    elif has_lowercase != True:
         return "Add lowercase characters."
    elif has_numbers != True:
         return "Add numbers."
    elif is_unique != True:
         return "Too many repeating characters."
    else:
         return f"Add symbols such as {symbols}"
    
#########

##### Tkinter GUI
main = tk.Tk()
main.configure(bg="grey")                               #   Background Colour
main.title("Password Checker")                          #   Window Title
main.geometry("1500x800")                               #   Size of main window
##### Enter Box                                             
enter_pass = tk.Entry(main, width=35)                   #   Textbox for putting in the password
enter_pass.place(x=679, y=400, anchor="center") 
enter_pass.focus()        
##### Show results
results_show = tk.Label(main, text="", bg="white", fg="black", width=50, height=3)      #   Box for showing password results
results_show.place(x=750, y = 500, anchor="center")                                     
##### Function for button click
def click():
    password_x = enter_pass.get()
    results = password_check(password_x)
    results_show.config(text=results)
    bar_progress = check_bar()
    pass_bar["value"] = bar_progress
    

##### Progress Bar
def check_bar():
    tscore = 0
    if passlength:
         tscore += 10
    if has_uppercase:
          tscore += 10
    if has_lowercase:
          tscore += 10
    if has_symbols:
         tscore += 10
    if has_numbers:
         tscore += 10
    if is_unique:
         tscore += 10
    return (tscore)

pass_bar = ttk.Progressbar(main, length= 350, maximum=60)
pass_bar.place(x=750, y=200, anchor="center")
##### Check Results Button
get_results = tk.Button(main, text="Check your password!", command=click)
get_results.place(x=864, y=400, anchor="center")
main.mainloop()
