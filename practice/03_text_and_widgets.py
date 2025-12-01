# ================
# TEXT AND WIDGETS
# ================

'''
OVERVIEW
--------
Most of what you do in streamlit is write text or create widgets. Widgets are
interactive elements on the webpage, like a text box, button, dropdown list,
etc. They are how the user interacts with your code. With Streamlit, making and
getting data from widgets is simple.

Text and widgets will appear on your page in the order that you type them in
your python code.

IMPORTANT! SAVE YOUR PYTHON CODE
--------------------------------
For your changes to display on your web page, you MUST save your python code.
I recommend just using the shortcuts (CTRL + S or CMD + S) but you can also 
go to File > Save every time.
'''

# 1. WRITING
# Import streamlit as st and then use st.write()
# anything you put in st.write() like text or variables will appear on your page.
# You can include markdown formatting to do headings.
# For example you can do "# My Page" for large font. You could alternatively
# do st.title("My Page") for the same effect.


# 2. TEXT INPUT 
# Use st.text_input() to create a text box that accepts input. The first
# parameter is the display text for the text input. If you set it
# equal to a variable, it will store the result of the text input.



# 3. SELECTBOX
# Use st.selectbox. The 1st parameter is the display text. The 2nd parameter
# needs to be a list of options to choose from. Give a it a short list of 
# colors to choose from. Then display the choice afterwards using st.write()


# 4. CHECKBOX
# st.checkbox() will return True or False depending on if it is checked or not.
# Try displaying the result of the Checkbox.



# 5. BUTTON
# st.button() also returns True or False, False by default, but True if it is 
# clicked. Just know that it will flip back to False after being clicked as 
# soon as you interact with anything else.


# 6. DATAFRAME TABLES
# Streamlit works really nicely with pandas dataframes. Using the dataframe
# given you below use st.dataframe() or st.write() to display it. The difference
# between the two is that .dataframe() will give you options for formatting the
# table, but we won't be going over that. Notice that you can sort the columns
# and all within your site. 

import pandas as pd

oscar_data = {
    "Name": [
        "Meryl Streep",
        "Katharine Hepburn",
        "Daniel Day-Lewis",
        "Jack Nicholson",
        "Ingrid Bergman",
        "Frances McDormand",
        "Walt Disney",
        "Denzel Washington",
        "Cate Blanchett",
        "Robert De Niro"
    ],
    "Oscar Wins": [
        3,  # Streep
        4,  # Hepburn
        3,  # Day-Lewis
        3,  # Nicholson
        3,  # Bergman
        3,  # McDormand
        22, # Disney
        2,  # Washington
        2,  # Blanchett
        2   # De Niro
    ]
}

df = pd.DataFrame(oscar_data)


# LOTS OF WIDGETS
# ---------------
# We don't have time to go over all the widgets, but here's a list of the main
# ones people use. Feel free to comment a line out and see what it looks like:

# st.text_input("Text Input")  # A box where the user can type a single line of text.
# st.text_area("Text Area")  # A larger box for typing multiple lines of text.
# st.number_input("Number Input")  # Lets the user enter a number (int or float).
# st.date_input("Date Input")  # Lets the user pick a date from a calendar.
# st.time_input("Time Input")  # Lets the user pick a time of day.
# st.selectbox("Selectbox", ["Option 1", "Option 2", "Option 3"])  # Dropdown menu to choose one option.
# st.multiselect("Multiselect", ["Option A", "Option B", "Option C"])  # Dropdown menu where multiple choices are allowed.
# st.radio("Radio Buttons", ["Choice 1", "Choice 2", "Choice 3"])  # A list of exclusive options where only one can be selected.
# st.checkbox("Checkbox")  # A simple true/false toggle.
# st.slider("Slider", 0, 100)  # A draggable slider for picking a numeric value.
# st.select_slider("Select Slider", options=["Low", "Medium", "High"])  # A slider that lets you choose from preset labels.
# st.button("Button Example")  # A clickable button to trigger an action.
# st.file_uploader("File Uploader")  # Lets the user upload a file.
# st.table({"A": [1, 2], "B": [3, 4]})  # Displays a static table.
# st.dataframe({"A": [1, 2], "B": [3, 4]})  # Displays an interactive, sortable table.
# st.image("https://via.placeholder.com/150")  # Displays an image from a URL or file.
# st.code("print('Hello')", language="python")  # Shows formatted code with syntax highlighting.



