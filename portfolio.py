import streamlit as st

# Set the title and page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="centered")

# Header
st.title("Welcome to My Personal Portfolio!")

# About Section
st.header("About Me")
st.write("""
    Hi! My real name is Eugene Barglespeugh, a passionate software developer with experience in Python, Streamlit, and other web technologies.
    I love creating web applications that are both functional and aesthetically pleasing. I also enjoy hacking for fun sometimes!
""")

# Skills Section
st.header("Skills")
st.write("""
- Python
- Streamlit
- Web Development (HTML, CSS, JavaScript)
- Machine Learning
- Data Science
- Cybersecurity
""")

# Projects Section
st.header("Projects")
st.write("""
Here are some of the projects I've worked on:
""")

# Add some projects
st.subheader("Project 1: Portfolio Website")
st.write("""
A simple and interactive portfolio built with Streamlit.
""")

st.subheader("Project 2: Web Scraping Tool")
st.write("""
A tool to scrape and analyze data from websites.
""")

# Footer
st.write("Thank you for visiting my portfolio! 🚀")

