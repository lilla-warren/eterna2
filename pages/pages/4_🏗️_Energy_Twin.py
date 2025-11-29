import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Digital Energy Twin", layout="wide")

st.title("🏗️ DIGITAL ENERGY TWIN")
st.markdown("### 3D Simulation of Your Home's Energy Flow")

# Interactive home model
st.markdown("#### 🏠 Your Home's Energy DNA")

home_type = st.selectbox("Select Home Type", 
    ["Luxury Villa (5,000 sq ft)", "Premium Apartment (2,000 sq ft)", "Executive Townhouse (3,500 sq ft)"])

# Energy flow simulation
st.markdown("#### 🔋 Live Energy Flow Map")

# Simulate room-by-room energy usage
rooms = ["Master Bedroom", "Living Room", "Kitchen", "Guest Room", "Pool Area", "Outdoor"]
usage = [random.randint(200, 600) for _ in rooms]

fig = px.bar(x=rooms, y=usage, title="Room-by-Room Energy Consumption")
st.plotly_chart(fig, use_container_width=True)

# What-if scenarios
st.markdown("#### 🔮 What-If Scenarios")

scenario = st.selectbox("Test different scenarios",
    ["Add Solar Panels", "Upgrade AC Units", "Install Smart Pool", "Add Guest Wing"])

if scenario:
    st.success(f"**{scenario} Impact:** +{random.randint(15, 40)}% efficiency | AED {random.randint(150, 400)} monthly savings")
