import streamlit as st
import pandas as pd



st.set_page_config(layout="wide",page_title="Newsworthy🤖", page_icon="🤖")
st.markdown("""
<style>
body {
    background: #0b2440;
}
</style>
""", unsafe_allow_html=True)

st.title('Newsworthy🤖')
st.write("A newsletter-like service that brings you the latest AI/ML papers and articles.")
st.subheader("Simply just drop your email and receive weekly updates📧")

# Cache the email list
@st.cache_data
def get_email_list():
    return []

# Form to collect email addresses
with st.form(key='email_form'):
    email = st.text_input('Enter your email:')
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    email_list = get_email_list()
    email_list.append(email)
    st.success(f"Thank you! {email} has been added to the mailing list.")


