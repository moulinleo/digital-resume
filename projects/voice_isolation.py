import streamlit as st
import altair as alt
import pandas as pd

def run():
    st.title("Voice Isolation with CNN")
    st.write("""
    This project focuses on isolating voice signals from noisy audio environments using deep learning techniques.
    """)
    st.image("assets/profile-pic.png", use_column_width=True)
    
    st.write("### Key Highlights")
    st.write("- Implemented using TensorFlow and Python.")
    st.write("- Achieved 92% accuracy on real-world audio datasets.")
    
    st.write("### Interactive Graph")
    data = pd.DataFrame({"Epoch": [1, 2, 3], "Accuracy": [80, 85, 92]})
    chart = alt.Chart(data).mark_line().encode(
        x="Epoch",
        y="Accuracy",
        tooltip=["Epoch", "Accuracy"]
    )
    st.altair_chart(chart, use_container_width=True)
    
    st.write("### Resources")
    st.write("[GitHub Repository](https://github.com/moulinleo/voice-isolation)")
    st.write("[Detailed Documentation](https://example.com/voice-isolation-doc)")
