"""

Credits to CharleyWargnier and his group that were the original creators of the following code.

You can find the code associated with the following repository URL below
|                                  |                                    |
v                                  v                                    v
https://github.com/streamlit/example-app-commenting


"""
from utils import db
import streamlit as st
from datetime import datetime


# Comment Section

st.set_page_config(page_title="chat", page_icon=":🗣:", layout="wide")

with st.container:
    st.header("Chat With Others")
    st.subheader("Discussion Room")

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


conn = db.connect()
comments = db.collect(conn)

with st.expander("Comments"):

    # Show comments

    st.write("**Comments:**")

    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("Your comment was successfully posted.")

    space(2)

    # Insert comment

    st.write("**Add a comment:**")
    form = st.form("comment")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Add comment")

    if submit:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.insert(conn, [[name, comment, date]])
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()