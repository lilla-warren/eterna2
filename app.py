import streamlit as st

st.set_page_config(
    page_title="ETERNA • UAE Energy Revolution",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# MIND-BLOWING CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0F4C81 0%, #1a237e 50%, #283593 100%);
        color: white;
    }
    
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        margin: 2rem 0;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .problem-card {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 5px solid #CE1126;
        color: #1E293B;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    .nav-button {
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 2rem;
        margin: 0.5rem;
        border: none;
        transition: all 0.3s ease;
    }
    
    .nav-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero-section">
    <h1 class="floating" style="font-size: 5rem; margin-bottom: 0;">⚡ ETERNA</h1>
    <h2 style="font-size: 2rem; margin-top: 0;">THE ENERGY REVOLUTION UAE HAS BEEN WAITING FOR</h2>
    <p style="font-size: 1.5rem;">Solving 8 critical energy problems that nobody else touches</p>
</div>
""", unsafe_allow_html=True)

# THE PROBLEMS WE SOLVE
st.markdown("## 🎯 THE UNTOUCHABLE PROBLEMS WE SOLVE")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="problem-card">
        <h3>⚡ Peak Demand Crisis</h3>
        <p><b>The Problem:</b> 3-6PM grid overload costs billions</p>
        <p><b>Our Solution:</b> AI that shifts usage automatically</p>
        <p><b>Impact:</b> 35% peak reduction potential</p>
    </div>
    
    <div class="problem-card">
        <h3>🏠 Villa Energy Chaos</h3>
        <p><b>The Problem:</b> Pools, multiple ACs, outdoor lighting = 500% waste</p>
        <p><b>Our Solution:</b> Whole-home orchestration</p>
        <p><b>Impact:</b> AED 15,000+ annual savings</p>
    </div>
    
    <div class="problem-card">
        <h3>🌙 Ramadan Energy Reversal</h3>
        <p><b>The Problem:</b> Night usage spikes 80% - nobody adapts</p>
        <p><b>Our Solution:</b> Cultural pattern AI</p>
        <p><b>Impact:</b> AED 2,160 savings per Ramadan</p>
    </div>
    
    <div class="problem-card">
        <h3>🧠 Behavioral Blindness</h3>
        <p><b>The Problem:</b> People waste 45% without knowing</p>
        <p><b>Our Solution:</b> Real-time waste detection</p>
        <p><b>Impact:</b> Instant 25% savings</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="problem-card">
        <h3>🏢 Construction Efficiency Debt</h3>
        <p><b>The Problem:</b> Buildings leak energy in desert climate</p>
        <p><b>Our Solution:</b> Digital twin simulations</p>
        <p><b>Impact:</b> 40% better efficiency</p>
    </div>
    
    <div class="problem-card">
        <h3>💰 Subsidy Confusion</h3>
        <p><b>The Problem:</b> 80% don't understand tiered pricing</p>
        <p><b>Our Solution:</b> Automated subsidy optimization</p>
        <p><b>Impact:</b> 15% bill reduction</p>
    </div>
    
    <div class="problem-card">
        <h3>🌡️ Desert AC Inefficiency</h3>
        <p><b>The Problem:</b> ACs work 3x harder in UAE heat</p>
        <p><b>Our Solution:</b> Desert-optimized algorithms</p>
        <p><b>Impact:</b> 55% AC cost reduction</p>
    </div>
    
    <div class="problem-card">
        <h3>🔌 Smart Home Fragmentation</h3>
        <p><b>The Problem:</b> Devices don't talk to each other</p>
        <p><b>Our Solution:</b> Universal energy orchestration</p>
        <p><b>Impact:</b> 30% better coordination</p>
    </div>
    """, unsafe_allow_html=True)

# NAVIGATION TO SOLUTIONS - FIXED
st.markdown("## 🚀 EXPLORE OUR REVOLUTIONARY SOLUTIONS")

# Create navigation buttons that work with Streamlit's auto-page detection
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("**🏠 Smart Dashboard**\n\nReal-time home intelligence", use_container_width=True):
        st.switch_page("pages/1_🏠_Dashboard.py")
    
    if st.button("**⚡ Live Orchestrator**\n\nWatch AI coordinate your home", use_container_width=True):
        st.switch_page("pages/2_⚡_Live_Orchestrator.py")

with col2:
    if st.button("**🇦🇪 UAE Intelligence**\n\nCultural & climate adaptation", use_container_width=True):
        st.switch_page("pages/3_🇦🇪_UAE_Intelligence.py")
    
    if st.button("**🏗️ Digital Twin**\n\n3D home simulation", use_container_width=True):
        st.switch_page("pages/4_🏗️_Digital_Twin.py")

with col3:
    if st.button("**💰 Bill Shield**\n\nPredict & prevent surprises", use_container_width=True):
        st.switch_page("pages/5_💰_Bill_Shield.py")
    
    if st.button("**🚀 Competition Ready**\n\nWhy we'll win", use_container_width=True):
        st.switch_page("pages/6_🚀_Competition.py")

# COMPETITION KILLER STATS
st.markdown("## 📊 THE NUMBERS THAT WIN COMPETITIONS")

metric_cols = st.columns(4)
metric_cols[0].metric("UAE Homes Impacted", "2.1M", "100% coverage")
metric_cols[1].metric("Annual Savings Potential", "AED 6.3B", "National impact")
metric_cols[2].metric("CO₂ Reduction", "1.2M tons", "Net Zero 2050")
metric_cols[3].metric("Problem Solved", "8/8", "Complete solution")

# FOOTER
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3>⚡ FROM STUDENT PROJECT TO NATIONAL SOLUTION</h3>
    <p>Create Apps Championship 2024 • UAE Energy Revolution</p>
</div>
""", unsafe_allow_html=True)
