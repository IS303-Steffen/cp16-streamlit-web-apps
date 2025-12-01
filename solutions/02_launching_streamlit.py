# ===================
# LAUNCHING STREAMLIT
# ===================

'''
OVERVIEW
--------
Up till now, you've been running python code directly in VS Code.
However, with streamlit, we are launching a mini webserver from the terminal,
and that webserver is going to run our python code.

Here are some key concepts that will help you understand:

- Web Server:
    - a program tha listens for requests and sends back web pages. When you run
      streamlit, your own computer is acting as the webserver.

- Localhost:
    - Rather than use an address on the internet, your app will be availabe
      at "localhost", which is just a special address that always points to
      your own computer. So you can't access your web app on the internet (yet).

- Stopping the Server:
    - You'll notice when you start up streamlit, that your terminal be
      continually running (instead of showing your computer name again and 
      waiting for a new command from you). That is because the streamlit
      webserver is now continually running and listening for interactions from
      the web page. To stop it, you can either press CTRL + C (same for Windows
      and Mac) or kill your terminal by clicking the trash icon.

'''

# 1. START UP STREAMLIT
# In your terminal, type:
#   streamlit run name_of_your_python_file.py
# In this case, you are probably in the "practice" folder, so you'll probably
# need to type streamlit run practice/02_launching_streamlit.py
# If you start typing out "p" and then press tab it will complete the name
# of the folder for you, and then if you start typing 02 then tab it will write
# out the rest of the file for you.


import streamlit as st

st.write("# Hello there!")
st.write("You are running this web application from your own computer")

