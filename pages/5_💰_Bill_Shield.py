import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Bill Shield", layout="wide")

# Initialize session state for bill data
if 'bill_data' not in st.session_state:
    st.session_state.bill_data = {
        'current_bill': 850,
        'previous_bill': 920,
        'savings_achieved': 70,
        'budget': 800,
        'peak_hours_usage': 45,
        'target_savings': 150
    }

if 'usage_patterns' not in st.session_state:
    st.session_state.usage_patterns = {
        'ac_usage': 65,
        'lighting': 15,
        'appliances': 12,
        'pool_pump': 8
    }

# Enhanced CSS for Bill Shield
st.markdown("""
<style>
    .shield-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .shield-card:hover {
        transform: translateY(-3px);
        background: rgba(255, 255, 255, 0.15);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    
    .emergency-shield {
        background: linear-gradient(45deg, #EF4444, #DC2626);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
    }
    
    .success-shield {
        background: linear-gradient(45deg, #22C55E, #16A34A);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
    }
    
    .warning-shield {
        background: linear-gradient(45deg, #F59E0B, #D97706);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-alert {
        animation: pulse 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ BILL SHIELD")
st.markdown("### AI-Powered Bill Protection & Savings Optimizer")

# QUICK OVERVIEW CARDS
col1, col2, col3, col4 = st.columns(4)

with col1:
    bill_change = st.session_state.bill_data['current_bill'] - st.session_state.bill_data['previous_bill']
    trend_icon = "📉" if bill_change < 0 else "📈"
    trend_color = "inverse" if bill_change < 0 else "normal"
    st.metric(
        "Current Bill", 
        f"AED {st.session_state.bill_data['current_bill']}",
        f"{trend_icon} AED {abs(bill_change)}",
        delta_color=trend_color
    )

with col2:
    savings_percent = (st.session_state.bill_data['savings_achieved'] / st.session_state.bill_data['previous_bill']) * 100
    st.metric(
        "Savings Achieved", 
        f"AED {st.session_state.bill_data['savings_achieved']}",
        f"📊 {savings_percent:.1f}%"
    )

with col3:
    budget_status = st.session_state.bill_data['current_bill'] - st.session_state.bill_data['budget']
    status_icon = "✅" if budget_status <= 0 else "⚠️"
    st.metric(
        "Budget Status", 
        f"AED {st.session_state.bill_data['budget']}",
        f"{status_icon} AED {abs(budget_status)} {'under' if budget_status <= 0 else 'over'}"
    )

with col4:
    days_until_due = 5  # Example
    st.metric(
        "Next Bill Due", 
        f"{days_until_due} days",
        "📅 15th Dec 2024"
    )

# MAIN CONTENT AREA
tab1, tab2, tab3, tab4 = st.tabs(["📊 Bill Analysis", "🔍 Usage Insights", "🎯 Savings Opportunities", "🛡️ Protection Plan"])

with tab1:
    st.markdown("#### 💡 Your Bill Breakdown & Trends")
    
    # Bill comparison chart
    months = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    bill_amounts = [950, 920, 890, 920, st.session_state.bill_data['current_bill']]
    budget_line = [st.session_state.bill_data['budget']] * len(months)
    
    fig_bill_trend = go.Figure()
    
    fig_bill_trend.add_trace(go.Scatter(
        x=months, y=bill_amounts,
        mode='lines+markers',
        name='Actual Bill',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=8)
    ))
    
    fig_bill_trend.add_trace(go.Scatter(
        x=months, y=budget_line,
        mode='lines',
        name='Your Budget',
        line=dict(color='#4ECDC4', width=3, dash='dash')
    ))
    
    fig_bill_trend.update_layout(
        title="📈 6-Month Bill Trend vs Your Budget",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"},
        height=400
    )
    
    st.plotly_chart(fig_bill_trend, use_container_width=True)
    
    # Bill breakdown
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Usage by appliance type
        usage_data = st.session_state.usage_patterns
        fig_usage = px.pie(
            values=list(usage_data.values()),
            names=list(usage_data.keys()),
            title="🔌 Energy Usage by Appliance Type",
            color_discrete_sequence=px.colors.sequential.Viridis
        )
        fig_usage.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"},
            showlegend=True
        )
        st.plotly_chart(fig_usage, use_container_width=True)
    
    with col2:
        st.markdown("#### 💰 Cost Allocation")
        
        cost_categories = {
            'AC Cooling': st.session_state.bill_data['current_bill'] * 0.65,
            'Lighting': st.session_state.bill_data['current_bill'] * 0.15,
            'Kitchen': st.session_state.bill_data['current_bill'] * 0.12,
            'Other': st.session_state.bill_data['current_bill'] * 0.08
        }
        
        for category, cost in cost_categories.items():
            progress_value = int(cost / st.session_state.bill_data['current_bill'] * 100)
            st.write(f"**{category}**")
            st.progress(progress_value, text=f"AED {cost:.0f}")

with tab2:
    st.markdown("#### 🔍 Deep Usage Insights")
    
    # Peak hours analysis
    st.markdown("##### 🕒 Peak Hours Usage Pattern")
    
    # Generate hourly usage data
    hours = list(range(24))
    typical_usage = [20, 18, 16, 15, 14, 16, 25, 45, 60, 55, 50, 48,
                    52, 58, 62, 65, 70, 75, 80, 65, 50, 40, 30, 22]
    
    your_usage = [usage * (1 + random.uniform(-0.1, 0.1)) for usage in typical_usage]
    
    fig_hourly = go.Figure()
    
    fig_hourly.add_trace(go.Scatter(
        x=hours, y=typical_usage,
        mode='lines',
        name='Typical Home',
        line=dict(color='#666', width=2, dash='dot')
    ))
    
    fig_hourly.add_trace(go.Scatter(
        x=hours, y=your_usage,
        mode='lines+markers',
        name='Your Home',
        line=dict(color='#FFD93D', width=4),
        fill='tozeroy',
        fillcolor='rgba(255, 217, 61, 0.2)'
    ))
    
    # Highlight peak hours
    fig_hourly.add_vrect(
        x0=14, x1=20,
        fillcolor="red", opacity=0.1,
        layer="below", line_width=0,
        annotation_text="Peak Hours", annotation_position="top left"
    )
    
    fig_hourly.update_layout(
        title="24-Hour Energy Consumption Pattern",
        xaxis_title="Hour of Day",
        yaxis_title="Energy Usage (kWh)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"}
    )
    
    st.plotly_chart(fig_hourly, use_container_width=True)
    
    # Usage alerts
    st.markdown("##### ⚠️ Usage Alerts")
    
    alert_col1, alert_col2, alert_col3 = st.columns(3)
    
    with alert_col1:
        with st.container():
            st.markdown('<div class="warning-shield">', unsafe_allow_html=True)
            st.error("**Peak Hour Usage**")
            st.write(f"{st.session_state.bill_data['peak_hours_usage']}% of your usage during premium rates")
            if st.button("Optimize Now", key="peak_opt", use_container_width=True):
                st.session_state.bill_data['peak_hours_usage'] = max(20, st.session_state.bill_data['peak_hours_usage'] - 15)
                st.success("Peak usage optimized! Reduced by 15%")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with alert_col2:
        with st.container():
            st.markdown('<div class="warning-shield">', unsafe_allow_html=True)
            st.warning("**AC Overuse**")
            st.write("65% of bill from AC - Consider temperature optimization")
            if st.button("Adjust AC", key="ac_opt", use_container_width=True):
                st.session_state.bill_data['current_bill'] = max(600, st.session_state.bill_data['current_bill'] - 45)
                st.success("AC optimized! Saved AED 45/month")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with alert_col3:
        with st.container():
            st.markdown('<div class="warning-shield">', unsafe_allow_html=True)
            st.info("**Weekend Spike**")
            st.write("45% higher usage on weekends vs weekdays")
            if st.button("Smart Schedule", key="weekend_opt", use_container_width=True):
                st.success("Weekend schedule optimized!")
            st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("#### 🎯 Personalized Savings Opportunities")
    
    # Get user profile for personalized recommendations
    user_profile = st.session_state.get('user_profile', {})
    home_type = user_profile.get('home_type', 'Apartment')
    ac_units = user_profile.get('ac_units', 2)
    family_size = user_profile.get('family_size', 4)
    
    # Savings recommendations based on user profile
    savings_opportunities = [
        {
            "title": "Peak Hour Shifting",
            "description": "Move 30% of peak hour usage to off-peak times",
            "savings": 120,
            "effort": "Low",
            "implementation": "Automated",
            "impact": "High"
        },
        {
            "title": "AC Temperature Optimization",
            "description": f"Increase default temperature by 2°C for your {ac_units} AC units",
            "savings": ac_units * 25,
            "effort": "Low", 
            "implementation": "Smart Thermostat",
            "impact": "High"
        },
        {
            "title": "Family Usage Coordination",
            "description": f"Optimize schedules for your {family_size}-person family",
            "savings": family_size * 15,
            "effort": "Medium",
            "implementation": "Family Planning",
            "impact": "Medium"
        }
    ]
    
    # Add home-type specific recommendations
    if home_type == 'Villa':
        savings_opportunities.append({
            "title": "Pool Pump Optimization",
            "description": "Reduce pool pump runtime by 3 hours daily",
            "savings": 95,
            "effort": "Medium",
            "implementation": "Timer Setup",
            "impact": "Medium"
        })
    
    # Add general recommendations
    savings_opportunities.extend([
        {
            "title": "LED Lighting Upgrade",
            "description": "Replace remaining halogen bulbs with LEDs",
            "savings": 45,
            "effort": "Medium",
            "implementation": "One-time Purchase",
            "impact": "Low"
        },
        {
            "title": "Standby Power Reduction",
            "description": "Eliminate ghost energy from idle devices",
            "savings": 35,
            "effort": "Low",
            "implementation": "Smart Plugs",
            "impact": "Low"
        }
    ])
    
    for i, opportunity in enumerate(savings_opportunities):
        with st.expander(f"💡 {opportunity['title']} - Potential: AED {opportunity['savings']}/month", expanded=i==0):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(opportunity['description'])
                st.caption(f"Implementation: {opportunity['implementation']}")
            
            with col2:
                st.metric("Monthly Savings", f"AED {opportunity['savings']}")
            
            with col3:
                effort_color = "🟢" if opportunity['effort'] == "Low" else "🟡" if opportunity['effort'] == "Medium" else "🔴"
                st.write(f"{effort_color} {opportunity['effort']} Effort")
                
                if st.button("Apply", key=f"apply_{i}", use_container_width=True):
                    # Apply savings
                    st.session_state.bill_data['current_bill'] = max(400, st.session_state.bill_data['current_bill'] - opportunity['savings'])
                    st.session_state.bill_data['savings_achieved'] += opportunity['savings']
                    st.success(f"✅ {opportunity['title']} applied! Estimated savings: AED {opportunity['savings']}/month")
                    st.rerun()
    
    # Total savings potential
    total_potential = sum(opp['savings'] for opp in savings_opportunities)
    st.markdown(f"##### 💰 Total Identified Savings Potential: **AED {total_potential}/month**")
    
    # Savings goal progress
    current_savings = st.session_state.bill_data['savings_achieved']
    target_savings = st.session_state.bill_data['target_savings']
    progress = min(100, (current_savings / target_savings) * 100)
    
    st.markdown("##### 🎯 Savings Goal Progress")
    st.progress(int(progress), text=f"AED {current_savings} of AED {target_savings} monthly target")
    
    if progress >= 100:
        st.markdown('<div class="success-shield">🎉 Congratulations! You achieved your savings target!</div>', unsafe_allow_html=True)
    elif progress >= 75:
        st.markdown('<div class="warning-shield">📈 Great progress! Almost at your target.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="emergency-shield">📊 Keep going! More savings opportunities available.</div>', unsafe_allow_html=True)

with tab4:
    st.markdown("#### 🛡️ Bill Protection Plan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🎪 Current Protection Status")
        
        protection_features = [
            {"feature": "Peak Hour Alerts", "status": "Active", "icon": "🔔", "level": "Basic"},
            {"feature": "Usage Forecasting", "status": "Active", "icon": "🔮", "level": "Basic"},
            {"feature": "Auto-Optimization", "status": "Inactive", "icon": "⚡", "level": "Pro"},
            {"feature": "Budget Protection", "status": "Active", "icon": "💰", "level": "Basic"},
            {"feature": "Emergency Shutdown", "status": "Inactive", "icon": "🛑", "level": "Pro"}
        ]
        
        for pf in protection_features:
            status_color = "🟢" if pf['status'] == "Active" else "🔴"
            level_color = "#22C55E" if pf['level'] == "Basic" else "#F59E0B"
            st.markdown(f"""
            <div class="shield-card">
                <div style="display: flex; justify-content: between; align-items: center;">
                    <div style="font-size: 1.5rem;">{pf['icon']}</div>
                    <div style="flex: 1; margin-left: 1rem;">
                        <div style="font-weight: bold;">{pf['feature']}</div>
                        <div style="color: {level_color}; font-size: 0.8rem;">{pf['level']} Plan</div>
                    </div>
                    <div style="color: {'#22C55E' if pf['status'] == 'Active' else '#EF4444'}">
                        {status_color} {pf['status']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("##### 🚀 Upgrade Your Protection")
        
        protection_plans = [
            {
                "name": "Basic Shield",
                "price": 0,
                "features": ["Peak Alerts", "Basic Analytics", "Monthly Reports"],
                "current": True,
                "color": "#22C55E"
            },
            {
                "name": "Pro Shield", 
                "price": 49,
                "features": ["Auto-Optimization", "Real-time Control", "Priority Support", "Advanced AI"],
                "current": False,
                "color": "#F59E0B"
            },
            {
                "name": "Enterprise Shield",
                "price": 99,
                "features": ["All Pro Features", "Custom Integrations", "Dedicated Manager", "API Access"],
                "current": False,
                "color": "#EF4444"
            }
        ]
        
        for plan in protection_plans:
            st.markdown(f"""
            <div class="shield-card" style="border-left: 4px solid {plan['color']};">
                <h3>{plan['name']}</h3>
                <div style="font-size: 1.5rem; font-weight: bold; color: {plan['color']};">
                    AED {plan['price']}/month
                </div>
            """, unsafe_allow_html=True)
            
            for feature in plan['features']:
                st.write(f"✅ {feature}")
            
            if plan['current']:
                st.success("**Current Plan**")
            else:
                if st.button(f"Upgrade to {plan['name']}", key=plan['name'], use_container_width=True):
                    st.success(f"🎉 {plan['name']} activated! Enhanced protection enabled.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Emergency controls
    st.markdown("---")
    st.markdown("##### 🚨 Emergency Bill Control")
    
    emergency_col1, emergency_col2, emergency_col3 = st.columns(3)
    
    with emergency_col1:
        if st.button("🔄 Enable Power Saving Mode", use_container_width=True, type="secondary"):
            st.session_state.bill_data['current_bill'] = max(400, st.session_state.bill_data['current_bill'] * 0.8)
            st.session_state.bill_data['savings_achieved'] += st.session_state.bill_data['current_bill'] * 0.2
            st.success("🔋 Power Saving Mode Activated! 20% reduction applied.")
            st.rerun()
    
    with emergency_col2:
        if st.button("⏰ Schedule AC Break", use_container_width=True, type="secondary"):
            st.info("❄️ AC will pause for 2 hours during peak times - Estimated savings: AED 35/month")
    
    with emergency_col3:
        if st.button("📱 Contact Energy Coach", use_container_width=True, type="primary"):
            st.success("👨‍💼 Energy coach will contact you within 24 hours for personalized advice!")

# BILL FORECASTING
st.markdown("---")
st.markdown("#### 🔮 Smart Bill Forecasting")

forecast_col1, forecast_col2 = st.columns([2, 1])

with forecast_col1:
    # Generate forecast data
    future_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    base_forecast = [820, 780, 720, 680, 750, 850]  # Summer increase
    optimized_forecast = [value * 0.75 for value in base_forecast]  # 25% savings
    
    fig_forecast = go.Figure()
    
    fig_forecast.add_trace(go.Scatter(
        x=future_months, y=base_forecast,
        mode='lines+markers',
        name='Without Optimization',
        line=dict(color='#FF6B6B', width=3)
    ))
    
    fig_forecast.add_trace(go.Scatter(
        x=future_months, y=optimized_forecast,
        mode='lines+markers', 
        name='With AI Optimization',
        line=dict(color='#4ECDC4', width=3)
    ))
    
    fig_forecast.update_layout(
        title="6-Month Bill Forecast with AI Optimization",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "white"},
        height=400
    )
    
    st.plotly_chart(fig_forecast, use_container_width=True)

with forecast_col2:
    st.markdown("##### 💡 Forecast Insights")
    
    total_without_opt = sum(base_forecast)
    total_with_opt = sum(optimized_forecast)
    total_savings = total_without_opt - total_with_opt
    
    st.metric("6-Month Forecast", f"AED {total_with_opt:.0f}", f"Save AED {total_savings:.0f}")
    st.metric("Average Monthly", f"AED {total_with_opt/6:.0f}", "With optimization")
    st.metric("Peak Summer", f"AED {optimized_forecast[5]}", "June forecast")
    
    st.info("💡 AI can reduce your summer peak by 25% through smart scheduling")

# QUICK ACTIONS BAR
st.markdown("---")
st.markdown("#### ⚡ Quick Actions")

action_col1, action_col2, action_col3, action_col4 = st.columns(4)

with action_col1:
    if st.button("📊 Update Bill Data", use_container_width=True):
        st.success("✅ Bill data synchronized with DEWA")

with action_col2:
    if st.button("🎯 Apply All Recommendations", use_container_width=True):
        total_savings = sum(opp['savings'] for opp in savings_opportunities)
        st.session_state.bill_data['current_bill'] = max(400, st.session_state.bill_data['current_bill'] - total_savings)
        st.session_state.bill_data['savings_achieved'] += total_savings
        st.success(f"✅ All recommendations applied! Total savings: AED {total_savings}/month")
        st.rerun()

with action_col3:
    if st.button("📧 Export Report", use_container_width=True):
        st.success("📋 Comprehensive bill report exported to PDF")

with action_col4:
    if st.button("🔄 Reset to Default", use_container_width=True):
        st.session_state.bill_data = {
            'current_bill': 850,
            'previous_bill': 920, 
            'savings_achieved': 70,
            'budget': 800,
            'peak_hours_usage': 45,
            'target_savings': 150
        }
        st.success("🔄 Bill data reset to default values")
        st.rerun()

# BILL SHIELD STATUS
st.markdown("---")
current_bill = st.session_state.bill_data['current_bill']
budget = st.session_state.bill_data['budget']

if current_bill <= budget:
    st.markdown('<div class="success-shield pulse-alert">🛡️ BILL SHIELD ACTIVE - You are within budget! 🎉</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="emergency-shield pulse-alert">🚨 BILL SHIELD ALERT - You are over budget! Take action.</div>', unsafe_allow_html=True)
