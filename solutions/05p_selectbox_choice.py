# ==========================
# PRACTICE: SELECTBOX CHOICE
# ==========================


# 1. PRACTICE
'''
Create a simple streamlit app.

1. Your app should have some large title text.

2. Then, it should allow the user to choose which they like more: Dogs or Cats

3. If they choose Dogs, it should then display a message about how superior dogs
   are. If they choose Cats, it should display a message about how superior cats
   are.

Note: If you are using a selectbox, if you set the index to None then neither of
      the two options will be selected when your app starts.
'''

import streamlit as st

st.write("# Make your choice!")

choice = st.selectbox("Do you prefer dogs or cats?", ["Dogs", "Cats"], index=None)

if choice == "Dogs":
    st.write("You are correct, dogs are superior!")
elif choice == "Cats":
    st.write("You are correct, cats are superior!")