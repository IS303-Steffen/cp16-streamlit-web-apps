# will update Soon

import streamlit as st

st.write("## Regular variables vs storing in session_state")
# Regular Python variable (resets every rerun)
if "persistent_counter" not in st.session_state:
    st.session_state["persistent_counter"] = 0 # add a variable the first time

regular_counter = 0

# Buttons
if st.button("Increment both"):
    # This will NOT persist
    regular_counter += 1

    # This WILL persist across reruns
    st.session_state.persistent_counter += 1


st.write("### Regular variable:", regular_counter)
st.write("### Session state variable:", st.session_state.persistent_counter)