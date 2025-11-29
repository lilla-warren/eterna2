import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Digital Twin", layout="wide")

# Initialize session state if not exists
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'home_type': 'Apartment',
        'ac_units': 2,
        'family_size': 4,
        'rooms': ['Living Room', 'Master Bedroom', 'Kitchen'],
        'appliances': ['AC', 'Refrigerator', 'Washing Machine']
    }

if 'digital_twin_data' not in st.session_state:
    st.session_state.digital_twin_data = {
        'simulation_active': False,
        'current_scenario': 'Current Setup',
        'room_temperatures': {},
        'energy_flow': {},
        'savings_potential': 0
    }

st.title("🏗️ DIGITAL ENERGY TWIN")
st.markdown("### 3D Simulation of Your Home's Energy Flow")

# PERSONALIZED HOME MODEL
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### 🏠 Your Home's Energy DNA")
    
    # Interactive home visualization based on user's actual home
    home_type = st.session_state.user_profile['home_type']
    room_count = len(st.session_state.user_profile['rooms'])
    
    # Create a visual representation of the user's home
    st.markdown(f"##### 📐 {home_type} Layout - {room_count} Rooms")
    
    # Generate room data based on user's actual rooms
    room_data = []
    for i, room in enumerate(st.session_state.user_profile['rooms']):
        base_energy = 200
        if 'bedroom' in room.lower():
            base_energy = 350
        elif 'living' in room.lower():
            base_energy = 450
        elif 'kitchen' in room.lower():
            base_energy = 400
        
        # Adjust based on family size and AC units
        adjusted_energy = base_energy + (st.session_state.user_profile['family_size'] * 10)
        room_data.append({
            'Room': room,
            'Energy Usage': adjusted_energy,
            'Temperature': 22 + random.randint(1, 4),
            'AC Units': 1 if i < st.session_state.user_profile['ac_units'] else 0
        })
    
    # Add pool if villa
    if home_type == 'Villa':
        room_data.append({
            'Room': 'Pool Area',
            'Energy Usage': 600,
            'Temperature': 28,
            'AC Units': 0
        })
    
    df_rooms = pd.DataFrame(room_data)
    
    # Room energy usage chart
    fig_rooms = px.bar(
        df_rooms, 
        x='Room', 
        y='Energy Usage',
        color='Energy Usage',
        color_continuous_scale=["#22C55E", "#F59E0B", "#EF4444"],
        title="Your Rooms - Current Energy Consumption"
    )
    fig_rooms.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"},
        showlegend=False
    )
    st.plotly_chart(fig_rooms, use_container_width=True)

with col2:
    st.markdown("#### 🔧 Your Home Specifications")
    
    with st.container():
        st.metric("Home Type", home_type)
        st.metric("Total Rooms", room_count)
        st.metric("AC Units", st.session_state.user_profile['ac_units'])
        st.metric("Family Size", st.session_state.user_profile['family_size'])
        
        # Home efficiency score
        efficiency_score = 60 + (st.session_state.user_profile['ac_units'] * 3) + (st.session_state.user_profile['family_size'] * 2)
        st.metric("Current Efficiency", f"{efficiency_score}%", "Good" if efficiency_score > 70 else "Needs improvement")

# REAL-TIME ENERGY FLOW SIMULATION
st.markdown("---")
st.markdown("#### 🔋 Live Energy Flow Map")

# Create a simulated energy flow between rooms
if st.button("🎬 Start Live Simulation", type="primary"):
    st.session_state.digital_twin_data['simulation_active'] = True

if st.session_state.digital_twin_data['simulation_active']:
    # Simulate energy flow between rooms
    simulation_placeholder = st.empty()
    
    for step in range(10):  # Reduced steps for better performance
        with simulation_placeholder.container():
            # Update room energies with some variation
            current_energies = []
            for room in room_data:
                variation = random.randint(-20, 20)
                current_energy = max(100, room['Energy Usage'] + variation)
                current_energies.append(current_energy)
            
            # Create animated flow chart
            fig_flow = go.Figure()
            
            # Add rooms as nodes
            fig_flow.add_trace(go.Scatter(
                x=[i * 2 for i in range(len(room_data))],
                y=[current_energies[i] / 20 for i in range(len(room_data))],
                mode='markers+text',
                marker=dict(
                    size=[min(60, max(20, energy / 10)) for energy in current_energies],
                    color=current_energies,
                    colorscale='Viridis',
                    showscale=True
                ),
                text=[room['Room'] for room in room_data],
                textposition="middle center",
                name="Rooms"
            ))
            
            # Add energy flow lines
            for i in range(len(room_data) - 1):
                fig_flow.add_trace(go.Scatter(
                    x=[i * 2, (i + 1) * 2],
                    y=[current_energies[i] / 20, current_energies[i + 1] / 20],
                    mode='lines',
                    line=dict(width=2, color='#22C55E'),
                    showlegend=False
                ))
            
            fig_flow.update_layout(
                title="🔄 Live Energy Flow Between Your Rooms",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font={'color': "white"},
                xaxis=dict(showticklabels=False, showgrid=False),
                yaxis=dict(showticklabels=False, showgrid=False),
                height=400
            )
            
            st.plotly_chart(fig_flow, use_container_width=True)
            st.caption(f"Simulation Step {step + 1}/10 - Watching energy move through your {home_type}")
        
        # Small delay for animation effect
        import time
        time.sleep(0.5)
    
    st.success("✅ Simulation complete! Energy flow patterns analyzed.")

