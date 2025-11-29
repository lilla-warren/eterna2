import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="UAE Intelligence", layout="wide")

# Initialize session state if not exists
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'home_type': 'Apartment',
        'ac_units': 2,
        'family_size': 4,
        'rooms': ['Living Room', 'Master Bedroom', 'Kitchen'],
        'appliances': ['AC', 'Refrigerator', 'Washing Machine']
    }

# Add location if missing
if 'location' not in st.session_state.user_profile:
    st.session_state.user_profile['location'] = 'Dubai'

if 'uai_settings' not in st.session_state:
    st.session_state.uai_settings = {
        'ramadan_mode': True,
        'summer_optimization': True,
        'family_patterns': True,
        'desert_adaptation': True
    }

st.title("🇦🇪 UAE ENERGY INTELLIGENCE")
st.markdown("### Cultural & Climate AI for Your Home")

# PERSONALIZED UAE SETTINGS
with st.sidebar:
    st.markdown("### ⚙️ UAE Intelligence Settings")
    
    with st.form("uae_settings_form"):
        st.subheader("🎯 Enable AI Features")
        
        ramadan_mode = st.checkbox(
            "🌙 Ramadan Intelligence", 
            value=st.session_state.uai_settings['ramadan_mode'],
            help="Adapt to night usage patterns during Ramadan"
        )
        
        summer_optimization = st.checkbox(
            "☀️ Summer Survival AI", 
            value=st.session_state.uai_settings['summer_optimization'],
            help="Optimize for extreme summer temperatures"
        )
        
        family_patterns = st.checkbox(
            "👨‍👩‍👧‍👦 Family Dynamics", 
            value=st.session_state.uai_settings['family_patterns'],
            help="Learn and adapt to your family's unique patterns"
        )
        
        desert_adaptation = st.checkbox(
            "🏜️ Desert Adaptation", 
            value=st.session_state.uai_settings['desert_adaptation'],
            help="Optimize for UAE's desert climate conditions"
        )
        
        location = st.selectbox(
            "Your Emirate",
            ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"],
            index=["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"].index(
                st.session_state.user_profile.get('location', 'Dubai')
            )
        )
        
        if st.form_submit_button("💾 Save UAE Settings", use_container_width=True):
            st.session_state.uai_settings = {
                'ramadan_mode': ramadan_mode,
                'summer_optimization': summer_optimization,
                'family_patterns': family_patterns,
                'desert_adaptation': desert_adaptation
            }
            st.session_state.user_profile['location'] = location
            st.success("✅ UAE settings saved!")
            st.rerun()

# MAIN CONTENT - PERSONALIZED UAE INTELLIGENCE
tab1, tab2, tab3, tab4 = st.tabs(["🌙 Ramadan AI", "☀️ Summer AI", "👨‍👩‍👧‍👦 Family AI", "🏜️ Desert AI"])

with tab1:
    st.markdown("### 🌙 Ramadan Energy Intelligence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Ramadan patterns card
        with st.container():
            st.markdown("#### 🕌 Your Ramadan Patterns")
            st.write(f"Based on your **family of {st.session_state.user_profile['family_size']}** in **{st.session_state.user_profile.get('location', 'Dubai')}**")
            
            st.divider()
            
            col1a, col1b = st.columns(2)
            with col1a:
                st.write("**Iftar Preparation**")
                st.write("**Taraweeh Prayers**")
                st.write("**Family Gatherings**")
                st.write("**Suhoor Preparation**")
            with col1b:
                st.write("6:00 PM - 7:30 PM")
                st.write("8:30 PM - 10:00 PM")
                st.write("10:00 PM - 1:00 AM")
                st.write("3:30 AM - 4:30 AM")
    
    with col2:
        # Personalized Ramadan usage pattern
        st.markdown("#### 📊 Your Ramadan vs Normal Usage")
        
        hours = [f"{h} PM" if h < 12 else f"{h-12} AM" if h > 12 else "12 AM" for h in range(18, 30)]
        
        # Base usage adjusted for family size and AC units
        base_normal = [random.randint(80, 120) for _ in range(12)]
        base_ramadan = [min(200, u * (1.5 + (st.session_state.user_profile['family_size'] * 0.1))) for u in base_normal]
        
        df_ramadan = pd.DataFrame({
            'Hour': hours,
            'Normal Day': base_normal,
            'Ramadan Day': base_ramadan
        })
        
        fig_ramadan = px.line(df_ramadan, x='Hour', y=['Normal Day', 'Ramadan Day'], 
                             title=f"Ramadan Pattern for {st.session_state.user_profile['family_size']}-Person Family")
        fig_ramadan.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"},
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ramadan, use_container_width=True)
    
    # Personalized Ramadan savings
    ramadan_savings = st.session_state.user_profile['family_size'] * 45 + st.session_state.user_profile['ac_units'] * 25
    
    with st.container():
        st.markdown("#### 💰 Your Ramadan Savings Potential")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.metric(
                "Monthly Savings During Ramadan", 
                f"AED {ramadan_savings}",
                "Personalized for your family"
            )
        
        with col4:
            st.metric(
                "AC Optimization", 
                f"{35 + st.session_state.user_profile['ac_units'] * 3}%",
                "Ramadan-specific"
            )
            st.metric(
                "Lighting Efficiency", 
                f"{25 + st.session_state.user_profile['family_size'] * 2}%", 
                "Night activity optimized"
            )
    
    if st.session_state.uai_settings['ramadan_mode']:
        st.success("🌙 Ramadan Intelligence: ACTIVE - Your home will automatically adapt to Ramadan patterns")
    else:
        st.warning("🌙 Ramadan Intelligence: INACTIVE - Enable in settings for optimal Ramadan savings")

