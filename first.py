import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- Load Assets ---
profile_pic = Image.open("your_photo.png")  # Replace with your actual image
resume_file = "resume.pdf"  # Replace with your actual resume

# --- Header ---
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(profile_pic, width=150)
    with col2:
        st.title("Suraj Kumar Jha")
        st.write("📧 zhasuraj31@gmail.com ")

# --- About ---
with st.container():
    st.subheader("About Me")
    st.write(
        "I am a passionate software developer with a strong background in Python, "
        "machine learning, and web development. I love building interactive tools "
        "and data-driven applications."
    )

# --- Skills ---
with st.container():
    st.subheader("Skills")
    st.write("""
    - 🐍 Python, Streamlit
    - 🌐 HTML, CSS, JavaScript
    -    Other Programmings(java , C, C++ ,Php, Mysql)
    """)

# --- Projects ---
with st.container():
    st.subheader("Projects")
    
    project_1, project_2 = st.columns(2)

    with project_1:
        st.markdown("### 📊 Data ")
        st.image("dashboard_project.png")  # replace with actual image
        st.write("An interactive dashboard built with Streamlit and Plotly.")
        st.markdown("[View Project](https://github.com/Suraj31-creator/app)")

    with project_2:
        st.markdown("### 🤖 Mini SearchEngine")
        st.image("ml_project.png")  # replace with actual image
        st.write("A LLM model based on langchain technology.")
        st.markdown("[View Project](https://github.com/Suraj31-creator/suraj_web)")

# --- Resume Download ---
with st.container():
    st.subheader("Resume")
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Your_Name_Resume.pdf",
        mime='application/octet-stream'
    )
st.subheader('''© 2025 SurajPortfolio. All rights reserved.

This website and its contents, including text, graphics, logos, code, and design, are the intellectual property of Suraj Kumar Jha unless otherwise stated. Unauthorized copying, reproduction, or distribution of any material from this site is prohibited without prior written permission.

For inquiries or usage permissions, please contact: [zhasuraj31@gmail.com]
''')
