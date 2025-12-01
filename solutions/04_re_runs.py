# ======
# RE RUNS
# ======

'''
OVERVIEW
--------
The most important thing to understand about how Streamlit works is that every
time you interact with a widget in your web app, YOUR ENTIRE PYTHON CODE is 
being run again from top to bottom. That is how streamlit updates what is being
shown. 

That means if you aren't careful, things you are storing in variables will be
overwritten.

HOW CAN YOU PREVENT PROBLEMS WITH THIS?
---------------------------------------
We will go over a good way to fix potential problems with this when we go over
session_state a little later. For now, just understand that streamlit is
rerunning after every interaction.
'''

# 1. UNDERSTANDING HOW STREAMLIT RE RUNS YOUR CODE
# Import streamlit as st and then use st.write()
# anything you put in st.write() like text or variables will appear on your page.
# You can include markdown formatting to do headings.
# For example you can do "# My Page" for large font. You could alternatively
# do st.title("My Page") for the same effect.

import random
import streamlit as st

st.write("# This is a random number")
st.write(f"## {random.randrange(0, 101)}")

st.write("Try interacting with the page and see what happens to the random number")
st.selectbox("Choose anything", ["Chocolate", "Vanilla", "Strawberry", "Neopolitan"])
st.text_input("Enter your favorite food")

st.write("---") # this just adds a line break to your page

# 2. SEE HOW IT OVERWRITES YOUR UPDATES
# Try adding stuff to your grocery list. Do you see the problem whenever you
# try to add something more than once?

grocery_list = []  # resets every rerun

new_item = st.text_input("add something to your grocery list:")
if st.button("Add to list"):
    grocery_list.append(new_item)

st.write("Current Grocery list:", grocery_list)


