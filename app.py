from pathlib import Path

import streamlit as st
from PIL import Image

# path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "resume_ds.pdf"
profile_pic = current_dir / "assets" / "pf_image.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Dhirendra Kumar"
PAGE_ICON = ":wave:"
NAME = "Dhirendra Kumar"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "dhirendra.hitk@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/dhirendra-kumar-4271b7230?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "GitHub": "https://github.com/kdhirendra"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",)
    st.write("📫", EMAIL)

# SOCIAL LINKS
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('#')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('#')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy, Pandas), SQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 🗄️ Databases: MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('#')
st.subheader("Projects & Accomplishments")
st.write(
    """
    - 🏆 NLP Web-App  - Named Entity Recognition, Sentiment Analysis, Abuse Detection
    - 🏆 Income and Expense Tracker - Web app with NoSQL database
    - 🏆 Flight Dashboard - Check Flights and Flight Database Analysis
    """
)