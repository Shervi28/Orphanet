import streamlit as st
import csv

st.title("Make New Friends!")
st.subheader("Dont have friends? No problem! Find people with the same interests as you!")

st.write("Enter your Name, Hobbies and Interests")

name = st.text_input("Enter your Name")
interests = st.text_input("Enter 1 of your biggest interests")
hobbies = st.text_input("Enter 1 of your biggest hobbies")
email = st.text_input("Enter your email so another person can contact you!")
submit = st.button("Submit")

st.write("Find Friends Here!")
interest = st.text_input("Type your interests to search up people with similar interests as you!")
hobby = st.text_input("Type your hobbies to search up people with similar hobbies as you!")
search = st.button("Search")

headersCSV = ['Name','Email','Interests','Hobbies'] 

def save_input():
    dict = {"Name": name,"Email": email, "Interests": interests, "Hobbies": hobbies}

    with open('data.csv','a', newline='') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=headersCSV)
        dict_object.writerow(dict)



if submit:
    save_input()

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

