import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Dashboard", layout="wide")

# Initialize session state for user data
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'home_type': 'Apartment',
        'ac_units': 2,
        'family_size': 4,
        'location': 'Dubai',
        'bill_target': 400,
        'rooms': ['Living Room', 'Master Bedroom', 'Kitchen'],
        'appliances': ['AC', 'Refrigerator', 'Washing Machine']
    }

if 'energy_data' not in st.session_state:
    st.session_state.energy_data = {
        'current_usage': 1500,
        'monthly_bill': 450,
        'savings_goal': 300,
        'usage_history': [],
        'custom_rooms': {}
    }

# ANIMATED CSS
st.markdown("""
<style>
    .user-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .user-card:hover {
        transform: translateY(-3px);
        background: rgba(255, 255, 255, 0.15);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    
    .setup-section {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 4px solid #22C55E;
    }
    
    .metric-highlight {
        background: linear-gradient(45deg, #22C55E, #16A34A);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
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
</style>
""", unsafe_allow_html=True)

st.title("🏠 YOUR SMART DASHBOARD")
st.markdown("### Personalized Energy Intelligence")

# SIDEBAR - USER SETUP
with st.sidebar:
    st.markdown("### ⚙️ Your Home Setup")
    
    with st.form("user_profile_form"):
        st.subheader("🏠 Tell Us About Your Home")
        
        home_type = st.selectbox(
            "Home Type",
            ["Apartment", "Villa", "Townhouse", "Duplex"],
            index=["Apartment", "Villa", "Townhouse", "Duplex"].index(st.session_state.user_profile['home_type'])
        )
        
        ac_units = st.slider(
            "Number of AC Units", 
            min_value=1, 
            max_value=10, 
            value=st.session_state.user_profile['ac_units']
        )
        
        family_size = st.slider(
            "Family Members", 
            min_value=1, 
            max_value=15, 
            value=st.session_state.user_profile['family_size']
        )
        
        location = st.selectbox(
            "Emirate",
            ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"],
            index=["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"].index(st.session_state.user_profile['location'])
        )
        
        bill_target = st.number_input(
            "Monthly Bill Target (AED)",
            min_value=100,
            max_value=2000,
            value=st.session_state.user_profile['bill_target']
        )
        
        # Custom rooms setup
        st.subheader("🏠 Your Rooms")
        default_rooms = st.session_state.user_profile['rooms']
        custom_rooms = st.text_area(
            "List your rooms (one per line)",
            value="\n".join(default_rooms),
            help="e.g., Master Bedroom, Living Room, Kitchen, Guest Room, etc."
        )
        
        # Appliances setup
        st.subheader("🔌 Major Appliances")
        default_appliances = st.session_state.user_profile['appliances']
        custom_appliances = st.text_area(
            "List your major appliances (one per line)",
            value="\n".join(default_appliances),
            help="e.g., AC, Refrigerator, Washing Machine, Water Heater, etc."
        )
        
        # Save button
        if st.form_submit_button("💾 Save My Profile", use_container_width=True):
            # Update user profile
            st.session_state.user_profile.update({
                'home_type': home_type,
                'ac_units': ac_units,
                'family_size': family_size,
                'location': location,
                'bill_target': bill_target,
                'rooms': [room.strip() for room in custom_rooms.split('\n') if room.strip()],
                'appliances': [appliance.strip() for appliance in custom_appliances.split('\n') if appliance.strip()]
            })
            
            # Recalculate energy data based on new profile
            base_usage = 1200 if home_type == "Apartment" else 1800 if home_type == "Villa" else 1500
            usage_adjustment = (ac_units * 120) + (family_size * 60)
            
            st.session_state.energy_data.update({
                'current_usage': base_usage + usage_adjustment,
                'monthly_bill': int((base_usage + usage_adjustment) * 0.35),
                'savings_goal': bill_target
            })
            
            st.success("✅ Profile saved successfully!")
            st.rerun()

# MAIN DASHBOARD CONTENT
col1, col2 = st.columns([2, 1])

