import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ETERNA • UAE Energy Revolution", 
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PREMIUM ANIMATED CSS
st.markdown("""
<style>
    /* Main background with gradient animation */
    .stApp {
        background: linear-gradient(-45deg, #0F4C81, #1a237e, #1565C0, #283593);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Pulsing ETERNA logo */
    @keyframes pulse-glow {
        0% { 
            transform: scale(1);
            text-shadow: 0 0 10px #22C55E, 0 0 20px #22C55E;
        }
        50% { 
            transform: scale(1.05);
            text-shadow: 0 0 20px #22C55E, 0 0 30px #22C55E, 0 0 40px #22C55E;
        }
        100% { 
            transform: scale(1);
            text-shadow: 0 0 10px #22C55E, 0 0 20px #22C55E;
        }
    }
    
    .pulsing-logo {
        animation: pulse-glow 2s ease-in-out infinite;
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(45deg, #FFFFFF, #22C55E, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0;
    }
    
    /* Floating animation for cards */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    
    .floating-card {
        animation: float 6s ease-in-out infinite;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .floating-card:hover {
        transform: translateY(-5px) scale(1.02);
        background: rgba(255, 255, 255, 0.15);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    /* Smooth fade-in animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 1s ease-out;
    }
    
    /* Glowing buttons */
    .glow-button {
        background: linear-gradient(45deg, #22C55E, #16A34A);
        border: none;
        border-radius: 15px;
        padding: 1rem 2rem;
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(34, 197, 94, 0.3);
    }
    
    .glow-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(34, 197, 94, 0.5);
    }
    
    /* Stats counter animation */
    @keyframes countUp {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    .stat-number {
        animation: countUp 1s ease-out;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #FFFFFF, #22C55E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #22C55E, #16A34A);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION WITH PULSING LOGO
st.markdown("""
<div class="fade-in">
    <h1 class="pulsing-logo">⚡ ETERNA</h1>
    <h2 style="text-align: center; font-size: 1.8rem; margin-top: 0; opacity: 0.9;">
        UAE Energy Intelligence Platform
    </h2>
    <p style="text-align: center; font-size: 1.2rem; opacity: 0.8;">
        Revolutionizing Home Energy with AI-Powered Orchestration
    </p>
</div>
""", unsafe_allow_html=True)

# ANIMATED PROBLEM CARDS
st.markdown("""
<div class="fade-in">
    <h2 style="text-align: center; margin: 3rem 0 2rem 0;">🎯 Solving UAE's Energy Challenges</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="floating-card fade-in">
        <h3>⚡ Peak Demand Crisis</h3>
        <p style="opacity: 0.9;">AI-powered load shifting during 3-6PM grid strain</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">35% Peak Reduction</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.2s;">
        <h3>🏠 Villa Energy Chaos</h3>
        <p style="opacity: 0.9;">Whole-home orchestration for pools, ACs, and outdoor systems</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">AED 15K+ Annual Savings</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.4s;">
        <h3>🌙 Ramadan Patterns</h3>
        <p style="opacity: 0.9;">Cultural AI adapting to 80% night usage spikes</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">AED 280/Month Savings</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.6s;">
        <h3>🧠 Behavioral Waste</h3>
        <p style="opacity: 0.9;">Real-time detection of invisible energy waste</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">45% Waste Elimination</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.1s;">
        <h3>🏢 Construction Efficiency</h3>
        <p style="opacity: 0.9;">Digital twins for desert climate optimization</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">40% Better Efficiency</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.3s;">
        <h3>💰 Subsidy Optimization</h3>
        <p style="opacity: 0.9;">Automated tiered pricing understanding</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">15% Bill Reduction</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.5s;">
        <h3>🌡️ Desert AC Intelligence</h3>
        <p style="opacity: 0.9;">Algorithms optimized for 45°C+ conditions</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">55% AC Savings</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="floating-card fade-in" style="animation-delay: 0.7s;">
        <h3>🔌 Smart Home Harmony</h3>
        <p style="opacity: 0.9;">Universal device coordination platform</p>
        <div style="background: rgba(34, 197, 94, 0.2); padding: 0.5rem; border-radius: 10px; margin-top: 1rem;">
            <span style="color: #22C55E; font-weight: bold;">30% Better Coordination</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ANIMATED STATS
st.markdown("""
<div class="fade-in">
    <h2 style="text-align: center; margin: 4rem 0 2rem 0;">📊 National Impact Metrics</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px;">
        <div class="stat-number">2.1M</div>
        <div style="opacity: 0.8;">UAE Homes</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px;">
        <div class="stat-number">AED 6.3B</div>
        <div style="opacity: 0.8;">Annual Savings</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px;">
        <div class="stat-number">1.2M</div>
        <div style="opacity: 0.8;">Tons CO₂ Reduction</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px;">
        <div class="stat-number">8/8</div>
        <div style="opacity: 0.8;">Problems Solved</div>
    </div>
    """, unsafe_allow_html=True)

# CTA SECTION
st.markdown("""
<div class="fade-in" style="text-align: center; margin: 4rem 0;">
    <h2>🚀 Ready to Transform Your Energy Experience?</h2>
    <p style="font-size: 1.2rem; opacity: 0.8; margin-bottom: 2rem;">
        Explore our revolutionary solutions in the sidebar navigation
    </p>
</div>
""", unsafe_allow_html=True)

# FOOTER WITH ANIMATION
st.markdown("---")
st.markdown("""
<div class="fade-in" style="text-align: center; padding: 2rem;">
    <h3 style="
        background: linear-gradient(45deg, #FFFFFF, #22C55E, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    ">⚡ FROM STUDENT VISION TO NATIONAL SOLUTION</h3>
    <p style="opacity: 0.7;">Create Apps Championship 2024 • UAE Energy Revolution</p>
</div>
""", unsafe_allow_html=True)

# ADD SMOOTH SCROLLING JAVASCRIPT
components.html("""
<script>
    // Smooth scrolling for anchor links
    document.addEventListener('DOMContentLoaded', function() {
        const links = document.querySelectorAll('a[href^="#"]');
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    });
    
    // Add intersection observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all fade-in elements
    document.addEventListener('DOMContentLoaded', function() {
        const fadeElements = document.querySelectorAll('.fade-in');
        fadeElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    });
</script>
""")
