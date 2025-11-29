import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title="Smart Dashboard", layout="wide")

st.title("🏠 SMART HOME DASHBOARD")
st.markdown("### Real-time Energy Intelligence")

# Live metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Usage", f"{random.randint(1200, 1800)}W", "-12%")
with col2:
    st.metric("Next Bill", f"AED {random.randint(380, 520)}", "-15%")
with col3:
    st.metric("CO₂ Saved", f"{random.randint(15, 25)} kg", "3.2 trees")

# Live gauge
st.subheader("⚡ Live Efficiency Score")
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=random.randint(65, 85),
    title={'text': "Efficiency"},
    gauge={'axis': {'range': [None, 100]}}
))
st.plotly_chart(fig, use_container_width=True)

# Active optimizations
st.subheader("🎯 Active Optimizations")
st.success("🌡️ AC Optimization: Saving AED 120/month")
st.success("💡 Peak Avoidance: Saving AED 85/month")
st.success("🔌 Standby Reduction: Saving AED 40/month")
