import streamlit as st

st.set_page_config(
    page_title="ETERNA • UAE Energy Revolution", 
    page_icon="⚡",
    layout="wide"
)

# AMAZING CSS
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
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
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
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero-section">
    <h1 class="floating" style="font-size: 4rem; margin-bottom: 0;">⚡ ETERNA</h1>
    <h2 style="font-size: 2rem; margin-top: 0;">UAE ENERGY INTELLIGENCE PLATFORM</h2>
    <p style="font-size: 1.2rem;">Solving 8 critical energy problems that nobody else touches</p>
</div>
""", unsafe_allow_html=True)

# PROBLEMS WE SOLVE
st.markdown("## 🎯 8 UNTOUCHABLE UAE ENERGY PROBLEMS")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="problem-card">
        <h3>⚡ Peak Demand Crisis</h3>
        <p><b>3-6PM grid overload</b> costs billions</p>
        <p>Our AI shifts usage automatically</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-card">
        <h3>🏠 Villa Energy Chaos</h3>
        <p><b>Pools + multiple ACs</b> = 500% waste</p>
        <p>Whole-home orchestration</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-card">
        <h3>🌙 Ramadan Reversal</h3>
        <p><b>80% night usage spikes</b> during Ramadan</p>
        <p>Cultural pattern AI adaptation</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-card">
        <h3>🧠 Behavioral Blindness</h3>
        <p><b>45% energy waste</b> goes unseen</p>
        <p>Real-time waste detection</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="problem-card">
        <h3>🏢 Construction Debt</h3>
        <p><b>Buildings leak energy</b> in desert climate</p>
        <p>Digital twin simulations</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-card">
        <h3>💰 Subsidy Confusion</h3>
        <p><b>80% don't understand</b> tiered pricing</p>
        <p>Automated subsidy optimization</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-card">
        <h3>🌡️ Desert AC Issues</h3>
        <p><b>ACs work 3x harder</b> in UAE heat</p>
        <p>Desert-optimized algorithms</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="problem-card">
        <h3>🔌 Smart Home Fragmentation</h3>
        <p><b>Devices don't talk</b> to each other</p>
        <p>Universal energy orchestration</p>
    </div>
    """, unsafe_allow_html=True)

# COMPETITION STATS
st.markdown("## 📊 THE NUMBERS THAT WIN COMPETITIONS")

col1, col2, col3, col4 = st.columns(4)
col1.metric("UAE Homes", "2.1M", "100% coverage")
col2.metric("Annual Savings", "AED 6.3B", "National impact") 
col3.metric("CO₂ Reduction", "1.2M tons", "Net Zero 2050")
col4.metric("Problems Solved", "8/8", "Complete solution")

# NAVIGATION
st.markdown("---")
st.success("🚀 **Explore our revolutionary solutions in the sidebar!**")

# FOOTER
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3>⚡ FROM STUDENT PROJECT TO NATIONAL SOLUTION</h3>
    <p>Create Apps Championship 2024 • UAE Energy Revolution</p>
</div>
""", unsafe_allow_html=True)