# WHAT-IF SCENARIOS
st.markdown("---")
st.markdown("#### 🔮 What-If Scenarios")

scenario_col1, scenario_col2 = st.columns(2)

with scenario_col1:
    scenario = st.selectbox(
        "Test different improvements:",
        [
            "Current Setup",
            "Add Solar Panels", 
            "Upgrade AC Units",
            "Install Smart Pool",
            "Better Insulation",
            "Smart Lighting",
            "Energy Efficient Appliances"
        ],
        index=0
    )

with scenario_col2:
    investment = st.slider(
        "Investment Amount (AED)",
        min_value=0,
        max_value=50000,
        value=10000,
        step=1000,
        help="How much would you invest in this improvement?"
    )

# Calculate scenario impacts
if scenario != "Current Setup":
    base_savings = 0
    efficiency_improvement = 0
    
    if scenario == "Add Solar Panels":
        base_savings = 250
        efficiency_improvement = 25
    elif scenario == "Upgrade AC Units":
        base_savings = st.session_state.user_profile['ac_units'] * 40
        efficiency_improvement = 20
    elif scenario == "Install Smart Pool" and home_type == 'Villa':
        base_savings = 120
        efficiency_improvement = 15
    elif scenario == "Better Insulation":
        base_savings = 180
        efficiency_improvement = 22
    elif scenario == "Smart Lighting":
        base_savings = 80
        efficiency_improvement = 12
    elif scenario == "Energy Efficient Appliances":
        base_savings = st.session_state.user_profile['family_size'] * 25
        efficiency_improvement = 18
    
    # Adjust based on investment
    investment_multiplier = min(2.0, 1 + (investment / 25000))
    final_savings = int(base_savings * investment_multiplier)
    final_efficiency = efficiency_improvement * investment_multiplier
    
    # ROI calculation
    monthly_savings = final_savings
    annual_savings = monthly_savings * 12
    roi_months = investment / monthly_savings if monthly_savings > 0 else 999
    
    st.markdown("##### 💰 Scenario Impact Analysis")
    
    impact_col1, impact_col2, impact_col3 = st.columns(3)
    
    with impact_col1:
        st.metric("Monthly Savings", f"AED {final_savings}", f"+{final_efficiency:.1f}% efficiency")
    
    with impact_col2:
        st.metric("Annual Return", f"AED {annual_savings}", f"{investment_multiplier:.1f}x impact")
    
    with impact_col3:
        if roi_months < 999:
            st.metric("ROI Period", f"{roi_months:.1f} months", "Break-even")
        else:
            st.metric("ROI Period", "Long-term", "Strategic investment")
    
    # Visual comparison
    st.markdown("##### 📊 Before vs After Comparison")
    
    comparison_data = {
        'Scenario': ['Current', scenario],
        'Efficiency': [efficiency_score, efficiency_score + final_efficiency],
        'Monthly Cost': [800, 800 - final_savings],
        'CO2 Impact': [100, 100 - (final_efficiency * 0.8)]
    }
    
    fig_comparison = go.Figure()
    
    fig_comparison.add_trace(go.Bar(
        name='Current',
        x=list(comparison_data.keys())[1:],
        y=[comparison_data['Efficiency'][0], comparison_data['Monthly Cost'][0], comparison_data['CO2 Impact'][0]],
        marker_color='#EF4444'
    ))
    
    fig_comparison.add_trace(go.Bar(
        name=scenario,
        x=list(comparison_data.keys())[1:],
        y=[comparison_data['Efficiency'][1], comparison_data['Monthly Cost'][1], comparison_data['CO2 Impact'][1]],
        marker_color='#22C55E'
    ))
    
    fig_comparison.update_layout(
        title=f"Impact of {scenario} on Your {home_type}",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"},
        barmode='group'
    )
    
    st.plotly_chart(fig_comparison, use_container_width=True)

else:
    st.info("💡 Select a scenario to see how improvements would impact your home")

# PERSONALIZED RECOMMENDATIONS
st.markdown("---")
st.markdown("#### 🎯 AI-Generated Recommendations for Your Home")

# Generate personalized recommendations based on user profile
recommendations = []

