import streamlit as st
import csv

st.write("Enter your Name, Hobbies and Interests")

name = st.text_input("Enter your Name")
interests = st.text_input("Enter 1 of your biggest interests")
hobbies = st.text_input("Enter 1 of your biggest hobbies")
submit = st.button("Submit")

st.write("Find Friends Here!")
interest = st.text_input("Type your interests to search up people with similar interests as you!")
hobby = st.text_input("Type your hobbies to search up people with similar hobbies as you!")
search = st.button("Search")

headersCSV = ['Name','Interests','Hobbies'] 

def save_input():
    dict = {"Name": name, "Interests": interests, "Hobbies": hobbies}

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
                if interest  == row[1] :
                    st.write(f" We have found {row[0]} as a potential friend based on your interests!")
                elif hobby == row[2]:
                    st.write(f" We have found {row[0]} as a potential friend based on your interests!")
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
                
        print(f"processed {line_count} lines.")

