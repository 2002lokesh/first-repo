import streamlit as st
import psycopg2

# Database connection parameters
DB_NAME = "sample"
DB_USER = "openpg"
DB_PASSWORD = "openpgpwd"
DB_HOST = "localhost"
DB_PORT = "5432"

def insert_name(name):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cursor = conn.cursor()
        
        # Insert the name into the names table
        cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Streamlit user interface
st.title("Name Entry Form")
name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        if insert_name(name):
            st.success(f"Name '{name}' has been added to the database!")
        else:
            st.error("Failed to add the name to the database.")
    else:
        st.warning("Please enter a name before submitting.")

