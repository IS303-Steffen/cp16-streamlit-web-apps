# =============
# SESSION STATE
# =============

'''
OVERVIEW
--------
Streamlit provides a way for you to store data across reruns via the
session_state dictionary. It is a special dictionary that allows you to store
anything you want in it like a regular dictionary, but it persists across
reruns.

SYNTAX
------
To access, just use:

    st.session_state

Like any dictionary you can add things to it like:

    st.session_state["new_variable"] = "hello"

Usually, the pattern is to create the variable the first time your code runs
like this:

if "new_variable" not in st.session_state:
    st.session_state["new_variable"] = "hello"

then you can use that variable anywhere else in your code.

'''

# 1. ADDING DATA TO SESSION STATE
# First, run the code below without changing anything. It should be incrementing
# a counter that goes up by one every time the button is pushed. But because
# streamlit reruns everytime the button is pushed, the counter is reset to 0
# each time.
# Instead, create a counter inside of st.session_state. The best way to do that
# is to initialize the counter inside an if statment that only runs the very
# first time. Create the counter, increment it each time the button is pressed,
# and display it with st.write(). 


import streamlit as st

st.write("## Regular variables vs storing in session_state")

# regular python variable. We reset every time we interact with the page.
regular_counter = 0

# Buttons
if st.button("Increment"):
    # This will NOT persist
    regular_counter += 1

st.write("### Regular variable:", regular_counter)