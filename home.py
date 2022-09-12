# Home.py is the main file that runs when you run the app
# Created by Shervin, Natasha, Robert, and Derin
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home", page_icon=":joy:", layout="wide")
image = Image.open("pages/logo.jpg")

# Main Function
def main():
    st.title("Home")
    st.subheader("Welcome To Orphanet")
    col1, col2, col3 = st.columns([1,4,1])

    with col1:
        st.write("")

    with col2:
        st.image(image)

    with col3:
        st.write("")

if __name__ == '__main__':
    main()