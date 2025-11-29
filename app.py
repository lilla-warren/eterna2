import streamlit as st

st.set_page_config(
    page_title="ETERNA • UAE Energy Revolution", 
    page_icon="⚡",
    layout="wide"
)

# SIMPLE CSS
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
    }
</style>
""", unsafe_allow_html=True)

# SIMPLE HOMEPAGE
st.markdown("""
<div class="hero-section">
    <h1 style="font-size: 4rem; margin-bottom: 0;">⚡ ETERNA</h1>
    <h2>UAE Energy Intelligence Platform</h2>
    <p>Solving energy problems that nobody else touches</p>
</div>
""", unsafe_allow_html=True)

# SIMPLE CONTENT
st.markdown("## 🎯 We Solve 8 Critical UAE Energy Problems")

col1, col2 = st.columns(2)
with col1:
    st.write("⚡ Peak Demand Crisis")
    st.write("🏠 Villa Energy Chaos")
    st.write("🌙 Ramadan Patterns")
    st.write("🧠 Behavioral Waste")
with col2:
    st.write("🏢 Building Efficiency")
    st.write("💰 Bill Confusion")
    st.write("🌡️ Desert AC Issues")
    st.write("🔌 Smart Home Coordination")

st.markdown("---")
st.info("🚀 **Use the sidebar to explore our solutions!**")
