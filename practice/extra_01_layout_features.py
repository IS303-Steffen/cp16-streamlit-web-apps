# ===============
# LAYOUT FEATURES
# ===============

'''
OVERVIEW
--------
You can arrange content in other ways with Streamlit, but we don't have time
to cover them all. Here are some examples of:
    - Wide view
    - the sidebar
    - columns
    - tabs
    - expanders
    - dialogs
'''

import streamlit as st

# ================
# WIDE LAYOUT VIEW
# ================
# You can set things to be more spreadout by setting layout to "wide" in
# .set_page_config
st.set_page_config(page_title="Layout Examples", layout="wide")

# =======
# SIDEBAR
# =======
# Widgets inside st.sidebar appear on the left side of the page.
with st.sidebar:
    st.title("Sidebar Example")
    sidebar_name = st.text_input("Your name")
    sidebar_choice = st.selectbox("Option", ["A", "B", "C"])


# =======
# COLUMNS
# =======
# Columns allow horizontal layout on the page.
st.header("Columns")
col1, col2, col3 = st.columns(3) # returns a list of columns, so just unpack them.

with col1:
    st.write("Column 1")
    st.number_input("Value 1", value=0)

with col2:
    st.write("Column 2")
    st.number_input("Value 2", value=0)

with col3:
    st.write("Column 3")
    st.button("Button")


# ====
# TABS
# ====
# Tabs group related content into separate sections.
st.header("Tabs")

tab1, tab2 = st.tabs(["Summary", "Details"])

with tab1:
    st.write("Summary information")

with tab2:
    st.write("More detailed information")


# =========
# EXPANDERS
# =========
# Expanders hide content until a user expands them.
st.header("Expander")

with st.expander("Show more"):
    st.write("This content is inside an expander.")


# ======
# DIALOG
# ======
# st.dialog() creates a modal dialog window.
st.header("Dialog")

@st.dialog("Example Dialog")
def my_dialog():
    st.write("This is a dialog window.")
    st.text_input("Enter something")
    if st.button("Close"):
        st.rerun()

if st.button("Open Dialog"):
    my_dialog()