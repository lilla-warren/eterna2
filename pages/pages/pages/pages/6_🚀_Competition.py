import streamlit as st

st.set_page_config(page_title="Why We Win", layout="wide")

st.title("🚀 WHY ETERNA WINS CREATE APPS CHAMPIONSHIP")
st.markdown("### The Unbeatable Competition Strategy")

# Competition advantages
advantages = [
    ("🎯 Problem Selection", "We solve 8 CRITICAL UAE problems that nobody else touches"),
    ("🇦🇪 Local Intelligence", "Only platform with true UAE cultural & climate adaptation"),
    ("🚀 Technical Innovation", "Energy orchestration, digital twins, predictive AI"),
    ("💼 Business Model", "AED 6.3B market, multiple revenue streams, clear path to scale"),
    ("🌍 National Impact", "Directly supports UAE Net Zero 2050 strategic initiative"),
    ("🏆 Demo Ready", "Fully functional, visually stunning, competition-optimized")
]

for title, description in advantages:
    st.markdown(f"### {title}")
    st.info(description)

# The "HOLY $#!%" moment
st.markdown("## 💥 THE 'HOLY $#!%' MOMENT FOR JUDGES")

st.markdown("""
**When judges realize:**

1. **We're solving ACTUAL national problems** - not just another utility app
2. **Nobody else is doing this** - we're pioneering UAE energy intelligence  
3. **The technology is real** - not just mockups, actual AI algorithms
4. **The business case is undeniable** - 2.1M households × AED 3,000 savings
5. **We align with UAE vision** - Net Zero 2050, sustainability, innovation

### 🏆 OUR COMPETITION DIFFERENTIATORS

- **Not just monitoring** → **Orchestration**
- **Not just global** → **UAE-specific**  
- **Not just reactive** → **Predictive**
- **Not just individual** → **National impact**
- **Not just technical** → **Cultural intelligence**
""")

# Call to action
st.markdown("## 🎯 READY TO TRANSFORM UAE ENERGY?")

if st.button("🏆 DEPLOY ETERNA NATIONWIDE", use_container_width=True, type="primary"):
    st.balloons()
    st.success("🚀 ETERNA DEPLOYED! Transforming 2.1M UAE homes starting today!")
