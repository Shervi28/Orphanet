import streamlit as st

st.write("Enter your Name, Hobbies and Interests")

name = st.text_input("Enter your Name")
interests = st.text_input("Enter 1 of your biggest interests")
hobbies = st.text_input("Enter 1 of your biggest hobbies")

def save_input(x,y,z):
    with open('connect_data.txt', 'a') as f:
        f.write(x)
        f.write(" ")
        f.write(y)
        f.write(" ")
        f.write(z)
        f.write('\n')

submit = st.button("Submit")

if submit:
    save_input(name, interests, hobbies)

with open('connect_data.txt','r') as file:
    for line in file:
        Line = line.strip()
        print(Line)

        for word in Line:
            pass