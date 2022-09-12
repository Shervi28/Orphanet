import streamlit as st

# A very basic version of a comment section for Orphanet
st.set_page_config(page_title="Chat", page_icon="😎", layout="wide")
st.title("Chat With Others")
st.header("Get to know others like you")

st.write("##")
forum = st.container()
commentBox= st.container()

# Forum Area
with forum:
    forum.subheader("Forum")
    forum.write("Anna")
    forum.write("Hello my name is Anna, nice to meet you George!")

    forum.write("#")

    forum.write("George")
    forum.write("Hi Anna, nice to meet you too.")

st.write("##")

# Generates the user's comment
def createComment(name, data):
    if (len(data) <= 250):
        forum.write("#")
        forum.write(name)
        forum.write(data)
        st.success("Your comment was successfully posted.")

    else:
        st.warning("Comments should be no more than 250 characters.")
        return


# Comment submission form
with commentBox:
    st.markdown("""---""")
    commentBox.subheader("Leave Your Comment Below")
    name = commentBox.text_input("Name")
    comment = commentBox.text_area("Comment", placeholder="Type here")
    submit = commentBox.button("Submit")    

    # Creates the comment the moment the user presses the submit button
    if submit:
        createComment(name, comment)