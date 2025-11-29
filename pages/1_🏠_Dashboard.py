import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random
import time

st.set_page_config(page_title="Smart Dashboard", layout="wide")

# Animated CSS for dashboard
st.markdown("""
<style>
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.15);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .slide-in {
        animation: slideIn 0.8s ease-out;
    }
    
    .pulse-dot {
        width: 12px;
        height: 12px;
        background: #22C55E;
        border-radius: 50%;
        display: inline-block;
        animation: pulse 2s infinite;
        margin-right: 8px;
    }
    
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0.7; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.7; }
    }
</style>
""", unsafe_allow_html=True)

st.title("🏠 SMART DASHBOARD")
st.markdown("### <span class='pulse-dot'></span>Live Energy Intelligence", unsafe_allow_html=True)

# Animated metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card slide-in">
        <div style="font-size: 2rem; font-weight: bold; color: #22C55E;">1.4kW</div>
        <div style="opacity: 0.8;">Current Usage</div>
        <div style="color: #22C55E; font-size: 0.9rem;">▼ 12% from average</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card slide-in" style="animation-delay: 0.1s;">
        <div style="font-size: 2rem; font-weight: bold; color: #22C55E;">AED 427</div>
        <div style="opacity: 0.8;">Next Bill</div>
        <div style="color: #22C55E; font-size: 0.9rem;">▼ 15% predicted</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card slide-in" style="animation-delay: 0.2s;">
        <div style="font-size: 2rem; font-weight: bold; color: #22C55E;">78%</div>
        <div style="opacity: 0.8;">Efficiency</div>
        <div style="color: #22C55E; font-size: 0.9rem;">Optimal range</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card slide-in" style="animation-delay: 0.3s;">
        <div style="font-size: 2rem; font-weight: bold; color: #22C55E;">24kg</div>
        <div style="opacity: 0.8;">CO₂ Saved</div>
        <div style="color: #22C55E; font-size: 0.9rem;">3.1 trees equivalent</div>
    </div>
    """, unsafe_allow_html=True)

# Live efficiency gauge with animation
st.markdown("### 📊 Live Home Efficiency")
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=78,
    delta={'reference': 65, 'increasing': {'color': "#22C55E"}},
    title={'text': "Overall Efficiency", 'font': {'size': 24}},
    gauge={
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
        'bar': {'color': "#22C55E"},
        'bgcolor': "rgba(255,255,255,0.1)",
        'borderwidth': 2,
        'bordercolor': "rgba(255,255,255,0.2)",
        'steps': [
            {'range': [0, 60], 'color': 'rgba(239, 68, 68, 0.3)'},
            {'range': [60, 80], 'color': 'rgba(234, 179, 8, 0.3)'},
            {'range': [80, 100], 'color': 'rgba(34, 197, 94, 0.3)'}],
        'threshold': {
            'line': {'color': "white", 'width': 4},
            'thickness': 0.75,
            'value': 78}
    }
))
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font={'color': "white", 'family': "Arial"},
    height=300
)
st.plotly_chart(fig, use_container_width=True)

# Room energy usage with smooth bars
st.markdown("### 🏠 Room-by-Room Energy Flow")
rooms = ["Master Bedroom", "Living Room", "Kitchen", "Guest Room", "Pool Area"]
usage = [420, 380, 320, 280, 450]

fig2 = px.bar(
    x=rooms, y=usage,
    color=usage,
    color_continuous_scale=["#22C55E", "#F59E0B", "#EF4444"],
    title=""
)
fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font={'color': "white"},
    showlegend=False,
    xaxis_title="",
    yaxis_title="Energy Usage (W)"
)
st.plotly_chart(fig2, use_container_width=True)

# Active optimizations with hover effects
st.markdown("### 🎯 Active AI Optimizations")
optimizations = [
    ("🌡️ AC Smart Cycling", "Saving AED 120/month", "#22C55E"),
    ("💡 Peak Avoidance", "Saving AED 85/month", "#22C55E"),
    ("🔌 Standby Reduction", "Saving AED 45/month", "#22C55E"),
    ("💧 Pool Optimization", "Saving AED 95/month", "#22C55E")
]

for opt, savings, color in optimizations:
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.1);
        border-left: 4px solid {color};
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    " onmouseover="this.style.background='rgba(255,255,255,0.15)'; this.style.transform='translateX(5px)';" 
    onmouseout="this.style.background='rgba(255,255,255,0.1)'; this.style.transform='translateX(0px)';">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: bold;">{opt}</span>
            <span style="color: {color}; font-weight: bold;">{savings}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
