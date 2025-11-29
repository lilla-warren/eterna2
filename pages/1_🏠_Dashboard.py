import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Dashboard", layout="wide")

# Initialize session state for user data with ALL required fields
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'home_type': 'Apartment',
        'ac_units': 2,
        'family_size': 4,
        'location': 'Dubai',
        'bill_target': 400,  # Added missing field
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
    
    .emergency-alert {
        background: linear-gradient(45deg, #EF4444, #DC2626);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .success-alert {
        background: linear-gradient(45deg, #22C55E, #16A34A);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
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
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
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
            value=st.session_state.user_profile.get('bill_target', 400)  # Safe access
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

    # QUICK STATS
    st.markdown("---")
    st.markdown("### 📈 Quick Stats")
    
    efficiency = min(95, 60 + (st.session_state.user_profile['ac_units'] * 3) + (st.session_state.user_profile['family_size'] * 2))
    
    st.metric("Efficiency Score", f"{efficiency}%")
    st.metric("AC Units", st.session_state.user_profile['ac_units'])
    st.metric("Family Members", st.session_state.user_profile['family_size'])
    st.metric("Rooms", len(st.session_state.user_profile['rooms']))

# MAIN DASHBOARD CONTENT
col1, col2 = st.columns([2, 1])

with col1:
    # PERSONALIZED METRICS WITH ENHANCED VISUALS
    st.markdown("### 📊 Your Energy Snapshot")
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        current_bill = st.session_state.energy_data['monthly_bill']
        target_bill = st.session_state.user_profile.get('bill_target', 400)
        bill_diff = current_bill - target_bill
        
        st.markdown(f"""
        <div class="user-card {'pulse' if bill_diff > 50 else ''}">
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
        usage_trend = "🔻" if st.session_state.energy_data['current_usage'] < 1600 else "🔺"
        st.markdown(f"""
        <div class="user-card">
            <div style="font-size: 1.2rem; font-weight: bold; color: #22C55E;">
                {st.session_state.energy_data['current_usage']}W
            </div>
            <div style="opacity: 0.8;">Live Usage</div>
            <div style="color: #22C55E; font-size: 0.9rem;">
                {usage_trend} Optimized for {st.session_state.user_profile['home_type']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        efficiency = min(95, 60 + (st.session_state.user_profile['ac_units'] * 3) + (st.session_state.user_profile['family_size'] * 2))
        status = "Excellent" if efficiency > 80 else "Good" if efficiency > 65 else "Needs improvement"
        status_color = "#22C55E" if efficiency > 80 else "#F59E0B" if efficiency > 65 else "#EF4444"
        
        st.markdown(f"""
        <div class="user-card">
            <div style="font-size: 1.2rem; font-weight: bold; color: {status_color};">
                {efficiency}%
            </div>
            <div style="opacity: 0.8;">Efficiency Score</div>
            <div style="color: {status_color}; font-size: 0.9rem;">
                {status}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ENHANCED EFFICIENCY GAUGE WITH MORE DETAILS
    st.markdown("### 🎯 Your Efficiency Progress")
    
    gauge_col1, gauge_col2 = st.columns([3, 1])
    
    with gauge_col1:
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
    
    with gauge_col2:
        st.markdown("#### 📈 Insights")
        st.write(f"**Home Type:** {st.session_state.user_profile['home_type']}")
        st.write(f"**AC Units:** {st.session_state.user_profile['ac_units']}")
        st.write(f"**Family Size:** {st.session_state.user_profile['family_size']}")
        st.write(f"**Location:** {st.session_state.user_profile['location']}")
        
        # Quick tip based on efficiency
        if efficiency < 70:
            st.error("💡 **Tip:** Consider AC optimization")
        elif efficiency < 85:
            st.warning("💡 **Tip:** Good, but can improve")
        else:
            st.success("💡 **Tip:** Excellent efficiency!")

    # ENHANCED ROOMS ENERGY USAGE WITH INTERACTIVITY
    if st.session_state.user_profile['rooms']:
        st.markdown("### 🏠 Your Rooms Energy Usage")
        
        rooms = st.session_state.user_profile['rooms']
        # Generate usage based on room type and user profile
        usage_data = []
        colors = []
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
            
            # Color coding based on usage
            if adjusted_usage > 450:
                colors.append('#EF4444')  # High usage - red
            elif adjusted_usage > 300:
                colors.append('#F59E0B')  # Medium usage - yellow
            else:
                colors.append('#22C55E')  # Low usage - green
        
        fig2 = px.bar(
            x=rooms, 
            y=usage_data,
            color=usage_data,
            color_continuous_scale=["#22C55E", "#F59E0B", "#EF4444"],
            title="Energy Consumption by Room"
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
        
        # Room optimization tips
        st.markdown("#### 💡 Room-Specific Tips")
        room_tips_col1, room_tips_col2 = st.columns(2)
        
        with room_tips_col1:
            for i, room in enumerate(rooms):
                if usage_data[i] > 400:
                    st.warning(f"**{room}**: High usage - consider optimization")
        
        with room_tips_col2:
            for i, room in enumerate(rooms):
                if 'bedroom' in room.lower() and usage_data[i] > 350:
                    st.info(f"**{room}**: Try increasing AC temperature by 1-2°C")

with col2:
    # ENHANCED USER PROFILE SUMMARY
    st.markdown("### 👤 Your Profile")
    
    st.markdown(f"""
    <div class="user-card">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div style="font-size: 2rem; margin-right: 1rem;">🏠</div>
            <div>
                <div style="font-weight: bold; font-size: 1.2rem;">{st.session_state.user_profile['home_type']}</div>
                <div style="opacity: 0.8; font-size: 0.9rem;">📍 {st.session_state.user_profile['location']}</div>
            </div>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.8rem 0; padding: 0.5rem; background: rgba(255,255,255,0.1); border-radius: 8px;">
            <span>👨‍👩‍👧‍👦 Family:</span>
            <span style="font-weight: bold;">{st.session_state.user_profile['family_size']} people</span>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.8rem 0; padding: 0.5rem; background: rgba(255,255,255,0.1); border-radius: 8px;">
            <span>❄️ AC Units:</span>
            <span style="font-weight: bold;">{st.session_state.user_profile['ac_units']} units</span>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.8rem 0; padding: 0.5rem; background: rgba(255,255,255,0.1); border-radius: 8px;">
            <span>🎯 Bill Target:</span>
            <span style="font-weight: bold; color: #22C55E;">AED {st.session_state.user_profile.get('bill_target', 400)}</span>
        </div>
        
        <div style="display: flex; justify-content: space-between; margin: 0.8rem 0; padding: 0.5rem; background: rgba(255,255,255,0.1); border-radius: 8px;">
            <span>🚪 Rooms:</span>
            <span style="font-weight: bold;">{len(st.session_state.user_profile['rooms'])} rooms</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ENHANCED PERSONALIZED SAVINGS RECOMMENDATIONS
    st.markdown("### 💡 Personalized Tips")
    
    recommendations = []
    
    # Generate personalized recommendations based on user profile
    if st.session_state.user_profile['ac_units'] > 3:
        savings = st.session_state.user_profile['ac_units'] * 35
        recommendations.append(("🌡️ AC Optimization", f"Optimize {st.session_state.user_profile['ac_units']} AC units", f"Save AED {savings}+", "high"))
    
    if st.session_state.user_profile['home_type'] == 'Villa':
        recommendations.append(("💧 Pool Management", "Smart pool scheduling", "Save AED 85+", "medium"))
    
    if st.session_state.user_profile['family_size'] > 4:
        savings = st.session_state.user_profile['family_size'] * 15
        recommendations.append(("👨‍👩‍👧‍👦 Family Scheduling", "Coordinate family usage", f"Save AED {savings}+", "medium"))
    
    if any('kitchen' in room.lower() for room in st.session_state.user_profile['rooms']):
        recommendations.append(("🍳 Kitchen Efficiency", "Optimize cooking hours", "Save AED 45+", "low"))
    
    # Add default recommendations
    recommendations.extend([
        ("💡 Peak Avoidance", "Shift heavy usage to off-peak", "Save AED 75+", "high"),
        ("🔌 Standby Power", "Reduce ghost loads", "Save AED 35+", "medium"),
        ("🌅 Morning Routine", "Optimize morning energy use", "Save AED 25+", "low")
    ])
    
    for title, description, savings, priority in recommendations[:5]:  # Show top 5
        priority_color = "#EF4444" if priority == "high" else "#F59E0B" if priority == "medium" else "#22C55E"
        priority_icon = "🔴" if priority == "high" else "🟡" if priority == "medium" else "🟢"
        
        st.markdown(f"""
        <div class="user-card" style="margin: 0.5rem 0; padding: 1rem; border-left: 4px solid {priority_color};">
            <div style="display: flex; justify-content: between; align-items: start;">
                <div style="flex: 1;">
                    <div style="font-weight: bold; color: {priority_color}; margin-bottom: 0.3rem;">{title}</div>
                    <div style="opacity: 0.9; font-size: 0.85rem; margin-bottom: 0.5rem;">{description}</div>
                    <div style="color: {priority_color}; font-weight: bold; font-size: 0.9rem;">{savings}</div>
                </div>
                <div style="font-size: 1.2rem;">{priority_icon}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ENHANCED QUICK ACTIONS
    st.markdown("### 🚀 Quick Actions")
    
    action_col1, action_col2 = st.columns(2)
    
    with action_col1:
        if st.button("📊 Update Data", use_container_width=True, use_container_width=True):
            st.success("Data sync initiated!")
            
        if st.button("🔄 Recalculate", use_container_width=True):
            base_usage = 1200 if st.session_state.user_profile['home_type'] == "Apartment" else 1800 if st.session_state.user_profile['home_type'] == "Villa" else 1500
            usage_adjustment = (st.session_state.user_profile['ac_units'] * 120) + (st.session_state.user_profile['family_size'] * 60)
            
            st.session_state.energy_data.update({
                'current_usage': base_usage + usage_adjustment,
                'monthly_bill': int((base_usage + usage_adjustment) * 0.35)
            })
            st.success("✅ Savings recalculated!")
            st.rerun()
    
    with action_col2:
        if st.button("📈 View Reports", use_container_width=True):
            st.switch_page("pages/2_📈_Energy_Reports.py")
            
        if st.button("🛡️ Bill Shield", use_container_width=True):
            st.switch_page("pages/3_🛡️_Bill_Shield.py")

# ENHANCED PROGRESS TOWARDS GOAL
st.markdown("### 🎯 Progress Towards Your Bill Target")

current_bill = st.session_state.energy_data['monthly_bill']
target_bill = st.session_state.user_profile.get('bill_target', 400)
progress = max(0, min(100, (1 - (current_bill - target_bill) / target_bill) * 100)) if current_bill > target_bill else 100

# Enhanced progress display
progress_col1, progress_col2, progress_col3 = st.columns([2, 1, 1])

with progress_col1:
    st.progress(progress / 100)
    
    if progress < 50:
        st.markdown(f'<div class="emergency-alert">🚨 You are AED {current_bill - target_bill} above target</div>', unsafe_allow_html=True)
    elif progress < 80:
        st.markdown(f'<div style="background: rgba(234, 179, 8, 0.2); padding: 1rem; border-radius: 10px; border: 1px solid #F59E0B;">⚠️ Close to target - AED {current_bill - target_bill} above</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="success-alert">✅ On track! AED {target_bill - current_bill} under target</div>', unsafe_allow_html=True)

with progress_col2:
    st.metric("Current Bill", f"AED {current_bill}")

with progress_col3:
    st.metric("Your Target", f"AED {target_bill}", f"{progress:.1f}%")

# ENHANCED DATA EXPORT OPTION
st.markdown("---")
export_col1, export_col2 = st.columns([3, 1])

with export_col1:
    st.markdown("#### 📥 Export Your Data")
    st.write("Download your complete energy profile and usage data for analysis")

with export_col2:
    if st.button("📊 Export Data", use_container_width=True):
        # Create downloadable data
        user_data = {
            'profile': st.session_state.user_profile,
            'energy_data': st.session_state.energy_data,
            'export_date': datetime.now().isoformat(),
            'summary': {
                'efficiency_score': efficiency,
                'monthly_savings_potential': sum([120, 85, 65, 45, 75, 35]),  # Example total
                'recommendations_count': len(recommendations)
            }
        }
        
        st.download_button(
            label="⬇️ Download JSON",
            data=json.dumps(user_data, indent=2),
            file_name=f"eterna_dashboard_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
            mime="application/json",
            use_container_width=True
        )

# REAL-TIME ALERTS SECTION
st.markdown("---")
st.markdown("### ⚡ Real-time Alerts")

alert_col1, alert_col2, alert_col3 = st.columns(3)

with alert_col1:
    if current_bill > target_bill + 100:
        st.error("🚨 **High Bill Alert**\n\nYou're significantly above your target bill")
    else:
        st.success("✅ **Bill Status: Normal**\n\nYou're within your target range")

with alert_col2:
    if st.session_state.user_profile['ac_units'] > 5:
        st.warning("⚠️ **AC Usage High**\n\nConsider optimizing your AC units")
    else:
        st.info("❄️ **AC Usage: Optimal**\n\nYour AC configuration is efficient")

with alert_col3:
    if efficiency < 70:
        st.error("📉 **Efficiency Low**\n\nCheck recommendations for improvements")
    else:
        st.success("📈 **Efficiency: Good**\n\nKeep up the good work!")
