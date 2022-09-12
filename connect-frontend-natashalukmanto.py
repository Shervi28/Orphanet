import streamlit as st

st.title("Connecting you with the world...")
st.text_input("Searching for your friend?", placeholder="Enter your friend's username here.")
st.subheader("Looking for new friends? Don't worry, we got your back!")
st.text("Answer some questions below and we'll do the hard work :)")

# The Questions
st.selectbox("Pick one ice cream flavor", ("Chocolate", "Vanilla", "Strawberry", "Ew, they all suck"))
st.text_input("What's your hobby?", placeholder="I like walking my dog...")
st.text_input("Who's your favorite disney character?", placeholder="Mickey mouse")
st.multiselect("Pick things that interest you: ", ["Music/Arts", "Science", "Technology", "Business", "Finance", "Books", "Sports", "Adventure", "Family"])
st.text_input("Tell me your favorite song", placeholder="August by Taylor Swift")
st.slider('How much do you like cotton candy', 0, 100, 50)

st.button("I'm done!")
st.header("Finding your best friend...")