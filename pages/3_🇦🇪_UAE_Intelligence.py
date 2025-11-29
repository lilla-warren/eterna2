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

# FIX: Add location if missing
if 'location' not in st.session_state.user_profile:
    st.session_state.user_profile['location'] = 'Dubai'

if 'uai_settings' not in st.session_state:
    st.session_state.uai_settings = {
        'ramadan_mode': True,
        'summer_optimization': True,
        'family_patterns': True,
        'desert_adaptation': True
    }

# PREMIUM ANIMATED CSS FOR UAE INTELLIGENCE
st.markdown("""
<style>
    .uae-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        border-left: 4px solid;
    }
    
    .uae-card.ramadan {
        border-left-color: #8B5CF6;
        background: rgba(139, 92, 246, 0.1);
    }
    
    .uae-card.summer {
        border-left-color: #F59E0B;
        background: rgba(245, 158, 11, 0.1);
    }
    
    .uae-card.family {
        border-left-color: #22C55E;
        background: rgba(34, 197, 94, 0.1);
    }
    
    .uae-card.desert {
        border-left-color: #EF4444;
        background: rgba(239, 68, 68, 0.1);
    }
    
    .uae-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }
    
    @keyframes slideInFromRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .slide-in-right {
        animation: slideInFromRight 0.8s ease-out;
    }
    
    .pattern-bar {
        height: 8px;
        background: linear-gradient(90deg, #22C55E, #3B82F6, #8B5CF6, #F59E0B);
        border-radius: 4px;
        margin: 0.5rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .pattern-bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .cultural-badge {
        background: linear-gradient(45deg, #8B5CF6, #A855F7);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.25rem;
        animation: pulse 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

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
        
        # FIX: Add location selector
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
            # FIX: Save location to user profile
            st.session_state.user_profile['location'] = location
            st.success("✅ UAE settings saved!")
            st.rerun()

# MAIN CONTENT - PERSONALIZED UAE INTELLIGENCE
tab1, tab2, tab3, tab4 = st.tabs(["🌙 Ramadan AI", "☀️ Summer AI", "👨‍👩‍👧‍👦 Family AI", "🏜️ Desert AI"])

with tab1:
    st.markdown("### 🌙 Ramadan Energy Intelligence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="uae-card ramadan slide-in-right">
            <h3>🕌 Your Ramadan Patterns</h3>
            <p>Based on your <strong>family of {st.session_state.user_profile['family_size']}</strong> in <strong>{st.session_state.user_profile.get('location', 'Dubai')}</strong></p>
            <div class="pattern-bar"></div>
            
            <div style="margin: 1.5rem 0;">
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Iftar Preparation:</span>
                    <span style="color: #8B5CF6; font-weight: bold;">6:00 PM - 7:30 PM</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Taraweeh Prayers:</span>
                    <span style="color: #8B5CF6; font-weight: bold;">8:30 PM - 10:00 PM</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Family Gatherings:</span>
                    <span style="color: #8B5CF6; font-weight: bold;">10:00 PM - 1:00 AM</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Suhoor Preparation:</span>
                    <span style="color: #8B5CF6; font-weight: bold;">3:30 AM - 4:30 AM</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
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
    
    st.markdown(f"""
    <div class="uae-card ramadan">
        <h3>💰 Your Ramadan Savings Potential</h3>
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; font-weight: bold; color: #8B5CF6; margin-bottom: 0.5rem;">
                AED {ramadan_savings}/month
            </div>
            <div style="opacity: 0.8;">
                During Ramadan months for your {st.session_state.user_profile['family_size']}-person family
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem;">
            <div style="text-align: center;">
                <div style="font-size: 1.2rem; font-weight: bold; color: #22C55E;">{35 + st.session_state.user_profile['ac_units'] * 3}%</div>
                <div style="opacity: 0.8;">AC Optimization</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.2rem; font-weight: bold; color: #22C55E;">{25 + st.session_state.user_profile['family_size'] * 2}%</div>
                <div style="opacity: 0.8;">Lighting Efficiency</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.uai_settings['ramadan_mode']:
        st.success("🌙 Ramadan Intelligence: ACTIVE - Your home will automatically adapt to Ramadan patterns")
    else:
        st.warning("🌙 Ramadan Intelligence: INACTIVE - Enable in settings for optimal Ramadan savings")

with tab2:
    st.markdown("### ☀️ Summer Survival AI")
    
    col1, col2 = st.columns(2)
    
    with col1:
        summer_savings = st.session_state.user_profile['ac_units'] * 55 + (100 if st.session_state.user_profile['home_type'] == 'Villa' else 0)
        
        st.markdown(f"""
        <div class="uae-card summer slide-in-right">
            <h3>🔥 UAE Summer Optimization</h3>
            <p>Personalized for your <strong>{st.session_state.user_profile['home_type']}</strong> with <strong>{st.session_state.user_profile['ac_units']} AC units</strong></p>
            
            <div style="margin: 1.5rem 0;">
                <div class="cultural-badge">Desert Heat Adaptation</div>
                <div class="cultural-badge">Peak Temperature Management</div>
                <div class="cultural-badge">AC Compressor Protection</div>
                <div class="cultural-badge">Sandstorm Preparation</div>
            </div>
            
            <div style="background: rgba(245, 158, 11, 0.2); padding: 1rem; border-radius: 10px; margin-top: 1rem;">
                <div style="color: #F59E0B; font-weight: bold; text-align: center;">
                    🎯 Summer Savings Target: AED {summer_savings}/month
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
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
        st.markdown(f"""
        <div style="
            background: rgba(245, 158, 11, 0.1);
            border-left: 4px solid #F59E0B;
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">
            <div style="font-weight: bold;">{feature}</div>
            <div style="color: #F59E0B; font-weight: bold;">{savings}</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### 👨‍👩‍👧‍👦 Family Dynamics AI")
    
    family_scheduling = st.session_state.user_profile['family_size'] * 18
    room_optimization = len(st.session_state.user_profile['rooms']) * 15
    pattern_learning = st.session_state.user_profile['family_size'] * 12
    
    st.markdown(f"""
    <div class="uae-card family slide-in-right">
        <h3>🏡 Understanding Your Family of {st.session_state.user_profile['family_size']}</h3>
        <p>AI learning your unique family patterns in <strong>{st.session_state.user_profile.get('location', 'Dubai')}</strong></p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 1.5rem;">
            <div>
                <h4>👥 Family Profile</h4>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Family Size:</span>
                    <span style="font-weight: bold;">{st.session_state.user_profile['family_size']} people</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Home Type:</span>
                    <span style="font-weight: bold;">{st.session_state.user_profile['home_type']}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>AC Units:</span>
                    <span style="font-weight: bold;">{st.session_state.user_profile['ac_units']} units</span>
                </div>
            </div>
            
            <div>
                <h4>💡 Family-Specific Savings</h4>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Family Scheduling:</span>
                    <span style="color: #22C55E; font-weight: bold;">AED {family_scheduling}/mo</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Room Optimization:</span>
                    <span style="color: #22C55E; font-weight: bold;">AED {room_optimization}/mo</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                    <span>Pattern Learning:</span>
                    <span style="color: #22C55E; font-weight: bold;">AED {pattern_learning}/mo</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
        st.markdown("""
        <div class="uae-card desert slide-in-right">
            <h3>🌵 Desert-Optimized Systems</h3>
            <p>Specialized for UAE's unique climate conditions</p>
            
            <div style="margin: 1.5rem 0;">
                <div style="background: rgba(239, 68, 68, 0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
                    <div style="color: #EF4444; font-weight: bold;">🌡️ Extreme Heat Management</div>
                    <div style="opacity: 0.8; font-size: 0.9rem;">AC optimization for 45°C+ temperatures</div>
                </div>
                
                <div style="background: rgba(139, 92, 246, 0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
                    <div style="color: #8B5CF6; font-weight: bold;">💧 Humidity Control</div>
                    <div style="opacity: 0.8; font-size: 0.9rem;">Coastal area adaptation</div>
                </div>
                
                <div style="background: rgba(245, 158, 11, 0.2); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
                    <div style="color: #F59E0B; font-weight: bold;">🏜️ Sand & Dust Protection</div>
                    <div style="opacity: 0.8; font-size: 0.9rem;">Equipment maintenance optimization</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
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
        ("AC Desert Mode", f"Optimized for {st.session_state.user_profile['ac_units']} units in extreme heat"),
        ("Humidity Priority", "Remove moisture before cooling - More efficient"),
        ("Sandstorm Protocol", "Automatic system protection during storms"),
        ("Rapid Response", "Quick adaptation to temperature changes")
    ]
    
    for optimization, description in desert_optimizations:
        st.markdown(f"""
        <div style="
            background: rgba(239, 68, 68, 0.1);
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
            border-left: 4px solid #EF4444;
        ">
            <div style="font-weight: bold; color: #EF4444; margin-bottom: 0.5rem;">{optimization}</div>
            <div style="opacity: 0.9;">{description}</div>
        </div>
        """, unsafe_allow_html=True)

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
