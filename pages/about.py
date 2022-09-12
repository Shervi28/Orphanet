import streamlit as st

# About Us Page
# Info about each member responsible for Orphanet

st.set_page_config(page_title="About Us", page_icon="❓", layout="wide")

st.title("About the Developer")
st.subheader("Meet the team who built Orphanet!")

col1, col2 = st.columns(2)

with col1: 
    st.header("Derin")
    st.image("https://media.giphy.com/media/KjuQizGwJCsgoYdziS/giphy.gif")
    st.caption("Full Name: Derin ")
    st.caption("Age: ")
    st.caption("LinkedIn: ")

with col2: 
    st.header("Shervin")
    st.image("https://media.giphy.com/media/th8uBNfTDvGuVGjKzd/giphy.gif")
    st.caption("Full Name: Shervin Antony")
    st.caption("Age: 14")
    st.caption("LinkedIn: https://www.linkedin.com/in/shervin-antony-08587821a/")

col3, col4 = st.columns(2)

with col3: 
    st.header("Natasha")
    st.image("https://media.giphy.com/media/PFLMyWNd4aa7KXq22C/giphy.gif")
    st.caption("Full Name: Natasha Lukmanto")
    st.caption("Age: 18")
    st.caption("LinkedIn: https://www.linkedin.com/in/natasha-audrey-lukmanto-973555206/")

with col4: 
    st.header("Robert")
    st.image("https://media.giphy.com/media/LYLkPDH7FlQK0aAYR1/giphy.gif")
    st.caption("Full Name: Robert Aguilar")
    st.caption("Age: 22")
    st.caption("LinkedIn: https://www.linkedin.com/in/robertjaguilar/")

st.header("Contact us")
st.text_area("Give us your feedback, suggestions, update requests or anything else!", placeholder="Write it here.")