with tab2:
    st.markdown("### ☀️ Summer Survival AI")
    
    col1, col2 = st.columns(2)
    
    with col1:
        summer_savings = st.session_state.user_profile['ac_units'] * 55 + (100 if st.session_state.user_profile['home_type'] == 'Villa' else 0)
        
        with st.container():
            st.markdown("#### 🔥 UAE Summer Optimization")
            st.write(f"Personalized for your **{st.session_state.user_profile['home_type']}** with **{st.session_state.user_profile['ac_units']} AC units**")
            
            st.divider()
            
            # Summer features as badges
            st.write("**Desert Heat Adaptation** 🌡️")
            st.write("**Peak Temperature Management** ☀️")
            st.write("**AC Compressor Protection** ❄️")
            st.write("**Sandstorm Preparation** 🏜️")
            
            st.divider()
            
            st.metric(
                "Summer Savings Target", 
                f"AED {summer_savings}/month",
                "AC-focused optimization"
            )
    
    with col2:
        # Summer temperature and usage correlation
        st.markdown("#### 🌡️ Temperature vs AC Usage")
        
        temperatures = [35, 38, 41, 44, 47, 50]
        ac_usage = [temp * st.session_state.user_profile['ac_units'] * 2.5 for temp in temperatures]
        
        fig_summer = go.Figure()
        fig_summer.add_trace(go.Scatter(
            x=temperatures, 
            y=ac_usage,
            mode='lines+markers',
            name='AC Usage (W)',
            line=dict(color='#F59E0B', width=4),
            marker=dict(size=8)
        ))
        
        fig_summer.update_layout(
            title="UAE Summer: Temperature Impact on Your AC Usage",
            xaxis_title="Temperature (°C)",
            yaxis_title="AC Power Consumption (W)",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"}
        )
        st.plotly_chart(fig_summer, use_container_width=True)
    
    # Summer optimization features
    st.markdown("#### ❄️ Your Summer Optimization Plan")
    
    summer_features = [
        ("Smart Pre-cooling", f"Cool before peak heat - Save AED {st.session_state.user_profile['ac_units'] * 25}"),
        ("AC Staggering", f"Coordinate {st.session_state.user_profile['ac_units']} units - Save AED {st.session_state.user_profile['ac_units'] * 18}"),
        ("Peak Avoidance", "Shift heavy usage - Save AED 75"),
        ("Equipment Protection", "Extend AC lifespan - Save on maintenance")
    ]
    
    if st.session_state.user_profile['home_type'] == 'Villa':
        summer_features.append(("Pool Optimization", "Reduce evaporation - Save AED 95"))
    
    for feature, savings in summer_features:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{feature}**")
            with col2:
                st.write(f"**{savings}**")

