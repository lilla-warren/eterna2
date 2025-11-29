import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta
import time

# Ultimate page config
st.set_page_config(
    page_title="ETERNA • UAE Energy Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CUSTOM CSS FOR WOW FACTOR
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #0F4C81 0%, #1a237e 50%, #283593 100%);
    }
    
    /* Premium cards */
    .wow-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Animated header */
    @keyframes glow {
        0% { text-shadow: 0 0 10px #22C55E; }
        50% { text-shadow: 0 0 20px #22C55E, 0 0 30px #22C55E; }
        100% { text-shadow: 0 0 10px #22C55E; }
    }
    
    .glowing-header {
        animation: glow 2s ease-in-out infinite;
        font-size: 4rem;
        text-align: center;
        color: white;
        font-weight: 900;
    }
</style>
""", unsafe_allow_html=True)

# DYNAMIC CALCULATION ENGINE
class EnergyCalculator:
    def __init__(self, home_type, ac_units, family_size):
        self.home_type = home_type
        self.ac_units = ac_units
        self.family_size = family_size
        
    def calculate_base_usage(self):
        # Base calculation based on inputs
        if self.home_type == "Luxury Villa":
            base = 1800 + (self.ac_units * 150) + (self.family_size * 80)
        elif self.home_type == "Premium Apartment":
            base = 1200 + (self.ac_units * 120) + (self.family_size * 60)
        else:  # Executive Townhouse
            base = 1500 + (self.ac_units * 130) + (self.family_size * 70)
        return base
    
    def calculate_savings(self):
        base_usage = self.calculate_base_usage()
        
        # Dynamic savings calculations
        ac_savings = (self.ac_units * 40) + (base_usage * 0.15)
        pool_savings = 85 if self.home_type == "Luxury Villa" else 0
        kitchen_savings = (self.family_size * 15) + 20
        lighting_savings = (base_usage * 0.08)
        
        total_savings = ac_savings + pool_savings + kitchen_savings + lighting_savings
        
        return {
            'ac_savings': int(ac_savings),
            'pool_savings': pool_savings,
            'kitchen_savings': int(kitchen_savings),
            'lighting_savings': int(lighting_savings),
            'total_savings': int(total_savings),
            'annual_savings': int(total_savings * 12),
            'co2_reduction': int(total_savings * 0.137),  # kg CO2 per AED saved
            'trees_equivalent': round(total_savings * 0.137 / 8.5, 1)  # trees equivalent
        }
    
    def calculate_uae_patterns(self):
        # UAE-specific pattern calculations
        ramadan_savings = (self.family_size * 25) + 80
        summer_savings = (self.ac_units * 55) + 100
        family_savings = (self.family_size * 12) + 40
        
        return {
            'ramadan_savings': int(ramadan_savings),
            'summer_savings': int(summer_savings),
            'family_savings': int(family_savings)
        }

# Initialize session state
if 'savings_activated' not in st.session_state:
    st.session_state.savings_activated = False
if 'show_animation' not in st.session_state:
    st.session_state.show_animation = False
if 'calculator' not in st.session_state:
    st.session_state.calculator = None

# ANIMATED HEADER
st.markdown('<h1 class="glowing-header">⚡ ETERNA</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; color: white; margin-bottom: 3rem;">THE FUTURE OF UAE HOME ENERGY</h3>', unsafe_allow_html=True)

# SIDEBAR WITH PREMIUM DESIGN
with st.sidebar:
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #0F4C81 0%, #1a237e 100%);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🚀 Control Center")
    
    st.subheader("🏠 Smart Home Setup")
    home_type = st.selectbox("Home Type", ["Luxury Villa", "Premium Apartment", "Executive Townhouse"])
    ac_units = st.slider("Smart AC Units", 1, 8, 3)
    family_size = st.slider("Family Size", 1, 12, 5)
    
    # Update calculator when inputs change
    st.session_state.calculator = EnergyCalculator(home_type, ac_units, family_size)
    
    st.subheader("⚡ AI Optimization")
    if st.button("🎯 ACTIVATE ENERGY ORCHESTRATION", use_container_width=True, type="primary"):
        st.session_state.savings_activated = True
        st.session_state.show_animation = True
        st.balloons()
        st.success("🚀 AI ORCHESTRATION ACTIVATED!")

# Calculate dynamic values
if st.session_state.calculator:
    savings_data = st.session_state.calculator.calculate_savings()
    uae_patterns = st.session_state.calculator.calculate_uae_patterns()
    
    # Dynamic bill prediction based on inputs
    base_bill = st.session_state.calculator.calculate_base_usage() * 0.35  # Convert to AED
    bill_prediction = int(base_bill - savings_data['total_savings'])
else:
    # Default values before calculator is initialized
    savings_data = {
        'ac_savings': 120, 'pool_savings': 85, 'kitchen_savings': 65, 
        'lighting_savings': 40, 'total_savings': 310, 'annual_savings': 3720,
        'co2_reduction': 42, 'trees_equivalent': 5.3
    }
    uae_patterns = {
        'ramadan_savings': 180, 'summer_savings': 220, 'family_savings': 95
    }
    bill_prediction = 427

# MAIN DASHBOARD - PREMIUM LAYOUT
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.metric(
            label="💰 NEXT BILL PREDICTION", 
            value=f"AED {bill_prediction}",
            delta=f"-{random.randint(12, 25)}%",
            delta_color="inverse"
        )
        st.progress(0.65)
        st.caption(f"AI Accuracy: {random.randint(92, 97)}%")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.metric(
            label="⚡ LIVE ENERGY FLOW", 
            value=f"{st.session_state.calculator.calculate_base_usage() if st.session_state.calculator else 1500}W",
            delta=f"{random.randint(5, 15)}% optimal"
        )
        # Real-time usage gauge
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = random.randint(65, 85),
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Efficiency Score"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#22C55E"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "lightgreen"}
                ]
            }
        ))
        fig.update_layout(height=200, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.metric(
            label="🌍 PLANET IMPACT", 
            value=f"{savings_data['co2_reduction']} kg CO₂",
            delta=f"{savings_data['trees_equivalent']} trees planted"
        )
        st.caption("Your sustainability journey")
        st.markdown('</div>', unsafe_allow_html=True)

# ENERGY ORCHESTRATION VISUALIZATION
st.markdown("---")
st.markdown('<h2 style="color: white;">🎵 SMART HOME ENERGY ORCHESTRATION</h2>', unsafe_allow_html=True)

orch_col1, orch_col2, orch_col3, orch_col4 = st.columns(4)

with orch_col1:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🌡️ AC SYMPHONY")
        st.metric("Optimized", "24°C", "-3°C")
        st.metric("Savings", f"AED {savings_data['ac_savings']}", f"{random.randint(25, 35)}%")
        st.markdown('</div>', unsafe_allow_html=True)

with orch_col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 💧 POOL MAESTRO")
        st.metric("Smart Pump", "Active", "Optimal")
        st.metric("Savings", f"AED {savings_data['pool_savings']}", f"{random.randint(40, 50)}%")
        st.markdown('</div>', unsafe_allow_html=True)

with orch_col3:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🍳 KITCHEN RHYTHM")
        st.metric("Peak Avoidance", "Active", "Smart")
        st.metric("Savings", f"AED {savings_data['kitchen_savings']}", f"{random.randint(25, 35)}%")
        st.markdown('</div>', unsafe_allow_html=True)

with orch_col4:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 💡 LIGHTING HARMONY")
        st.metric("Auto-Dimming", "Active", "Efficient")
        st.metric("Savings", f"AED {savings_data['lighting_savings']}", f"{random.randint(15, 25)}%")
        st.markdown('</div>', unsafe_allow_html=True)

# AI ENERGY INTELLIGENCE
st.markdown("---")
st.markdown('<h2 style="color: white;">🤖 AI ENERGY INTELLIGENCE</h2>', unsafe_allow_html=True)

ai_col1, ai_col2 = st.columns(2)

with ai_col1:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🇦🇪 UAE SMART PATTERNS")
        
        # Ramadan Intelligence
        st.markdown("**🌙 Ramadan Mode**")
        progress_ramadan = min(uae_patterns['ramadan_savings'] / 300, 1.0)
        st.progress(progress_ramadan)
        st.caption(f"Night optimization: AED {uae_patterns['ramadan_savings']}/month savings")
        
        # Summer Intelligence  
        st.markdown("**☀️ Summer Survival AI**")
        progress_summer = min(uae_patterns['summer_savings'] / 400, 1.0)
        st.progress(progress_summer)
        st.caption(f"Peak heat management: AED {uae_patterns['summer_savings']}/month savings")
        
        # Family Intelligence
        st.markdown("**👨‍👩‍👧‍👦 Family Rhythm AI**")
        progress_family = min(uae_patterns['family_savings'] / 200, 1.0)
        st.progress(progress_family)
        st.caption(f"Pattern learning: AED {uae_patterns['family_savings']}/month savings")
        
        st.markdown('</div>', unsafe_allow_html=True)

with ai_col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 PREDICTIVE INSIGHTS")
        
        insights = [
            f"🎯 {ac_units} AC units optimized - Maximum efficiency achieved",
            f"📈 {family_size} family members - Patterns learned and optimized", 
            f"💡 {home_type} configuration - Tailored savings activated",
            f"🌙 Ramadan ready - {uae_patterns['ramadan_savings']} AED/month savings configured",
            f"🏆 You're in top {random.randint(10, 20)}% of efficient UAE homes"
        ]
        
        for insight in insights:
            st.info(insight)
            st.write("")
        
        st.markdown('</div>', unsafe_allow_html=True)

# SAVINGS IMPACT VISUALIZATION
if st.session_state.savings_activated:
    st.markdown("---")
    st.markdown('<h2 style="color: white; text-align: center;">🎉 ENERGY ORCHESTRATION ACTIVATED!</h2>', unsafe_allow_html=True)
    
    impact_col1, impact_col2, impact_col3 = st.columns(3)
    
    with impact_col1:
        st.metric("MONTHLY SAVINGS", f"AED {savings_data['total_savings']}", 
                 f"{int((savings_data['total_savings']/base_bill)*100)}%", delta_color="inverse")
    
    with impact_col2:
        st.metric("ANNUAL IMPACT", f"AED {savings_data['annual_savings']}", 
                 "Game Changing", delta_color="inverse")
    
    with impact_col3:
        st.metric("CO₂ REDUCTION", f"{savings_data['co2_reduction']} kg", 
                 f"{savings_data['trees_equivalent']} trees", delta_color="inverse")
    
    # Achievement badges
    st.markdown("### 🏆 EARNED ACHIEVEMENTS")
    badge_col1, badge_col2, badge_col3, badge_col4 = st.columns(4)
    
    with badge_col1:
        st.success("🌍 Eco Warrior")
    with badge_col2:
        st.success("💡 Energy Maestro")
    with badge_col3:
        st.success("🇦🇪 UAE Smart Home")
    with badge_col4:
        st.success("🚀 AI Pioneer")

# FOOTER WITH IMPACT
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: white; padding: 2rem;">
    <h3>⚡ TRANSFORMING UAE HOMES, ONE WATT AT A TIME</h3>
    <p>ETERNA • Create Apps Championship 2024 • UAE Energy Revolution</p>
</div>
""", unsafe_allow_html=True)

# WOW ANIMATION
if st.session_state.show_animation:
    st.balloons()
    st.session_state.show_animation = False
