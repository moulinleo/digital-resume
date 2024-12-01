import streamlit as st
import altair as alt
import pandas as pd

def run():
    st.title("Anomaly Detection in Railway Services")
    st.write("""
    Built a predictive model to detect and prevent anomalies in railway systems using machine learning.
    """)
    st.image("assets/profile-pic.png", use_column_width=True)
    
    st.write("### Key Highlights")
    st.write("- Explored extensive railway maintenance datasets.")
    st.write("- Implemented model selection and feature engineering for prediction.")
    
    st.write("### Interactive Graph")
    data = pd.DataFrame({"Date": ["Jan", "Feb", "Mar"], "Anomalies": [5, 3, 1]})
    chart = alt.Chart(data).mark_bar().encode(
        x="Date",
        y="Anomalies",
        tooltip=["Date", "Anomalies"]
    )
    st.altair_chart(chart, use_container_width=True)
    
    st.write("### Resources")
    st.write("[GitHub Repository](https://github.com/moulinleo/railway-anomaly)")
    st.write("[Detailed Documentation](https://example.com/railway-doc)")
