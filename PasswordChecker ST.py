import streamlit as st
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

##### Progress Bar Logic
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

##### Streamlit GUI
st.set_page_config(page_title="Password Checker")
st.title("Password Checker")

##### Enter Box
enter_pass = st.text_input("Enter your password", type="password")

##### Check Results Button
if st.button("Check your password!"):
    results = password_check(enter_pass)

    # Progress Bar (Streamlit uses 0.0 to 1.0, so we divide your max score of 60)
    bar_progress = check_bar()
    st.progress(bar_progress / 60)

    # Show results
    st.info(results)
