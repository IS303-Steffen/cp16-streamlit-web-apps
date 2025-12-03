# =============
# MULTIPAGE APP
# =============

'''
OVERVIEW
--------
Streamlit supports mulitpage apps. You put each page in its own .py file.
The page you run in the terminal will load in the other pages and put them
in a navigation bar.

You can choose to put the navigation bar on the top or side, or hide it.
'''

import streamlit as st


# 1. CREATE PAGES
# You're provided with 2 other pages (10b and 10c). Add them as pages using
# st.Page("file_path.py", title="Your Page Title"). The filepaths should be
# relative to this file (meaning leave out "practice/")

page_1 = st.Page(r"10b_multipage_app.py", title="Home")
page_2 = st.Page(r"10c_multipage_app.py", title="About")


# 2. SETUP NAVIGATION
# Use st.navigation([list, of, pages], position='top') and put the 2 pages you
# created earlier in. Set st.navigation equal to a variable like page then do
# page.run(). Now start streamlit using this page like normal, and you shoul
current_page = st.navigation([page_1, page_2], position='top')

current_page.run()