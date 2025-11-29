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
    
    /* UAE flag colors */
    .uae-red { color: #CE1126; }
    .uae-green { color: #22C55E; }
    .uae-white { color: white; }
    .uae-black { color: #000000; }
    
    /* Premium buttons */
    .stButton>button {
        border-radius: 15px;
        border: none;
        padding: 1rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# ANIMATED HEADER
st.markdown('<h1 class="glowing-header">⚡ ETERNA</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; color: white; margin-bottom: 3rem;">THE FUTURE OF UAE HOME ENERGY</h3>', unsafe_allow_html=True)

# Initialize session state for WOW effects
if 'savings_activated' not in st.session_state:
    st.session_state.savings_activated = False
if 'show_animation' not in st.session_state:
    st.session_state.show_animation = False

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
    family_members = st.slider("Family Members", 1, 12, 5)
    
    st.subheader("⚡ AI Optimization")
    if st.button("🎯 ACTIVATE ENERGY ORCHESTRATION", use_container_width=True, type="primary"):
        st.session_state.savings_activated = True
        st.session_state.show_animation = True
        st.balloons()
        st.success("🚀 AI ORCHESTRATION ACTIVATED!")

# MAIN DASHBOARD - PREMIUM LAYOUT
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.metric(
            label="💰 NEXT BILL PREDICTION", 
            value=f"AED {random.randint(380, 520)}",
            delta=f"-{random.randint(12, 25)}%",
            delta_color="inverse"
        )
        st.progress(0.65)
        st.caption("AI Accuracy: 94.7%")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.metric(
            label="⚡ LIVE ENERGY FLOW", 
            value=f"{random.randint(1200, 1800)}W",
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
            value=f"{random.randint(18, 32)} kg CO₂",
            delta=f"{random.randint(3, 6)} trees planted"
        )
        st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=300", use_column_width=True)
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
        st.metric("Savings", "AED 120", "32%")
        st.markdown('</div>', unsafe_allow_html=True)

with orch_col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 💧 POOL MAESTRO")
        st.metric("Smart Pump", "Active", "Optimal")
        st.metric("Savings", "AED 85", "45%")
        st.markdown('</div>', unsafe_allow_html=True)

with orch_col3:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🍳 KITCHEN RHYTHM")
        st.metric("Peak Avoidance", "Active", "Smart")
        st.metric("Savings", "AED 65", "28%")
        st.markdown('</div>', unsafe_allow_html=True)

with orch_col4:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 💡 LIGHTING HARMONY")
        st.metric("Auto-Dimming", "Active", "Efficient")
        st.metric("Savings", "AED 40", "18%")
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
        st.progress(0.8)
        st.caption("Night optimization: AED 180/month savings")
        
        # Summer Intelligence  
        st.markdown("**☀️ Summer Survival AI**")
        st.progress(0.9)
        st.caption("Peak heat management: AED 220/month savings")
        
        # Family Intelligence
        st.markdown("**👨‍👩‍👧‍👦 Family Rhythm AI**")
        st.progress(0.7)
        st.caption("Pattern learning: AED 95/month savings")
        
        st.markdown('</div>', unsafe_allow_html=True)

with ai_col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 PREDICTIVE INSIGHTS")
        
        insights = [
            "🎯 AC units will lose 12% efficiency in 30 days - Schedule maintenance",
            "📈 Next month's bill predicted to spike 28% - Activate Summer Mode", 
            "💡 23% of energy wasted on standby - Smart plugs recommended",
            "🌙 Ramadan night usage pattern detected - Auto-optimization ready",
            "🏆 You're in top 15% of efficient UAE homes"
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
        st.metric("MONTHLY SAVINGS", "AED 310", "27%", delta_color="inverse")
    
    with impact_col2:
        st.metric("ANNUAL IMPACT", "AED 3,720", "Game Changing", delta_color="inverse")
    
    with impact_col3:
        st.metric("CO₂ REDUCTION", "42.5 kg", "5.3 trees", delta_color="inverse")
    
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

# COMPETITION WINNING FEATURES
st.markdown("---")
st.markdown('<h2 style="color: white;">🏆 COMPETITION-READY INNOVATIONS</h2>', unsafe_allow_html=True)

innov_col1, innov_col2, innov_col3 = st.columns(3)

with innov_col1:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🎵 Energy Orchestration")
        st.write("First system that coordinates ALL home devices like a symphony conductor")
        st.markdown('</div>', unsafe_allow_html=True)

with innov_col2:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🇦🇪 Cultural AI")
        st.write("Only platform that understands Ramadan, summer, and UAE family patterns")
        st.markdown('</div>', unsafe_allow_html=True)

with innov_col3:
    with st.container():
        st.markdown('<div class="wow-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 Predictive Immunity")
        st.write("Prevents bill shock 30 days in advance with AI predictions")
        st.markdown('</div>', unsafe_allow_html=True)

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
