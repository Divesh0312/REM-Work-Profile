import streamlit as st

# Page Configuration
st.set_page_config(page_title="Divesh Bangera - REM Portfolio", layout="wide")

# --- SIDEBAR: Personal Info ---
with st.sidebar:
    #st.image("https://drive.google.com/uc?export=view&id=1dvg3DDm3pwMPfejy0zQdYPJoTmtmycse", caption="Divesh Bangera") # Replace with your photo link
    st.title("Divesh Bangera")
    st.write("**Roll No:** 22108A0079")
    st.write("**Branch:** Electronics & Computer Science - A")
    st.write("**Year:** BE - Final Year")
    st.write("**Institute:** Vidyalankar Institute of Technology")
    st.divider()
    st.markdown("### Quick Links")
    st.write("[LinkedIn](https://linkedin.com/in/yourprofile)") # Update with your link
    st.write("[GitHub](https://github.com/yourusername)")      # Update with your link

# --- MAIN CONTENT ---
st.title("Renewable Energy Management Work Profile")
st.markdown("---")

# Section 1: About the Subject & Learning Outcomes
col1, col2 = st.columns([2, 1])

with col1:
    st.header("What I've Learnt")
    st.write("""
    Throughout this course, I have explored the transition from conventional fossil fuels to sustainable 
    non-conventional energy sources. Key areas of focus included:
    """)
    st.markdown("""
    * **Energy Fundamentals:** Comparing Renewable vs. Non-Renewable energy scenarios[cite: 552].
    * **Solar Technologies:** Deep dive into Solar PV systems and Solar Thermal applications[cite: 561, 648].
    * **Hydropower & Biomass:** Principles of hydro generation and modern biomass conversion[cite: 6, 42].
    * **Management & Policy:** Implementing Energy Management Systems (EMS) and understanding India's renewable energy policies[cite: 93, 141].
    """)

with col2:
    st.header("Course Outcomes")
    st.info("""
    - **CO1:** Understand principles of technologies[cite: 1000].
    - **CO2:** Analyze economic and environmental impacts[cite: 1004].
    - **CO3:** Design systems for specific applications[cite: 1007].
    - **CO6:** Gain practical skills in project planning[cite: 1014].
    """)

st.divider()

# Section 2: Assignment Repository
st.header("My Assignments & Projects")

# Organizing assignments in an expander for a clean look
with st.expander("View All REM Assignments", expanded=True):
    # Corrected table headers
    c1, c2, c3 = st.columns([1, 3, 1])
    c1.markdown("**No.**")
    c2.markdown("**Topic**")
    c3.markdown("**Link**")
    
    assignments = [
        ("0", "Assignment 0", "https://drive.google.com/file/d/13NdEpyv1Z6Oh6GpdjYbdkeyIJ5UTaZ-R/view?usp=sharing"),
        ("1", "Assignment 1 : one page report on national energy scenario", "https://drive.google.com/file/d/1WecRPMi7ijKFS8FaazsbEnvN11A9FtWk/view?usp=sharing"),
        ("2", "Assignment 2 (a+b): Upload Signed PDF of Handwritten Assignment", "https://drive.google.com/file/d/129LT_VlDARRKrzGrWSPvLCByonFKHad7/view?usp=sharing"),
        ("3", "Assignment 3:Tech & App sheet: Dashboard energy utility scenario in VIT campus", "https://drive.google.com/file/d/1svP1hD_AjJq3Qj59NTs2bYNwPoCSKNKx/view?usp=sharing"),
        ("4", "Assignment 4: upload signed PDF of handwritten questions", "https://drive.google.com/file/d/1qcVKcJJupcThbpcUCWE6_qDkOPHdq8zI/view?usp=sharing"),
        ("5", "Assignment 5: Smart Poster of a real life case study on REM", "https://drive.google.com/file/d/1Ppjkcjl66Bqg8ptVcKwh44-vf6MSEI6U/view?usp=sharing"),
        ("6", "Assignment 9: Design Based Assignment on REM Applications Video (FLashcard)", "https://drive.google.com/file/d/195hYjU3ONVhTKJsTztqnni2xxTJesxsF/view?usp=sharing"),
        ("7", "Assignment 9: Design Based Assignment on REM Applications Video (Quiz)", "https://drive.google.com/file/d/1NxZS-_7sR-gO00v5WRhzrm20jabq0Vle/view?usp=sharing"),
        ("8", "Assignment 9: Design Based Assignment on REM Applications Video (Summary Report)", "https://drive.google.com/file/d/1muH85Ajx-GBeDAfzEklyJNwBDJfawXLY/view?usp=sharing"),
        ("9", "Assignment 9: Design Based Assignment on REM Applications Video (MindMap)", "https://drive.google.com/file/d/1I_-TVnyObeoXXwYOxeR0iqYPNmji83Up/view?usp=sharing")
    ]

    for no, topic, link in assignments:
        col_a, col_b, col_c = st.columns([1, 3, 1])
        col_a.write(no)
        col_b.write(topic)
        col_c.markdown(f"[View PDF]({link})")

st.divider()

# Section 3: Technical Skills Highlight
st.header("🛠 Technical Skills Highlight")
st.markdown("""
* **Programming:** Python (Streamlit, Pandas, Plotly) [cite: 787-790]
* **Analysis:** Data cleaning and interactive dashboarding for energy utility scenarios [cite: 782]
* **Design:** Technical posters and process flow diagrams [cite: 496]
""")

st.success("Thank you for visiting my REM Work Profile!")