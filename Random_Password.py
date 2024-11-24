import random
import string
import streamlit as st

def generate_password(length):
    """
    Generates a random password of the specified length.
    """
    if length <= 0:
        st.error("Please enter a valid password length.")
        return None

    # Define character set for the password
    char_set = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    return ''.join(random.choice(char_set) for _ in range(length))


# Streamlit Interface
st.title("Random Password Generator")
st.markdown("Generate a secure and random password quickly.")

# Input for Password Length
password_length = st.number_input("Password Length:", min_value=1, step=1)

# Button to Generate Password
if st.button("Generate Password"):
    if password_length <= 0:
        st.error("Please enter a valid password length.")
    else:
        password = generate_password(password_length)
        if password:
            st.success("Password generated successfully!")
            st.text_input("Your Password:", value=password, disabled=True)
