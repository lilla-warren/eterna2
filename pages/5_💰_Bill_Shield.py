import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Bill Shock Shield", layout="wide")

st.title("💰 BILL SHOCK SHIELD")
st.markdown("### Predict & Prevent Surprise Bills 30 Days in Advance")

# Bill prediction timeline
st.markdown("#### 📅 30-Day Bill Forecast")

dates = pd.date_range(start=datetime.now(), periods=30, freq='D')
predicted = [400 + i*5 + random.randint(-20, 20) for i in range(30)]
actual = [val + random.randint(-30, 30) for val in predicted]

df = pd.DataFrame({
    'Date': dates,
    'Predicted': predicted,
    'Actual': actual
})

fig = px.line(df, x='Date', y=['Predicted', 'Actual'], 
              title="30-Day Bill Prediction vs Actual")
st.plotly_chart(fig, use_container_width=True)

# Early warning system
st.markdown("#### 🚨 EARLY WARNING SYSTEM")

warnings = [
    ("AC Overuse Detected", "Bill will increase 28%", "Optimize now to save AED 185"),
    ("Peak Hour Spike", "3PM usage 45% above normal", "Shift usage to save AED 95"),
    ("Standby Power Waste", "AED 65 monthly ghost load", "Smart plugs can save 80%"),
    ("Pool Pump Inefficiency", "Running 4 extra hours daily", "Optimize schedule: Save AED 120")
]

for warning, problem, solution in warnings:
    with st.expander(f"⚠️ {warning}"):
        st.error(f"**Problem:** {problem}")
        st.success(f"**Solution:** {solution}")
