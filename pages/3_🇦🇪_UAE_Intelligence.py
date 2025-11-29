import streamlit as st

st.set_page_config(page_title="UAE Intelligence", layout="wide")

st.title("🇦🇪 UAE ENERGY INTELLIGENCE")
st.markdown("### The only platform that understands UAE life")

tab1, tab2, tab3 = st.tabs(["🌙 Ramadan AI", "☀️ Summer AI", "👨‍👩‍👧‍👦 Family AI"])

with tab1:
    st.header("🌙 Ramadan Energy Revolution")
    st.write("**Problem:** 80% night usage spikes during Ramadan")
    st.write("**Solution:** AI that adapts to night activity patterns")
    st.metric("Savings Potential", "AED 180-320/month", "During Ramadan")

with tab2:
    st.header("☀️ Summer Survival AI") 
    st.write("**Problem:** AC costs triple in UAE summers")
    st.write("**Solution:** Desert heat anticipation algorithms")
    st.metric("AC Savings", "55% reduction", "Summer months")

with tab3:
    st.header("👨‍👩‍👧‍👦 UAE Family Dynamics")
    st.write("**Problem:** Multi-generational homes have unique patterns")
    st.write("**Solution:** Family rhythm learning AI")
    st.metric("Efficiency Gain", "25% better", "Family optimization")
