"""
Orphanet is a website created to help other orphans find and connect with other orphans around the world.
This multipage website was made with Python using streamlit and 

Created by Shirvin, Robert, Natasha, and Derin.

"""

# Home.py is the main file that runs when you run the app
import pages
import streamlit as st

st.set_page_config(page_title="Home", page_icon=":joy:", layout="wide")


# Main Function
def main():
    st.title("Home")
    st.subheader("Welcome To Orphanet")


if __name__ == '__main__':
    main()
