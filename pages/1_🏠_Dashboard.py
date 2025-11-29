import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title="Smart Dashboard", layout="wide")

st.title("🏠 SMART HOME DASHBOARD")
st.markdown("### Real-time Energy Intelligence")

# Live energy flow simulation
col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(go.Figure(go.Indicator(
        mode = "gauge+number",
        value = random.randint(1200, 1800),
        title = {'text': "LIVE USAGE"},
        gauge = {'axis': {'range': [None, 2000]}}
    )), use_container_width=True)

with col2:
    st.plotly_chart(go.Figure(go.Indicator(
        mode = "gauge+number",
        value = random.randint(65, 95),
        title = {'text': "EFFICIENCY SCORE"},
        gauge = {'axis': {'range': [None, 100]}}
    )), use_container_width=True)

with col3:
    st.plotly_chart(go.Figure(go.Indicator(
        mode = "gauge+number", 
        value = random.randint(40, 80),
        title = {'text': "SAVINGS POTENTIAL"},
        gauge = {'axis': {'range': [None, 100]}}
    )), use_container_width=True)

# Problem-Solution Matrix
st.markdown("## 🎯 ACTIVE PROBLEM SOLVING")

problems = [
    ("Peak Demand", "85%", "AI shifting load: -35%"),
    ("AC Overuse", "72%", "Smart cycling: -55%"), 
    ("Standby Waste", "45%", "Auto shutoff: -80%"),
    ("Pool Inefficiency", "63%", "Optimal scheduling: -40%"),
    ("Ramadan Spike", "78%", "Night optimization: -60%")
]

for problem, severity, solution in problems:
    col1, col2, col3 = st.columns([1, 1, 2])
    col1.metric("Problem", problem)
    col2.metric("Severity", severity)
    col3.metric("Our Solution", solution)
