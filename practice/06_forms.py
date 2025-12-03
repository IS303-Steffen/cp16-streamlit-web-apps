# =====
# FORMS
# =====

'''
OVERVIEW
--------
Forms are a way to group a set of widgets together. When using a form, streamlit
will NOT rerun your python code after interacting with a widget inside the form.
Instead, it will only rerun once the form submit button has been pushed.

This is useful when you have a set of inputs and you only want the script to 
rerun once you've collected everything you need.

SYNTAX
------

with st.form("example_form"):
    name = st.text_input("Enter your name")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(name)

'''


import streamlit as st
st.write("# Forms practice")

# 1. CREATE A FORM
# Create a form that collects a name (using text_input()) and a birthday (using
# date_input()). Then your form should have a form_submit_button() (every form
# must have one). If the form is submitted it should say "x's birthday is on x"

