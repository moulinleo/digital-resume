import streamlit as st
import altair as alt
import pandas as pd

def run():
    st.title("Satellite Communication Chain Simulation")
    st.write("""
    Simulated satellite communication chains with coding, filtering, and modulation techniques.
    """)
    st.image("assets/profile-pic.png", use_column_width=True)
    
    st.write("### Key Highlights")
    st.write("- Developed in MATLAB for high-speed communication systems.")
    st.write("- Demonstrated error correction with simulated noisy environments.")
    
    st.write("### Interactive Graph")
    data = pd.DataFrame({"Iteration": [1, 2, 3], "Error Rate": [0.1, 0.08, 0.05]})
    chart = alt.Chart(data).mark_line().encode(
        x="Iteration",
        y="Error Rate",
        tooltip=["Iteration", "Error Rate"]
    )
    st.altair_chart(chart, use_container_width=True)

    
    st.write("### Resources")
    st.write("[GitHub Repository](https://github.com/moulinleo/satellite-simulation)")
    st.write("[Detailed Documentation](https://example.com/satellite-doc)")


