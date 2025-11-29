import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Bill Shield", layout="wide")

st.title("💰 BILL SHOCK SHIELD")
st.markdown("### Predict & Prevent Surprise Bills")

# Bill prediction chart
dates = pd.date_range(start=datetime.now(), periods=30, freq='D')
predicted = [400 + i*5 + random.randint(-20,20) for i in range(30)]

df = pd.DataFrame({'Date': dates, 'Predicted': predicted})
fig = px.line(df, x='Date', y='Predicted', title="30-Day Bill Forecast")
st.plotly_chart(fig, use_container_width=True)

# Early warnings
st.subheader("🚨 Early Warning System")
st.warning("AC overuse detected - bill may increase 28%")
st.info("Peak hour usage high - shift laundry to save AED 65")
st.error("Standby power waste - AED 45/month being lost")