with tab3:
    st.markdown("### 👨‍👩‍👧‍👦 Family Dynamics AI")
    
    # Calculate family-specific savings
    family_scheduling = st.session_state.user_profile['family_size'] * 18
    room_optimization = len(st.session_state.user_profile['rooms']) * 15
    pattern_learning = st.session_state.user_profile['family_size'] * 12
    
    with st.container():
        st.markdown(f"#### 🏡 Understanding Your Family of {st.session_state.user_profile['family_size']}")
        st.write(f"AI learning your unique family patterns in **{st.session_state.user_profile.get('location', 'Dubai')}**")
    
    # Family profile using Streamlit components
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 👥 Your Family Profile")
        
        # Create a nice container for family info
        with st.container():
            st.metric("Family Size", f"{st.session_state.user_profile['family_size']} people")
            st.metric("Home Type", st.session_state.user_profile['home_type'])
            st.metric("AC Units", f"{st.session_state.user_profile['ac_units']} units")
            st.metric("Rooms", f"{len(st.session_state.user_profile['rooms'])} rooms")
    
    with col2:
        st.markdown("##### 💡 Family-Specific Savings")
        
        # Create savings container
        with st.container():
            st.metric("Family Scheduling", f"AED {family_scheduling}/mo")
            st.metric("Room Optimization", f"AED {room_optimization}/mo") 
            st.metric("Pattern Learning", f"AED {pattern_learning}/mo")
            
            total_family_savings = family_scheduling + room_optimization + pattern_learning
            st.metric("Total Family Savings", f"AED {total_family_savings}/mo", delta="Optimized")
    
    # Family daily pattern
    st.markdown("#### 📅 Your Family's Daily Rhythm")
    
    times = ["6 AM", "9 AM", "12 PM", "3 PM", "6 PM", "9 PM", "12 AM"]
    family_activity = [
        "🌅 Wake up & Preparation",
        "💼 Work/School Hours", 
        "🍽️ Lunch & Break",
        "☀️ Afternoon Activities",
        "👨‍👩‍👧‍👦 Family Time",
        "📺 Evening Relaxation",
        "😴 Sleep Time"
    ]
    
    usage_levels = [30, 60, 70, 85, 95, 80, 40]
    
    df_family = pd.DataFrame({
        'Time': times,
        'Activity': family_activity,
        'Energy Usage': usage_levels
    })
    
    fig_family = px.bar(df_family, x='Time', y='Energy Usage', 
                       hover_data=['Activity'],
                       title=f"Daily Energy Pattern for {st.session_state.user_profile['family_size']}-Person Family")
    fig_family.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"}
    )
    fig_family.update_traces(marker_color='#22C55E')
    st.plotly_chart(fig_family, use_container_width=True)

with tab4:
    st.markdown("### 🏜️ Desert Climate Adaptation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("#### 🌵 Desert-Optimized Systems")
            st.write("Specialized for UAE's unique climate conditions")
            
            st.divider()
            
            st.write("**🌡️ Extreme Heat Management**")
            st.caption("AC optimization for 45°C+ temperatures")
            
            st.write("**💧 Humidity Control**")
            st.caption("Coastal area adaptation")
            
            st.write("**🏜️ Sand & Dust Protection**")
            st.caption("Equipment maintenance optimization")
    
    with col2:
        # Desert efficiency comparison
        st.markdown("#### ⚡ Desert vs Standard Efficiency")
        
        categories = ['AC Performance', 'Equipment Life', 'Energy Cost', 'Maintenance']
        standard = [65, 70, 60, 55]
        desert_optimized = [
            65 + st.session_state.user_profile['ac_units'] * 4,
            70 + 15,
            60 + 20,
            55 + 18
        ]
        
        fig_desert = go.Figure()
        fig_desert.add_trace(go.Bar(
            name='Standard System',
            x=categories,
            y=standard,
            marker_color='#EF4444'
        ))
        fig_desert.add_trace(go.Bar(
            name='Desert Optimized',
            x=categories,
            y=desert_optimized,
            marker_color='#22C55E'
        ))
        
        fig_desert.update_layout(
            title="Desert Climate Performance Comparison",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"},
            barmode='group'
        )
        st.plotly_chart(fig_desert, use_container_width=True)
    
    # Desert-specific optimizations
    st.markdown("#### 🎯 Your Desert Adaptation Plan")
    
    desert_optimizations = [
        (f"AC Desert Mode for {st.session_state.user_profile['ac_units']} units", "Optimized for extreme heat"),
        ("Humidity Priority", "Remove moisture before cooling - More efficient"),
        ("Sandstorm Protocol", "Automatic system protection during storms"),
        ("Rapid Response", "Quick adaptation to temperature changes")
    ]
    
    for optimization, description in desert_optimizations:
        with st.container():
            st.write(f"**{optimization}**")
            st.caption(description)

# ACTIVATE ALL UAE INTELLIGENCE
st.markdown("---")
st.markdown("### 🚀 Activate UAE Intelligence")

if st.button("🇦🇪 ACTIVATE ALL UAE AI FEATURES", type="primary", use_container_width=True):
    st.session_state.uai_settings = {
        'ramadan_mode': True,
        'summer_optimization': True,
        'family_patterns': True,
        'desert_adaptation': True
    }
    st.balloons()
    st.success("🎉 All UAE Intelligence features activated! Your home is now optimized for UAE life!")
    st.rerun()

# UAE IMPACT SUMMARY
st.markdown("---")
st.markdown("### 📊 Your UAE Impact Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Cultural Adaptation", "4/4 Features", "Fully optimized")

with col2:
    st.metric("Climate Optimization", "Desert Ready", "UAE specific")

with col3:
    total_uae_savings = (st.session_state.user_profile['family_size'] * 45 + 
                        st.session_state.user_profile['ac_units'] * 55 +
                        (100 if st.session_state.user_profile['home_type'] == 'Villa' else 0))
    st.metric("Monthly Savings", f"AED {total_uae_savings}", "UAE optimized")

with col4:
    st.metric("National Alignment", "Net Zero 2050", "UAE Vision")
