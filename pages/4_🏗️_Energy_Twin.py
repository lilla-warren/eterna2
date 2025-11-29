import streamlit as st
import plotly.express as px
import pandas as pd
import random

st.set_page_config(page_title="Digital Twin", layout="wide")

st.title("🏗️ DIGITAL ENERGY TWIN")
st.markdown("### 3D Simulation of Your Home's Energy Flow")

# Room energy simulation
rooms = ["Bedroom", "Living Room", "Kitchen", "Guest Room", "Pool", "Outdoor"]
usage = [random.randint(200, 600) for _ in rooms]

fig = px.bar(x=rooms, y=usage, title="Room-by-Room Energy Consumption")
st.plotly_chart(fig, use_container_width=True)

# What-if scenarios
st.subheader("🔮 What-If Scenarios")
scenario = st.selectbox("Test improvements:", 
    ["Add Solar Panels", "Upgrade AC", "Smart Pool", "Better Insulation"])

if scenario:
    st.success(f"**{scenario} Impact:** +{random.randint(15,40)}% efficiency | AED {random.randint(150,400)} monthly savings")
