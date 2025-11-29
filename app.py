import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="ETERNA - UAE Energy Intelligence",
    page_icon="⚡",
    layout="wide"
)

# UAE-inspired styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #0F4C81;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 4px solid #22C55E;
    }
    .uae-blue {
        color: #0F4C81;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<h1 class="main-header">⚡ ETERNA</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="uae-blue" style="text-align: center;">UAE Energy Intelligence Platform</h3>', unsafe_allow_html=True)

# Initialize session state
if 'savings_mode' not in st.session_state:
    st.session_state.savings_mode = False

# Sidebar
with st.sidebar:
    st.header("🏠 Home Setup")
    home_type = st.selectbox("Home Type", ["Apartment", "Villa", "Townhouse"])
    ac_units = st.slider("AC Units", 1, 10, 2)
    family_size = st.slider("Family Size", 1, 10, 4)
    
    st.header("⚡ Quick Actions")
    if st.button("🎯 Activate Savings Mode", type="primary"):
        st.session_state.savings_mode = True
        st.success("Savings mode activated! Saving AED 245/month")
    
    if st.button("📊 Generate Report"):
        st.info("Energy report generated!")

# Main dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="Next Bill Prediction", 
        value=f"AED {random.randint(380, 520)}",
        delta=f"-{random.randint(5, 15)}%"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="Current Usage", 
        value=f"{random.randint(1200, 1800)} W",
        delta=f"+{random.randint(1, 8)}%"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(
        label="CO₂ Saved", 
        value=f"{random.randint(15, 25)} kg",
        delta="3.2 trees"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Energy consumption chart
st.subheader("📈 Energy Consumption Trends")
dates = pd.date_range(start='2024-01-01', end='2024-06-01', freq='M')
consumption = [random.randint(300, 600) for _ in dates]

fig = px.line(
    x=dates, 
    y=consumption,
    labels={'x': 'Month', 'y': 'AED'},
    title="Monthly Energy Costs"
)
fig.update_traces(line_color='#0F4C81')
st.plotly_chart(fig, use_container_width=True)

# AI Insights
st.subheader("🤖 AI Energy Insights")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **🌡️ AC Optimization Opportunity**
    - Your AC uses 70% of total energy
    - Setting to 24°C can save AED 120/month
    - Recommended: Smart scheduling
    """)

with col2:
    st.warning("""
    **⏰ Peak Hour Alert**
    - 2PM-8PM usage is 45% higher
    - Shift laundry to morning: Save AED 65/month
    - Use delay start features
    """)

# Savings impact
if st.session_state.savings_mode:
    st.success("""
    **🎉 Savings Mode Active**
    - AC optimized: Saving AED 120/month
    - Peak avoidance: Saving AED 85/month  
    - Standby reduction: Saving AED 40/month
    - **Total: AED 245/month savings!**
    """)

# UAE-specific features
st.subheader("🇦🇪 UAE Energy Intelligence")

tab1, tab2, tab3 = st.tabs(["Ramadan Mode", "Summer Optimization", "Family Patterns"])

with tab1:
    st.write("""
    **🌙 Ramadan Energy Patterns**
    - Night usage increases by 60-80%
    - Iftar time peak: 6PM-8PM
    - Recommended: Pre-cool before Iftar
    - Potential savings: AED 180/month
    """)
    
with tab2:
    st.write("""
    **☀️ Summer Survival Guide**  
    - AC costs triple in summer months
    - Recommended temp: 24-26°C
    - Use curtains during peak sun
    - Service AC units monthly
    """)
    
with tab3:
    st.write("""
    **👨‍👩‍👧‍👦 Family Energy Patterns**
    - Teenager rooms: 23% higher usage
    - Living room: 35% of total energy
    - Kitchen: 15% during cooking hours
    - Guest rooms: Optimize when empty
    """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B;'>ETERNA • UAE Energy Intelligence • Create Apps Championship 2024</p>", unsafe_allow_html=True)