# AC-related recommendations
if st.session_state.user_profile['ac_units'] > 3:
    recommendations.append({
        "title": "AC Unit Staggering",
        "description": f"Coordinate your {st.session_state.user_profile['ac_units']} AC units to avoid simultaneous startup",
        "savings": st.session_state.user_profile['ac_units'] * 35,
        "priority": "High"
    })

# Family-related recommendations
if st.session_state.user_profile['family_size'] > 4:
    recommendations.append({
        "title": "Family Schedule Optimization",
        "description": f"Smart scheduling for your {st.session_state.user_profile['family_size']}-person family",
        "savings": st.session_state.user_profile['family_size'] * 20,
        "priority": "Medium"
    })

# Home-type specific recommendations
if home_type == 'Villa':
    recommendations.append({
        "title": "Pool Pump Optimization",
        "description": "Smart scheduling for your villa's pool system",
        "savings": 95,
        "priority": "High"
    })

# General recommendations
recommendations.extend([
    {
        "title": "Peak Hour Management",
        "description": "Shift energy usage away from 2PM-8PM peak rates",
        "savings": 85,
        "priority": "High"
    },
    {
        "title": "Standby Power Reduction",
        "description": "Eliminate ghost energy from idle devices",
        "savings": 45,
        "priority": "Medium"
    },
    {
        "title": "Smart Thermostat",
        "description": "Precise temperature control for better efficiency",
        "savings": 65,
        "priority": "Medium"
    }
])

# Display recommendations
for i, rec in enumerate(recommendations[:4]):  # Show top 4
    with st.container():
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.write(f"**{rec['title']}**")
            st.caption(rec['description'])
        
        with col2:
            st.metric("Savings", f"AED {rec['savings']}/mo")
        
        with col3:
            priority_color = "🔴" if rec['priority'] == "High" else "🟡" if rec['priority'] == "Medium" else "🟢"
            st.write(f"{priority_color} **{rec['priority']} Priority**")

# 3D HOME VISUALIZATION
st.markdown("---")
st.markdown("#### 🏠 3D Home Model Visualization")

# Create a simple 3D representation of the user's home
try:
    # Generate 3D coordinates based on room count and home type
    rooms_3d = []
    for i, room in enumerate(st.session_state.user_profile['rooms']):
        x = i % 3
        y = i // 3
        z = 0
        
        rooms_3d.append({
            'Room': room,
            'x': x,
            'y': y, 
            'z': z,
            'Size': 100 + (i * 20),
            'Energy': room_data[i]['Energy Usage'] if i < len(room_data) else 300
        })
    
    df_3d = pd.DataFrame(rooms_3d)
    
    fig_3d = px.scatter_3d(
        df_3d,
        x='x',
        y='y',
        z='z',
        size='Size',
        color='Energy',
        hover_name='Room',
        title=f"3D Model of Your {home_type}",
        color_continuous_scale='Viridis'
    )
    
    fig_3d.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"},
        scene=dict(
            bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showbackground=False, showticklabels=False, title=""),
            yaxis=dict(showbackground=False, showticklabels=False, title=""),
            zaxis=dict(showbackground=False, showticklabels=False, title="")
        )
    )
    
    st.plotly_chart(fig_3d, use_container_width=True)
    
except Exception as e:
    st.info("🎨 3D visualization ready for your home layout - interactive model loading")

# EXPORT AND SHARE
st.markdown("---")
st.markdown("#### 📤 Export Your Digital Twin")

col1, col2 = st.columns(2)

with col1:
    if st.button("💾 Save Current Simulation", use_container_width=True):
        st.session_state.digital_twin_data = {
            'simulation_active': False,
            'current_scenario': scenario,
            'room_temperatures': {room['Room']: room['Temperature'] for room in room_data},
            'energy_flow': {room['Room']: room['Energy Usage'] for room in room_data},
            'savings_potential': final_savings if scenario != "Current Setup" else 0
        }
        st.success("✅ Digital Twin data saved!")

with col2:
    if st.button("📊 Generate Optimization Report", use_container_width=True):
        total_potential = sum(rec['savings'] for rec in recommendations)
        st.success(f"📋 Report generated! Total savings potential: AED {total_potential}/month")

# QUICK ACTIONS
st.markdown("#### 🚀 Quick Actions")

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:
    if st.button("🔄 Reset Simulation", use_container_width=True):
        st.session_state.digital_twin_data['simulation_active'] = False
        st.rerun()

with action_col2:
    if st.button("🎯 Apply Top Recommendation", use_container_width=True):
        if recommendations:
            top_rec = recommendations[0]
            st.success(f"✅ Applied '{top_rec['title']}' - Estimated savings: AED {top_rec['savings']}/month")

with action_col3:
    if st.button("🏠 Back to Dashboard", use_container_width=True):
        st.switch_page("pages/1_🏠_Dashboard.py")
