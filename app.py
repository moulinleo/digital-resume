from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent
css_file = current_dir / "styles" / "main2.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile_pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Leo Moulin"
PAGE_ICON = ":wave:"
NAME = "Leo Moulin"
DESCRIPTION = """
R&D Engineer specialized in Audio Signal Processing, Data Science, and Telecommunications, with a passion for problem-solving and innovation.
"""
EMAIL = "moulinleo17@gmail.com"
PHONE = "+32 472419811"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/leo-moulin-265b7017a",
    "GitHub": "https://github.com/moulinleo",
}
PROJECTS = ["Voice Isolation with CNN", "Satellite Communication Chain Simulation", "Anomaly Detection in Railway Services"]
PUBLICATION = {
    "Joint Registration of Multiple Point Sets with Refinement (IEEE ISM 2019)": "https://www.computer.org/csdl/proceedings-article/ism/2019/560600a072/1gFJdf4ARlm",
}
ACADEMIC_PROJECTS = {
    "Voice Isolation with a CNN (2018)": "Deep learning, audio signal processing, Tensorflow",
    "Simulation of a Satellite Communication Chain (2018)": "Matlab, modulation, coding, filtering",
    "Design of a Water Level Control System (2018)": "System identification, PID controller, Simulink",
    "Anomaly Detection in Railway Service (2024)": "Data exploration, feature engineering, model selection",
}

# --- LOAD CSS, PDF & PROFILE PIC ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)


# --- SIDEBAR ---
st.sidebar.title("Menu")
menu_selection = st.sidebar.radio("Projects", ["About Me"] + PROJECTS, label_visibility="collapsed")

# --- ABOUT ME SECTION ---
if menu_selection == "About Me":
    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=222)
        for platform, link in SOCIAL_MEDIA.items():
            st.write(f"[{platform}]({link})")

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.write(f"📞 {PHONE}")
        st.write(f"📫 {EMAIL}")
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    # --- WORK EXPERIENCE ---
    st.write('\n')
    st.subheader("Work Experience")
    st.write("---")

    # Adding company logos near each position
    col1, col2 = st.columns([6, 1])  # Adjust the width ratios to make the logo smaller
    with col1:
        st.write("**IoT Engineer | RTBF (Brussels)** ")
        st.write("_06/2024 - Now_")
    with col2:
        st.image(Image.open(current_dir / "assets" / "rtbf.png"), width=60)  # Small logo
    
    st.write("""
    - Led the development of IoT solutions for smart building vision of a media company.
    - Managed the deployment of IoT devices and sensors for data collection.
    - Conducted data analysis and visualization for IoT projects.
    """)

    st.write('\n')
    col1, col2 = st.columns([6, 1])
    with col1:
        st.write("**R&D Engineer in Audio Processing | SoundTalks (Leuven)** ")
        st.write("_03/2021 - 03/2023_")
    with col2:
        st.image(Image.open(current_dir / "assets" / "soundtalks.jpeg"), width=60)
    
    st.write("""
    - Developed Python algorithms for audio signal analysis and feature extraction.
    - Conducted research and validation of new audio processing algorithms.
    """)

    st.write('\n')
    col1, col2 = st.columns([6, 1])
    with col1:
        st.write("**Technical Engineer | Huawei Technologies Ltd (Brussels)**")
        st.write('_09/2019 - 08/2020_')
    with col2:
        st.image(Image.open(current_dir / "assets" / "huawei.png"), width=60)
    
    st.write("""
    - Delivered services and products for telecommunications customers.
    - Managed installation, commissioning, and support for fixed network technologies.
    """)

    st.write('\n')
    st.write("**Orchard Worker | Vineco (Hastings, New Zealand)**")
    st.write("_10/2018 - 12/2018_")
    st.write("""
    - Performed kiwi fruit thinning in New Zealand.
    """)
    
    
    # --- EDUCATION ---
    st.write('\n')
    st.subheader("Education")
    st.write("---")
    st.write("**Specialized Master in Data Science, Big Data | Université Libre de Bruxelles**")
    st.write("_2023-2024_")
    st.write("""
    - Data Mining, Deep Learning, Big Data Management
    """)
    
    st.write("**Master in Electrical Engineering - ICT Systems | Université Libre de Bruxelles**")
    st.write("_2016-2019_")
    st.write("""
    - Machine Learning, Digital Signal Processing, Final thesis: *3D Reconstruction in Multi-Camera Systems* (published in IEEE)
    """)
    
    st.write("**Bachelor in Civil Engineering (Electronics & Telecommunications) | Université Libre de Bruxelles**")
    st.write("_2012-2016_")
   

    # --- PROFESSIONAL SKILLS ---
    st.write('\n')
    st.subheader("Professional Skills")
    st.write("---")
    st.write(
        """
    - **Programming**: Python (Pandas, Scikit-learn, Tensorflow, Pytorch), SQL, C++, R
    - **Audio Signal Processing**: Librosa, Matlab
    - **Data Analysis**: Data Science Stack, Statistical Modeling, Machine Learning
    - **Tools**: Git, JupyterLab, Linux Scripting
    """
    )
    

    # --- LANGUAGES ---
    st.write('\n')
    st.subheader("Languages")
    st.write("---")
    st.write(
        """
        - 🇫🇷 French: Native
        - 🇬🇧 English: Professional Working Proficiency
        - 🇳🇱 Dutch: Basic
        """
    )

    # --- PUBLICATIONS ---
    st.write('\n')
    st.subheader("Publications")
    st.write("---")
    for title, link in PUBLICATION.items():
        st.write(f"[{title}]({link})")

    # --- INTERESTS ---
    st.write('\n')
    st.subheader("Interests")
    st.write("---")
    st.write(
        """
        - 🏞️ Mountain Hiking
        - 🤖 Applications of Machine Learning
        - 🎲 Board Games
        """
    )

    # --- ACADEMIC PROJECTS ---
    st.write('\n')
    st.subheader("Academic Projects")
    st.write("---")
    for project, details in ACADEMIC_PROJECTS.items():
        st.write(f"**{project}**: {details}")

# --- PROJECT SECTIONS ---
else:
    if menu_selection == "Voice Isolation with CNN":
        import projects.voice_isolation as project
    elif menu_selection == "Satellite Communication Chain Simulation":
        import projects.satellite_simulation as project
    elif menu_selection == "Anomaly Detection in Railway Services":
        import projects.railway_anomaly as project
    
    # Display project-specific content
    project.run()