with col1:
    # PERSONALIZED METRICS
    st.markdown("### 📊 Your Energy Snapshot")
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        current_bill = st.session_state.energy_data['monthly_bill']
        target_bill = st.session_state.user_profile['bill_target']
        bill_diff = current_bill - target_bill
        
        st.markdown(f"""
        <div class="user-card">
            <div style="font-size: 1.2rem; font-weight: bold; color: {'#EF4444' if bill_diff > 0 else '#22C55E'};">
                AED {current_bill}
            </div>
            <div style="opacity: 0.8;">Current Bill</div>
            <div style="color: {'#EF4444' if bill_diff > 0 else '#22C55E'}; font-size: 0.9rem;">
                {'▲' if bill_diff > 0 else '▼'} AED {abs(bill_diff)} { 'above' if bill_diff > 0 else 'below'} target
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown(f"""
        <div class="user-card">
            <div style="font-size: 1.2rem; font-weight: bold; color: #22C55E;">
                {st.session_state.energy_data['current_usage']}W
            </div>
            <div style="opacity: 0.8;">Live Usage</div>
            <div style="color: #22C55E; font-size: 0.9rem;">
                ▼ Optimized for {st.session_state.user_profile['home_type']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        efficiency = min(95, 60 + (st.session_state.user_profile['ac_units'] * 3) + (st.session_state.user_profile['family_size'] * 2))
        st.markdown(f"""
        <div class="user-card">
            <div style="font-size: 1.2rem; font-weight: bold; color: #22C55E;">
                {efficiency}%
            </div>
            <div style="opacity: 0.8;">Efficiency Score</div>
            <div style="color: #22C55E; font-size: 0.9rem;">
                { 'Excellent' if efficiency > 80 else 'Good' if efficiency > 65 else 'Needs improvement'}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # PERSONALIZED EFFICIENCY GAUGE
    st.markdown("### 🎯 Your Efficiency Progress")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=efficiency,
        delta={'reference': 65, 'increasing': {'color': "#22C55E"}},
        title={'text': f"Personalized for {st.session_state.user_profile['home_type']}", 'font': {'size': 16}},
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
                'value': efficiency}
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "white", 'family': "Arial"},
        height=300
    )
    st.plotly_chart(fig, use_container_width=True)

    # CUSTOM ROOMS ENERGY USAGE
    if st.session_state.user_profile['rooms']:
        st.markdown("### 🏠 Your Rooms Energy Usage")
        
        rooms = st.session_state.user_profile['rooms']
        # Generate usage based on room type and user profile
        usage_data = []
        for room in rooms:
            base_usage = 200
            if 'bedroom' in room.lower():
                base_usage = 350
            elif 'living' in room.lower():
                base_usage = 450
            elif 'kitchen' in room.lower():
                base_usage = 400
            elif 'pool' in room.lower() and st.session_state.user_profile['home_type'] == 'Villa':
                base_usage = 600
            
            # Adjust based on family size
            adjusted_usage = base_usage + (st.session_state.user_profile['family_size'] * 10)
            usage_data.append(adjusted_usage)
        
        fig2 = px.bar(
            x=rooms, 
            y=usage_data,
            color=usage_data,
            color_continuous_scale=["#22C55E", "#F59E0B", "#EF4444"],
            title=""
        )
        fig2.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"},
            showlegend=False,
            xaxis_title="Your Rooms",
            yaxis_title="Energy Usage (W)"
        )
        st.plotly_chart(fig2, use_container_width=True)

with col2:
    # USER PROFILE SUMMARY
    st.markdown("### 👤 Your Profile")
    
    st.markdown(f"""
    <div class="user-card">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div style="font-size: 1.5rem; margin-right: 1rem;">🏠</div>
            <div>
                <div style="font-weight: bold;">{st.session_state.user_profile['home_type']}</div>
                <div style="opacity: 0.8; font-size: 0.9rem;">{st.session_state.user_profile['location']}</div>
            </div>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
            <span>Family Size:</span>
            <span style="font-weight: bold;">{st.session_state.user_profile['family_size']} people</span>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
            <span>AC Units:</span>
            <span style="font-weight: bold;">{st.session_state.user_profile['ac_units']} units</span>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
            <span>Bill Target:</span>
            <span style="font-weight: bold;">AED {st.session_state.user_profile['bill_target']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # PERSONALIZED SAVINGS RECOMMENDATIONS
    st.markdown("### 💡 Personalized Tips")
    
    recommendations = []
    
    # Generate personalized recommendations
    if st.session_state.user_profile['ac_units'] > 3:
        recommendations.append(("🌡️ AC Optimization", f"Optimize {st.session_state.user_profile['ac_units']} AC units", "Save AED 120+"))
    
    if st.session_state.user_profile['home_type'] == 'Villa':
        recommendations.append(("💧 Pool Management", "Smart pool scheduling", "Save AED 85+"))
    
    if st.session_state.user_profile['family_size'] > 4:
        recommendations.append(("👨‍👩‍👧‍👦 Family Scheduling", "Coordinate family usage", "Save AED 65+"))
    
    if any('kitchen' in room.lower() for room in st.session_state.user_profile['rooms']):
        recommendations.append(("🍳 Kitchen Efficiency", "Optimize cooking hours", "Save AED 45+"))
    
    # Add default recommendations
    recommendations.extend([
        ("💡 Peak Avoidance", "Shift heavy usage", "Save AED 75+"),
        ("🔌 Standby Power", "Reduce ghost loads", "Save AED 35+")
    ])
    
    for title, description, savings in recommendations[:4]:  # Show top 4
        st.markdown(f"""
        <div class="user-card" style="margin: 0.5rem 0; padding: 1rem;">
            <div style="font-weight: bold; color: #22C55E; margin-bottom: 0.5rem;">{title}</div>
            <div style="opacity: 0.9; font-size: 0.9rem; margin-bottom: 0.5rem;">{description}</div>
            <div style="color: #22C55E; font-weight: bold; font-size: 0.9rem;">{savings}</div>
        </div>
        """, unsafe_allow_html=True)

    # QUICK ACTIONS
    st.markdown("### 🚀 Quick Actions")
    
    if st.button("📊 Update My Data", use_container_width=True):
        st.info("Opening data update form...")
        # This would typically open a form or navigate to data entry
    
    if st.button("🎯 Recalculate Savings", use_container_width=True):
        # Recalculate based on current profile
        base_usage = 1200 if st.session_state.user_profile['home_type'] == "Apartment" else 1800 if st.session_state.user_profile['home_type'] == "Villa" else 1500
        usage_adjustment = (st.session_state.user_profile['ac_units'] * 120) + (st.session_state.user_profile['family_size'] * 60)
        
        st.session_state.energy_data.update({
            'current_usage': base_usage + usage_adjustment,
            'monthly_bill': int((base_usage + usage_adjustment) * 0.35)
        })
        st.success("✅ Savings recalculated based on your profile!")
        st.rerun()

# PROGRESS TOWARDS GOAL
st.markdown("### 🎯 Progress Towards Your Bill Target")
current_bill = st.session_state.energy_data['monthly_bill']
target_bill = st.session_state.user_profile['bill_target']
progress = max(0, min(100, (1 - (current_bill - target_bill) / target_bill) * 100)) if current_bill > target_bill else 100

st.progress(progress / 100)
col1, col2 = st.columns(2)
col1.metric("Current Bill", f"AED {current_bill}")
col2.metric("Your Target", f"AED {target_bill}", f"{progress:.1f}% achieved")

# DATA EXPORT OPTION
st.markdown("---")
if st.button("📥 Export My Energy Data", use_container_width=True):
    # Create downloadable data
    user_data = {
        'profile': st.session_state.user_profile,
        'energy_data': st.session_state.energy_data,
        'export_date': datetime.now().isoformat()
    }
    
    st.download_button(
        label="⬇️ Download JSON Data",
        data=json.dumps(user_data, indent=2),
        file_name=f"eterna_profile_{datetime.now().strftime('%Y%m%d')}.json",
        mime="application/json"
    )
