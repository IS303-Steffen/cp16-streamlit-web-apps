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
    - a program that listens for requests and sends back web pages. When you run
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

      
START UP STREAMLIT
------------------
In your TERMINAL, type:

streamlit run practice/02_launching_streamlit.py

If you start typing out "p" and then press tab it will complete the name
of the folder for you, and then if you start typing "02" then tab it will write
out the rest of the file for you.

or if that doesn't work, try:

python -m streamlit run practice/02_launching_streamlit.py

If you are opening VS code from a different folder though, I recommend just
right clicking each file name and copying and pasting the file path instead.

IS IT ASKING FOR YOUR EMAIL?
----------------------------
If it asks you for your email in the terminal, just press enter/return to skip
it then it won't ask again and it should start working.

'''

import streamlit as st

st.write("# Hello there!")
st.write("You are running this web application from your own computer")
st.write("If you'd like, try editing some of the text here, save the python file, then click rerun in your browser.")

