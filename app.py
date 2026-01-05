import streamlit as st
import datetime
import pandas as pd
import random

# ------------------------------------------
# PAGE CONFIG
# ------------------------------------------
st.set_page_config(
    page_title="MedTimer Pro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------
# CUSTOM STYLES - Enhanced & Gamified
# ------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Quicksand:wght@400;500;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
        background-attachment: fixed;
    }
    
    .main-header {
        font-family: 'Quicksand', sans-serif;
        font-size: 3.5rem !important;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem !important;
    }
    
    .sub-header {
        text-align: center;
        color: #6366f1;
        font-weight: 500;
        margin-top: 0 !important;
    }
    
    .gamified-card {
        background: white;
        padding: 25px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.1);
        border: 2px solid rgba(99, 102, 241, 0.1);
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .gamified-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.2);
    }
    
    .gamified-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 6px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .medication-name {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 10px;
    }
    
    .medication-time {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }
    
    .badge-gamified {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
    }
    
    .taken-badge {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
    }
    
    .missed-badge {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
    }
    
    .upcoming-badge {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
    }
    
    .progress-container {
        background: white;
        padding: 30px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.1);
        text-align: center;
        position: relative;
        overflow: hidden;
        border: 2px solid rgba(99, 102, 241, 0.1);
    }
    
    .progress-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 20px;
    }
    
    .progress-percentage {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
    }
    
    .streak-counter {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: white;
        padding: 15px;
        border-radius: 16px;
        margin: 15px 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        box-shadow: 0 6px 12px rgba(251, 191, 36, 0.3);
    }
    
    .points-display {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        color: white;
        padding: 15px;
        border-radius: 16px;
        margin: 15px 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        box-shadow: 0 6px 12px rgba(139, 92, 246, 0.3);
    }
    
    .celebration-animation {
        animation: celebrate 0.8s ease infinite alternate;
        text-align: center;
        padding: 15px;
        border-radius: 16px;
        background: rgba(16, 185, 129, 0.1);
        margin: 20px 0;
        border: 2px dashed #10b981;
    }
    
    @keyframes celebrate {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }
    
    .take-button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: 50px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 15px;
        font-size: 1rem;
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.3);
    }
    
    .take-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
    }
    
    .add-medicine-section {
        background: white;
        padding: 25px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.1);
        margin-bottom: 30px;
        border: 2px solid rgba(99, 102, 241, 0.1);
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin: 20px 0;
    }
    
    .stat-box {
        background: white;
        padding: 15px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: 800;
        color: #6366f1;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #64748b;
    }
    
    .download-button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 1rem;
        box-shadow: 0 6px 12px rgba(16, 185, 129, 0.3);
        width: 100%;
    }
    
    .download-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(16, 185, 129, 0.4);
    }
    
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 40px;
        padding: 20px;
        font-size: 0.9rem;
    }
    
    .medal-icon {
        font-size: 1.8rem;
        margin-right: 8px;
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .achievement-badge {
        position: absolute;
        top: 15px;
        right: 15px;
        background: #fbbf24;
        color: #78350f;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(251, 191, 36, 0.4);
    }
    
    .medicine-card-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# SESSION STATE - Enhanced with Gamification
# ------------------------------------------
if "meds" not in st.session_state:
    st.session_state.meds = []

if "history" not in st.session_state:
    st.session_state.history = []

if "celebration" not in st.session_state:
    st.session_state.celebration = ""

if "points" not in st.session_state:
    st.session_state.points = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "last_taken_date" not in st.session_state:
    st.session_state.last_taken_date = None

if "achievements" not in st.session_state:
    st.session_state.achievements = {
        "first_med": False,
        "perfect_week": False,
        "streak_5": False,
        "streak_10": False,
        "all_taken": False
    }

# ------------------------------------------
# HEADER WITH ANIMATION
# ------------------------------------------
st.markdown('<h1 class="main-header">💊 MedTimer Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Level up your health with gamified medication tracking 🎮</p>', unsafe_allow_html=True)

# ------------------------------------------
# QUICK STATS BAR
# ------------------------------------------
st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-value">🏆</div>
        <div class="stat-value">{st.session_state.points}</div>
        <div class="stat-label">Health Points</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-value">🔥</div>
        <div class="stat-value">{st.session_state.streak}</div>
        <div class="stat-label">Day Streak</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    today = datetime.date.today()
    meds_today = [m for m in st.session_state.meds if m["date"] == today]
    taken_today = len([m for m in meds_today if m["taken"]])
    total_today = len(meds_today)
    
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-value">💊</div>
        <div class="stat-value">{taken_today}/{total_today}</div>
        <div class="stat-label">Today's Meds</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------
# ADD MEDICINE SECTION
# ------------------------------------------
st.markdown('<div class="add-medicine-section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">➕ Add New Medication</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns([3, 2, 1.5, 1.5])

with c1:
    name = st.text_input("Medicine Name", placeholder="e.g., Vitamin D, Metformin...")

with c2:
    time = st.time_input("Scheduled Time", value=datetime.time(9, 0))

with c3:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Add Medicine", use_container_width=True, type="primary"):
        if name:
            st.session_state.meds.append({
                "name": name,
                "time": time,
                "taken": False,
                "date": datetime.date.today(),
                "added": datetime.datetime.now()
            })
            
            # Award points for adding a medicine
            st.session_state.points += 10
            
            # Check for first medicine achievement
            if not st.session_state.achievements["first_med"]:
                st.session_state.achievements["first_med"] = True
                st.session_state.points += 50
                st.session_state.celebration = "🎉 Achievement Unlocked: First Medicine Added! +50 points"
            
            st.success(f"✅ {name} added! +10 points")
            st.rerun()

with c4:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎲 Quick Add", use_container_width=True):
        quick_meds = ["Vitamin C", "Iron Supplement", "Multivitamin", "Omega-3", "Calcium"]
        quick_name = random.choice(quick_meds)
        quick_time = datetime.time(random.randint(7, 20), 0)
        
        st.session_state.meds.append({
            "name": quick_name,
            "time": quick_time,
            "taken": False,
            "date": datetime.date.today(),
            "added": datetime.datetime.now()
        })
        st.session_state.points += 5
        st.success(f"⚡ Quick-added {quick_name} for {quick_time.strftime('%I:%M %p')}! +5 points")
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------
# MAIN DASHBOARD
# ------------------------------------------
left, right = st.columns([3, 1])

# ------------------------------------------
# TODAY'S MEDICATIONS - GAMIFIED CARDS
# ------------------------------------------
with left:
    st.markdown('<div class="section-title">📋 Today\'s Medications</div>', unsafe_allow_html=True)
    
    today = datetime.date.today()
    now = datetime.datetime.now().time()
    meds_today = [m for m in st.session_state.meds if m["date"] == today]
    
    if meds_today:
        # Sort medicines by time
        meds_today.sort(key=lambda x: x["time"])
        
        # Display in rows of 2 for better spacing
        rows = [meds_today[i:i+2] for i in range(0, len(meds_today), 2)]
        
        for row in rows:
            cols = st.columns(len(row))
            for idx, med in enumerate(row):
                with cols[idx]:
                    # Determine status and badge
                    if med["taken"]:
                        status, badge, icon = "Taken", "taken-badge", "✅"
                        badge_color = "success"
                    elif now > med["time"]:
                        status, badge, icon = "Missed", "missed-badge", "⏰"
                        badge_color = "error"
                    else:
                        status, badge, icon = "Upcoming", "upcoming-badge", "🕐"
                        badge_color = "warning"
                    
                    # Create the card using container
                    with st.container():
                        st.markdown(f'<div class="gamified-card">', unsafe_allow_html=True)
                        
                        # Check if this medicine has an achievement
                        has_achievement = False
                        if med["taken"] and random.random() > 0.7:  # Random chance for demo
                            has_achievement = True
                            st.markdown('<div class="achievement-badge">🏅</div>', unsafe_allow_html=True)
                        
                        # Medicine name
                        st.markdown(f'<div class="medication-name">{icon} {med["name"]}</div>', unsafe_allow_html=True)
                        
                        # Medicine time
                        st.markdown(f'''
                        <div class="medication-time">
                            <span>🕐</span> {med["time"].strftime("%I:%M %p")}
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        # Status badge - using st.markdown to render HTML
                        st.markdown(f'<span class="badge-gamified {badge}">{status}</span>', unsafe_allow_html=True)
                        
                        # Add "I Took It" button if not taken yet
                        if not med["taken"]:
                            if st.button("💊 I Took It!", key=f"take_{id(med)}", use_container_width=True):
                                med["taken"] = True
                                st.session_state.history.append({
                                    "Medicine": med["name"],
                                    "Date": today,
                                    "Time": med["time"].strftime("%I:%M %p"),
                                    "Status": "Taken"
                                })
                                
                                # Award points for taking medicine
                                points_earned = 20
                                st.session_state.points += points_earned
                                
                                # Update streak
                                today_date = datetime.date.today()
                                if st.session_state.last_taken_date != today_date:
                                    if st.session_state.last_taken_date and (today_date - st.session_state.last_taken_date).days == 1:
                                        st.session_state.streak += 1
                                    elif not st.session_state.last_taken_date or (today_date - st.session_state.last_taken_date).days > 1:
                                        st.session_state.streak = 1
                                    st.session_state.last_taken_date = today_date
                                
                                # Check streak achievements
                                if st.session_state.streak >= 5 and not st.session_state.achievements["streak_5"]:
                                    st.session_state.achievements["streak_5"] = True
                                    st.session_state.points += 100
                                    st.session_state.celebration = f"🔥 Amazing! {st.session_state.streak}-day streak! +100 points"
                                elif st.session_state.streak >= 10 and not st.session_state.achievements["streak_10"]:
                                    st.session_state.achievements["streak_10"] = True
                                    st.session_state.points += 250
                                    st.session_state.celebration = f"🏆 Legendary! {st.session_state.streak}-day streak! +250 points"
                                else:
                                    celebration_messages = [
                                        "🎉 Great job! Your future self thanks you!",
                                        "⭐ Excellent! Consistency is key!",
                                        "💪 Well done! You're taking control of your health!",
                                        "✨ Bravo! Every dose brings you closer to wellness!",
                                        "🌈 Wonderful! You're building healthy habits!"
                                    ]
                                    st.session_state.celebration = f"{random.choice(celebration_messages)} +{points_earned} points"
                                
                                st.rerun()
                        
                        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 50px; background: white; border-radius: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <h3 style="color: #64748b;">No medications scheduled for today</h3>
            <p>Add your first medicine above to start tracking! 🚀</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------
# PROGRESS & GAMIFICATION PANEL
# ------------------------------------------
with right:
    st.markdown('<div class="progress-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="progress-title">🎯 Your Progress</div>', unsafe_allow_html=True)
    
    # Calculate progress
    total = len(meds_today)
    taken_count = len([m for m in meds_today if m["taken"]])
    score = int((taken_count / total) * 100) if total else 0
    
    # Progress bar with color based on score
    if score == 100:
        progress_color = "#10b981"
        emoji = "🏆"
    elif score >= 80:
        progress_color = "#3b82f6"
        emoji = "⭐"
    elif score >= 50:
        progress_color = "#f59e0b"
        emoji = "🙂"
    else:
        progress_color = "#ef4444"
        emoji = "💪"
    
    # Display progress
    st.markdown(f'<div class="progress-percentage">{emoji} {score}%</div>', unsafe_allow_html=True)
    
    # Custom progress bar
    st.markdown(f"""
    <div style="
        width: 100%;
        background: #e2e8f0;
        border-radius: 50px;
        height: 24px;
        margin: 20px 0;
        overflow: hidden;
    ">
        <div style="
            width: {score}%;
            background: {progress_color};
            height: 100%;
            border-radius: 50px;
            transition: width 0.5s ease;
        "></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Streak counter
    st.markdown(f"""
    <div class="streak-counter">
        <span>🔥</span>
        <span style="font-weight: 700; font-size: 1.3rem;">{st.session_state.streak} Day Streak</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Points display
    st.markdown(f"""
    <div class="points-display">
        <span>🏅</span>
        <span style="font-weight: 700; font-size: 1.3rem;">{st.session_state.points} Points</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Level indicator (simplified)
    level = st.session_state.points // 100 + 1
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        color: white;
        padding: 10px;
        border-radius: 16px;
        margin: 15px 0;
        text-align: center;
        font-weight: 600;
    ">
        Level {level} Health Hero
    </div>
    """, unsafe_allow_html=True)
    
    # Celebration message
    if st.session_state.celebration:
        st.markdown(f'<div class="celebration-animation">{st.session_state.celebration}</div>', unsafe_allow_html=True)
    
    # Next level progress
    points_to_next = 100 - (st.session_state.points % 100)
    st.markdown(f"""
    <div style="margin-top: 20px; color: #64748b; font-size: 0.9rem;">
        ⚡ {points_to_next} points to Level {level + 1}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------
# ACHIEVEMENTS & DOWNLOAD SECTION
# ------------------------------------------
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
st.markdown('<div class="section-title">🏆 Your Achievements</div>', unsafe_allow_html=True)

# Display achievements
achievement_cols = st.columns(5)
achievements_list = [
    {"name": "First Step", "desc": "Add your first medicine", "achieved": st.session_state.achievements["first_med"], "icon": "1️⃣"},
    {"name": "5-Day Streak", "desc": "Take medicine for 5 consecutive days", "achieved": st.session_state.achievements["streak_5"], "icon": "🔥"},
    {"name": "Perfect Day", "desc": "Take all medicines for the day", "achieved": taken_count == total and total > 0, "icon": "⭐"},
    {"name": "10-Day Streak", "desc": "Take medicine for 10 consecutive days", "achieved": st.session_state.achievements["streak_10"], "icon": "🏆"},
    {"name": "Week Warrior", "desc": "7 days of perfect adherence", "achieved": st.session_state.achievements["perfect_week"], "icon": "💪"},
]

for idx, achievement in enumerate(achievements_list):
    with achievement_cols[idx]:
        if achievement["achieved"]:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
                color: #78350f;
                padding: 15px;
                border-radius: 16px;
                text-align: center;
                height: 120px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                box-shadow: 0 6px 12px rgba(251, 191, 36, 0.3);
            ">
                <div style="font-size: 2rem; margin-bottom: 10px;">{achievement['icon']}</div>
                <div style="font-weight: 700; font-size: 0.9rem;">{achievement['name']}</div>
                <div style="font-size: 0.7rem; opacity: 0.9;">{achievement['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="
                background: #f1f5f9;
                color: #94a3b8;
                padding: 15px;
                border-radius: 16px;
                text-align: center;
                height: 120px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            ">
                <div style="font-size: 2rem; margin-bottom: 10px; opacity: 0.5;">{achievement['icon']}</div>
                <div style="font-weight: 700; font-size: 0.9rem; opacity: 0.7;">{achievement['name']}</div>
                <div style="font-size: 0.7rem; opacity: 0.6;">{achievement['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

# ------------------------------------------
# DOWNLOAD REPORT
# ------------------------------------------
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 Health Report</div>', unsafe_allow_html=True)

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    
    # Display preview
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.download_button(
            label="📥 Download Report",
            data=csv,
            file_name=f"medtimer_report_{datetime.date.today()}.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary"
        )
    
    with col2:
        if st.button("🔄 Reset All Data", use_container_width=True):
            st.session_state.meds = []
            st.session_state.history = []
            st.session_state.points = 0
            st.session_state.streak = 0
            st.session_state.celebration = "Data reset successfully. Start fresh! 🌱"
            st.rerun()
else:
    st.info("No report available yet. Start taking your medicines to generate a health report!")

# ------------------------------------------
# MOTIVATIONAL FOOTER
# ------------------------------------------
st.markdown("""
<div class="footer">
    <hr style="border: none; height: 1px; background: #e2e8f0; margin: 40px 0;">
    <p style="font-size: 1.1rem; color: #6366f1; font-weight: 600;">MedTimer Pro — Your gamified health companion 🎮</p>
    <p style="margin-top: 10px;">Every dose is a step toward better health. Keep going! 💪</p>
    <p style="margin-top: 20px; font-size: 0.8rem; color: #94a3b8;">
        Track • Motivate • Thrive • Level Up Your Health Journey
    </p>
</div>
""", unsafe_allow_html=True)

