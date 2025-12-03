# ==============
# MULTIPLE VIEWS
# ==============

'''
OVERVIEW
--------
Often, you will want to display different views, or groups of widgets, depending
on how a user interacts with your page.

Checking on a value in session_state is a great way to do this.

You will also find it useful to use st.rerun() to re run you python code from 
the top, but with the updated value of session_state
'''

# PRACTICE:
# Follow the comments below to show different views within a single page.

import streamlit as st
import peewee as p
import pandas as pd

db = p.SqliteDatabase("movies.db")

class Movie(p.Model):
    movie_id = p.AutoField(primary_key=True)
    title = p.CharField()
    watched = p.BooleanField(default=False)

    class Meta:
        database = db

    def __str__(self): # This is called when you print an object. You can use it on any class, not just peewee
        return self.title

db.connect()
db.create_tables([Movie])

# 1. Check if "current_view" is not in the session state. If it is not, then add
#    it with a value of "main_menu"
pass

st.write("# Movie Manager")

# ==============
# MAIN MENU VIEW
# ==============
# 2. Display the main menu view only if "current_view" equals "main_menu"
if 1 == 1:
    st.write("#### Menu options")
    add_movie = st.button("Add a movie")
    update_watchlist = st.button("Update your watchlist")

    if add_movie:
        # 3.1 If add_movie is clicked, it should update 'current_view' to
        #     'add_movie' and call st.rerun()
        pass

    elif update_watchlist:
        # 3.2 If update_watchlist is clicked, it should update 'current_view' to
        #     'update_watchlist' and call st.rerun()
        pass

    st.write("---") # puts a little a divider in
    watched_movies = pd.DataFrame([m.title for m in Movie.select(Movie.title).where(Movie.watched == True)], columns=["Title"]) # get watched movies in a single column dataframe
    unwatched_movies = pd.DataFrame([m.title for m in Movie.select(Movie.title).where(Movie.watched == False)], columns=["Title"]) # same for unwatched movies
    col_1, col_2 = st.columns(2) # you can place things in columns if you want. This creates 2, but you could create any number of columns
    with col_1: # put anything you want in a specifc column indented from the "with col"
        st.write("##### Unwatched Movies")
        st.write(unwatched_movies)
    with col_2:
        st.write("##### Watched Movies")
        st.write(watched_movies)

# ==============
# ADD MOVIE VIEW
# ==============
# 4. Display the add movie view only if "current_view" equals "add_movie"
elif 1 == 0:
    st.write("# Add a movie to your watchlist")
    with st.form("add_movie"):
        title_input = st.text_input("Movie Title")
        submitted = st.form_submit_button("Add to list")

    if submitted:
        Movie.create(title=title_input)
        # 5. If the form is submitted, update "current_view" to "main_menu" and st.rerun()
        pass

# =====================
# UPDATE WATCHLIST VIEW
# =====================
# 6. Display the watchlist view only if "current_view" equals "update_watchlist"
elif 1 == 0:
    movie_list = list(Movie.select().where(Movie.watched == False))
    with st.form("watchlist"):
        movie_choice = st.selectbox("Choose a movie from watchlist", movie_list, index=None)
        submitted = st.form_submit_button("Mark as watched")

    if submitted:
        if movie_choice:
            movie_choice.watched = True
            movie_choice.save()
        # 7. If the form is submitted, update "current_view" to "main_menu" and st.rerun()
        pass


    


