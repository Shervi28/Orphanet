import streamlit as st
import csv

# Connect Page to help orphans find friends
st.set_page_config(page_title="Connect", page_icon="🥶", layout="wide")
st.title("Make New Friends!")
st.subheader("Dont have friends? No problem! Find people with the same interests as you!")
st.text("Answer some questions below and we'll do the hard work :)")
st.markdown("""---""")

st.write("Enter your Name, Hobbies and Interests")

# Input for user's profile description
name = st.text_input("Enter your name:")
interests = st.text_input("Enter one of your interests:")
hobbies = st.text_input("Enter one of your hobbies:")
email = st.text_input("Enter your email so another person can contact you!")
submit = st.button("Submit")

# Friend finder based on user's profile
st.write("Find Friends Here!")
interest = st.text_input("Type your interests to search up people with similar interests as you!")
hobby = st.text_input("Type your hobbies to search up people with similar hobbies as you!")
search = st.button("Search")

# CSV file to save user info using a dictionary
headersCSV = ['Name','Email','Interests','Hobbies'] 

def save_input():
    dict = {"Name": name,"Email": email, "Interests": interests, "Hobbies": hobbies}

    with open('data.csv','a', newline='') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=headersCSV)
        dict_object.writerow(dict)


# When the button is clicked, call save_input
if submit:
    save_input()

# Helps to search for a potential friend with similar interest as the user
if search:
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("Data")
                line_count +=1
            else:
                if interest  == row[2] :
                    st.write(f" We have found {row[0]} as a potential friend based on your interests! Their email is {row[1]}")
                elif hobby == row[3]:
                    st.write(f" We have found {row[0]} as a potential friend based on your interests! Their email is {row[1]}")
                print(f'\t{row[0]} works in the {row[2]} department, and was born in {row[3]}.')
                line_count += 1
                
        print(f"processed {line_count} lines.")