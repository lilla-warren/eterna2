import streamlit as st
import time
import random
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Live Orchestrator", layout="wide")

# Initialize session state if not exists
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'home_type': 'Apartment',
        'ac_units': 2,
        'family_size': 4,
        'rooms': ['Living Room', 'Master Bedroom', 'Kitchen'],
        'appliances': ['AC', 'Refrigerator', 'Washing Machine']
    }

if 'orchestrator_settings' not in st.session_state:  # FIXED: Changed key name
    st.session_state.orchestrator_settings = {
        'priority': 'Balance Savings & Comfort',
        'schedule': 'Family Day',
        'features': ['Peak Avoidance', 'Standby Reduction']
    }

# ANIMATED CSS FOR ORCHESTRATOR
st.markdown("""
<style>
    .orchestrator-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .device-status {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.08);
        transition: all 0.3s ease;
    }
    
    .device-status.optimizing {
        border-left: 4px solid #F59E0B;
        background: rgba(245, 158, 11, 0.1);
    }
    
    .device-status.optimized {
        border-left: 4px solid #22C55E;
        background: rgba(34, 197, 94, 0.1);
    }
    
    .device-status.efficient {
        border-left: 4px solid #3B82F6;
        background: rgba(59, 130, 246, 0.1);
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    .live-pulse {
        width: 12px;
        height: 12px;
        background: #22C55E;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        animation: pulse 1.5s infinite;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ LIVE ENERGY ORCHESTRATOR")
st.markdown("### <span class='live-pulse'></span>AI-Powered Home Coordination", unsafe_allow_html=True)

# PERSONALIZED ORCHESTRATION SETUP
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎵 Your Home Orchestra")
    
    # Show user's actual devices based on their profile
    user_devices = []
    
    # Add AC units based on user's actual count
    for i in range(st.session_state.user_profile['ac_units']):
        room_name = f"AC Unit {i+1}"
        if i < len(st.session_state.user_profile['rooms']):
            room_name = f"{st.session_state.user_profile['rooms'][i]} AC"
        user_devices.append((f"🌡️ {room_name}", "ac", 40))
    
    # Add other devices based on user's appliances and home type
    if 'Refrigerator' in st.session_state.user_profile['appliances']:
        user_devices.append(("❄️ Refrigerator", "appliance", 25))
    
    if 'Washing Machine' in st.session_state.user_profile['appliances']:
        user_devices.append(("👕 Washing Machine", "appliance", 35))
    
    if 'Water Heater' in st.session_state.user_profile['appliances']:
        user_devices.append(("🔥 Water Heater", "appliance", 45))
    
    # Add home-type specific devices
    if st.session_state.user_profile['home_type'] == 'Villa':
        user_devices.append(("💧 Pool Pump", "pool", 85))
        user_devices.append(("💡 Garden Lighting", "lighting", 30))
    
    user_devices.extend([
        ("💡 Living Room Lighting", "lighting", 20),
        ("📺 Entertainment System", "electronics", 25),
        ("💻 Home Office", "electronics", 30)
    ])
    
    # Display user's actual devices
    st.markdown(f"#### 📱 Your {len(user_devices)} Devices Ready for Optimization")
    
    for device, category, max_savings in user_devices:
        st.markdown(f"""
        <div class="device-status">
            <div>
                <div style="font-weight: bold; font-size: 1.1rem;">{device}</div>
                <div style="opacity: 0.8; font-size: 0.9rem;">Ready for AI optimization</div>
            </div>
            <div style="text-align: right;">
                <div style="color: #22C55E; font-weight: bold;">Up to AED {max_savings}/mo</div>
                <div style="opacity: 0.7; font-size: 0.8rem;">{category.title()}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎯 Orchestration Settings")
    
    with st.form("orchestration_settings"):
        st.subheader("⚙️ Optimization Preferences")
        
        # Personalized settings based on user profile
        priority = st.selectbox(
            "Optimization Priority",
            ["Maximum Savings", "Balance Savings & Comfort", "Maximum Comfort"],
            help="Choose your preference for the AI optimization",
            index=["Maximum Savings", "Balance Savings & Comfort", "Maximum Comfort"].index(
                st.session_state.orchestrator_settings['priority']
            )
        )
        
        schedule_type = st.selectbox(
            "Daily Schedule",
            ["Family Day", "Work From Home", "Weekend", "Ramadan", "Summer"],
            help="Select your typical daily pattern",
            index=["Family Day", "Work From Home", "Weekend", "Ramadan", "Summer"].index(
                st.session_state.orchestrator_settings['schedule']
            )
        )
        
        # Smart features based on user's home
        smart_features = []
        if st.session_state.user_profile['ac_units'] > 2:
            smart_features.append("AC Staggering")
        if st.session_state.user_profile['home_type'] == 'Villa':
            smart_features.append("Pool Optimization")
        if st.session_state.user_profile['family_size'] > 3:
            smart_features.append("Family Scheduling")
        
        smart_features.extend(["Peak Avoidance", "Standby Reduction"])
        
        enabled_features = st.multiselect(
            "Smart Features",
            smart_features,
            default=st.session_state.orchestrator_settings['features'],
            help="Select which AI features to enable"
        )
        
        if st.form_submit_button("💾 Save Settings", use_container_width=True):
            # FIXED: Use the correct session state key
            st.session_state.orchestrator_settings = {
                'priority': priority,
                'schedule': schedule_type,
                'features': enabled_features
            }
            st.success("✅ Settings saved!")
            st.rerun()

# LIVE ORCHESTRATION DEMO
st.markdown("---")
st.markdown("### 🎬 Live Orchestration Demo")

if st.button("🚀 START PERSONALIZED ORCHESTRATION", type="primary", use_container_width=True):
    
    # Initialize orchestration state
    orchestration_state = {device[0]: {
        'status': 'pending',
        'savings': 0,
        'progress': 0,
        'category': device[1],
        'max_savings': device[2]
    } for device in user_devices}
    
    # Create progress containers
    progress_bar = st.progress(0)
    status_text = st.empty()
    devices_container = st.empty()
    metrics_container = st.empty()
    
    total_savings = 0
    completed_devices = 0
    
    # Simulate orchestration process
    for step in range(101):
        progress_bar.progress(step)
        status_text.text(f"🔄 AI orchestrating your {st.session_state.user_profile['home_type']}... {step}% complete")
        
        # Update device statuses
        if step % 15 == 0 and step > 0:
            for device_name, device_data in orchestration_state.items():
                if device_data['status'] == 'pending' and random.random() > 0.6:
                    device_data['status'] = random.choice(['optimizing', 'optimized', 'efficient'])
                    device_data['savings'] = random.randint(device_data['max_savings'] // 2, device_data['max_savings'])
                    device_data['progress'] = 100 if device_data['status'] == 'optimized' else random.randint(50, 90)
                    
                    if device_data['status'] == 'optimized':
                        completed_devices += 1
        
        # Calculate total savings
        total_savings = sum(device['savings'] for device in orchestration_state.values())
        
        # Update metrics
        with metrics_container.container():
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Savings", f"AED {total_savings}/month")
            col2.metric("Devices Optimized", f"{completed_devices}/{len(user_devices)}")
            col3.metric("Efficiency Gain", f"{min(85, 40 + (step // 1.2))}%")
            col4.metric("Time Saved", f"{step // 4} min")
        
        # Update devices display with progress
        with devices_container.container():
            st.markdown("#### 📊 Device Optimization Progress")
            
            for device_name, device_data in orchestration_state.items():
                status_emoji = {
                    'pending': '⏳',
                    'optimizing': '🔄', 
                    'optimized': '✅',
                    'efficient': '⚡'
                }[device_data['status']]
                
                status_class = {
                    'pending': '',
                    'optimizing': 'optimizing',
                    'optimized': 'optimized', 
                    'efficient': 'efficient'
                }[device_data['status']]
                
                st.markdown(f"""
                <div class="device-status {status_class}">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <div style="font-size: 1.5rem;">{status_emoji}</div>
                        <div>
                            <div style="font-weight: bold;">{device_name}</div>
                            <div style="opacity: 0.8; font-size: 0.9rem;">
                                {device_data['status'].title()}
                            </div>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: #22C55E; font-weight: bold;">AED {device_data['savings']}/mo</div>
                        <div style="opacity: 0.7; font-size: 0.8rem;">
                            {device_data['progress']}% complete
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        time.sleep(0.1)
    
    # Final results
    progress_bar.empty()
    status_text.empty()
    
    st.balloons()
    st.success(f"🎉 ORCHESTRATION COMPLETE! Achieved AED {total_savings}/month in personalized savings!")
    
    # Show personalized results
    st.markdown("### 📈 Your Personalized Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Savings breakdown by category
        category_savings = {}
        for device_data in orchestration_state.values():
            category = device_data['category']
            if category not in category_savings:
                category_savings[category] = 0
            category_savings[category] += device_data['savings']
        
        fig1 = go.Figure(data=[go.Pie(
            labels=list(category_savings.keys()),
            values=list(category_savings.values()),
            hole=.3,
            marker_colors=['#22C55E', '#3B82F6', '#F59E0B', '#EF4444', '#8B5CF6']
        )])
        fig1.update_layout(
            title="Savings by Category",
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"}
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Efficiency improvement
        phases = ["Before", "After Optimization"]
        base_efficiency = 60
        improved_efficiency = min(95, base_efficiency + (st.session_state.user_profile['ac_units'] * 3) + (st.session_state.user_profile['family_size'] * 2))
        
        fig2 = go.Figure(data=[
            go.Bar(
                name='Efficiency Score', 
                x=phases, 
                y=[base_efficiency, improved_efficiency],
                marker_color=['#EF4444', '#22C55E']
            )
        ])
        fig2.update_layout(
            title="Efficiency Improvement",
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"},
            showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)

# QUICK ACTIONS FOR USER'S SPECIFIC HOME
st.markdown("---")
st.markdown("### 🎮 Quick Actions for Your Home")

quick_col1, quick_col2, quick_col3 = st.columns(3)

with quick_col1:
    if st.button("🌡️ Optimize All AC Units", use_container_width=True):
        st.info(f"🔄 Optimizing your {st.session_state.user_profile['ac_units']} AC units...")
        time.sleep(1)
        st.success(f"✅ {st.session_state.user_profile['ac_units']} AC units optimized! Estimated savings: AED {st.session_state.user_profile['ac_units'] * 40}/month")

with quick_col2:
    if st.button("💡 Smart Lighting", use_container_width=True):
        st.info("🔄 Implementing smart lighting schedules...")
        time.sleep(1)
        st.success("✅ Lighting optimized! Estimated savings: AED 45/month")

with quick_col3:
    if st.button("📊 Generate Report", use_container_width=True):
        st.info("📋 Generating personalized optimization report...")
        time.sleep(2)
        st.success(f"✅ Report generated for your {st.session_state.user_profile['home_type']}!")

# PERSONALIZED INSIGHTS
st.markdown("---")
st.markdown("### 💡 Personalized AI Insights")

insights = [
    f"🏠 **Your {st.session_state.user_profile['home_type']}**: Perfect for whole-home orchestration",
    f"🌡️ **{st.session_state.user_profile['ac_units']} AC Units**: Staggered startup can save AED {st.session_state.user_profile['ac_units'] * 35}/month",
    f"👨‍👩‍👧‍👦 **Family of {st.session_state.user_profile['family_size']}**: Smart scheduling can optimize family patterns",
]

if st.session_state.user_profile['home_type'] == 'Villa':
    insights.append("💧 **Pool System**: Optimal pump scheduling can save AED 85+/month")

for insight in insights:
    st.markdown(f"""
    <div class="orchestrator-card">
        <div style="display: flex; align-items: start; gap: 1rem;">
            <div style="font-size: 1.2rem;">💡</div>
            <div>{insight}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
