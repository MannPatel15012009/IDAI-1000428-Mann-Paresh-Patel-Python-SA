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
        color: #1e293b !important;
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
        margin-bottom: 20px;
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
        color: #064e3b !important;
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
        color: #1e293b !important;
    }
    
    .stButton button {
        width: 100%;
    }
    
    .stButton {
        margin-top: 15px;
    }
    
    .points-tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    .points-tooltip:hover::after {
        content: "Points: +10 Add med • +20 Take med • +50 Badge • +100 5-day streak • +250 10-day streak";
        position: absolute;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        background: #1e293b;
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.8rem;
        white-space: nowrap;
        z-index: 100;
    }
    
    /* Dataframe styling for light mode */
    .stDataFrame, .dataframe {
        background: white !important;
    }
    
    .dataframe th {
        background: #f8fafc !important;
        color: #1e293b !important;
        border-color: #e2e8f0 !important;
    }
    
    .dataframe td {
        background: white !important;
        color: #1e293b !important;
        border-color: #e2e8f0 !important;
    }
    
    /* Info boxes in light mode */
    .stAlert {
        background: #f8fafc !important;
        border-color: #e2e8f0 !important;
    }
    
    .element-container .stAlert [data-testid="stMarkdownContainer"] {
        color: #1e293b !important;
    }
    
    /* ========== DARK MODE FIXES ========== */
    @media (prefers-color-scheme: dark) {
        body {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
            color: white !important;
        }
        
        .main-header {
            background: linear-gradient(90deg, #94a3b8 0%, #cbd5e1 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
        }
        
        .sub-header {
            color: #cbd5e1 !important;
        }
        
        .gamified-card {
            background: #1e293b !important;
            border-color: #475569 !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
        }
        
        .gamified-card:hover {
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4) !important;
        }
        
        .medication-name {
            color: white !important;
        }
        
        .medication-time {
            color: #cbd5e1 !important;
        }
        
        .progress-container, .add-medicine-section {
            background: #1e293b !important;
            border-color: #475569 !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
        }
        
        .progress-title, .section-title {
            color: white !important;
        }
        
        .stat-box {
            background: #1e293b !important;
            border-color: #475569 !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
        }
        
        .stat-value {
            color: #94a3b8 !important;
        }
        
        .stat-label {
            color: #cbd5e1 !important;
        }
        
        /* Input fields in dark mode */
        .stTextInput input, .stSelectbox select, .stTextInput input:focus {
            background-color: #1e293b !important;
            color: white !important;
            border-color: #475569 !important;
        }
        
        /* Placeholder text */
        .stTextInput input::placeholder {
            color: #94a3b8 !important;
        }
        
        /* Radio buttons in dark mode */
        .stRadio > div {
            color: white !important;
        }
        
        /* Form labels */
        label, [data-testid="stMarkdownContainer"] {
            color: white !important;
        }
        
        /* Dataframe in dark mode */
        .stDataFrame, .dataframe {
            background: #1e293b !important;
        }
        
        .dataframe th {
            background: #334155 !important;
            color: white !important;
            border-color: #475569 !important;
        }
        
        .dataframe td {
            background: #1e293b !important;
            color: white !important;
            border-color: #475569 !important;
        }
        
        /* Tab headers in dark mode */
        .stTabs [data-baseweb="tab-list"] {
            background: #1e293b !important;
            border-color: #475569 !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            color: #cbd5e1 !important;
        }
        
        .stTabs [aria-selected="true"] {
            color: white !important;
        }
        
        /* Metrics in dark mode */
        [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
            color: white !important;
        }
        
        /* Info boxes in dark mode */
        .stAlert {
            background: #0f172a !important;
            border-color: #334155 !important;
        }
        
        .element-container .stAlert [data-testid="stMarkdownContainer"] {
            color: white !important;
        }
        
        /* Progress bar background */
        .stProgress > div > div > div {
            background-color: #334155 !important;
        }
        
        /* Table borders */
        [data-testid="stTable"] {
            border: 1px solid #475569 !important;
        }
        
        /* Selectbox dropdown */
        [data-baseweb="select"] {
            color: white !important;
            background-color: #1e293b !important;
        }
        
        /* Time format radio labels */
        .stRadio label p {
            color: white !important;
        }
        
        /* Medicine card content */
        .medicine-card-content {
            color: white !important;
        }
        
        /* Footer text */
        .footer {
            color: #cbd5e1 !important;
        }
        
        /* Health tip box */
        [data-testid="stExpander"] {
            background: #1e293b !important;
            border-color: #475569 !important;
        }
        
        /* Tooltip background */
        .points-tooltip:hover::after {
            background: #0f172a !important;
            border: 1px solid #475569 !important;
            color: white !important;
        }
        
        /* Stats box text */
        .stat-box .stat-value, .stat-box .stat-label {
            color: white !important;
        }
        
        /* Celebration animation */
        .celebration-animation {
            color: white !important;
            background: rgba(16, 185, 129, 0.2) !important;
            border-color: #10b981 !important;
        }
        
        /* Suggestion box */
        div[data-testid="stHorizontalBlock"] > div > div {
            color: white !important;
        }
        
        /* Custom containers with white background */
        div.stMarkdown > div {
            color: white !important;
        }
        
        /* All p tags in dark mode */
        p {
            color: white !important;
        }
        
        /* All h1-h6 tags in dark mode */
        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }
        
        /* Streamlit text elements */
        .stMarkdown {
            color: white !important;
        }
        
        /* Streamlit caption */
        .stCaption {
            color: #94a3b8 !important;
        }
        
        /* Badge text in dark mode */
        .badge-gamified {
            color: white !important;
        }
        
        /* Progress percentage in dark mode */
        .progress-percentage {
            color: white !important;
            -webkit-text-fill-color: white !important;
            background: linear-gradient(90deg, #94a3b8 0%, #cbd5e1 100%) !important;
            -webkit-background-clip: text !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# MOTIVATIONAL TIPS & BADGES DATA
# ------------------------------------------
MOTIVATIONAL_TIPS = [
    {"tip": "💫 Every dose is a victory! Keep building your health streak!", "color": "#8B5CF6"},
    {"tip": "🌈 Consistency is the secret ingredient to wellness!", "color": "#06B6D4"},
    {"tip": "🌟 You're not just taking medicine, you're investing in YOU!", "color": "#10B981"},
    {"tip": "🌻 Small steps today lead to giant leaps in health tomorrow!", "color": "#F59E0B"},
    {"tip": "💪 Your commitment to health is truly inspiring!", "color": "#EF4444"},
    {"tip": "🌱 Nourish your body like you'd nurture a precious garden!", "color": "#84CC16"},
    {"tip": "⭐️ Every 'I Took It' click is a step toward vitality!", "color": "#6366F1"},
    {"tip": "🌼 Self-care isn't selfish - it's essential!", "color": "#EC4899"},
]

SUGGESTIONS = [
    "💡 Set a daily reminder 5 minutes before medicine time",
    "💡 Keep medicines visible but out of reach of children",
    "💡 Drink a full glass of water with your medicine",
    "💡 Track side effects in the notes section",
    "💡 Set up a weekly pill organizer for convenience",
    "💡 Always check expiration dates monthly",
    "💡 Keep a backup supply for emergencies",
    "💡 Store medicines away from heat and humidity",
]

DAILY_HEALTH_TIPS = [
    "🌿 Staying hydrated helps your body process medications more effectively. Aim for 8 glasses of water daily!",
    "🥗 Eating a balanced meal before taking medications can help with absorption and reduce stomach upset.",
    "⏰ Taking medications at the same time each day helps build a consistent routine for better adherence.",
    "📝 Keep a medication diary to track any side effects or reactions you experience.",
    "🌡️ Store medications properly - most should be kept in a cool, dry place away from direct sunlight.",
    "💊 Never skip a dose; if you forget, take it as soon as you remember unless it's close to the next dose.",
    "🍌 Some medications work better with certain foods - check if yours should be taken with or without food.",
    "🧘 Deep breathing exercises can help if you feel anxious about taking medications regularly.",
    "📱 Set phone reminders for your medication times to ensure you never miss a dose.",
    "🏃 Regular light exercise can improve how your body responds to medications.",
    "😴 Getting enough sleep helps your body recover and process medications effectively.",
    "🚭 Avoid alcohol when taking medications as it can interfere with their effectiveness.",
    "🥛 Always take pills with a full glass of water to help them dissolve properly.",
    "📊 Review your medications with your doctor regularly to ensure they're still needed.",
    "🧴 Use a weekly pill organizer to keep track of your daily doses.",
    "🌅 Morning medications are best taken after breakfast to avoid stomach irritation.",
    "🌙 Evening medications should be taken at least 2 hours before bedtime for proper absorption.",
    "🤝 Inform all your healthcare providers about all medications you're taking to avoid interactions.",
    "📦 Keep medications in their original containers with labels intact.",
    "🧼 Wash your hands before handling medications to prevent contamination.",
]

# Additional badge types
BADGE_TYPES = {
    "early_bird": {"name": "Early Bird", "icon": "🌅", "color": "#FBBF24"},
    "night_owl": {"name": "Night Owl", "icon": "🦉", "color": "#7C3AED"},
    "perfect_week": {"name": "Perfect Week", "icon": "🏆", "color": "#10B981"},
    "consistency_king": {"name": "Consistency King", "icon": "👑", "color": "#8B5CF6"},
    "weekend_warrior": {"name": "Weekend Warrior", "icon": "⚔️", "color": "#EF4444"},
}

# ------------------------------------------
# SESSION STATE - Enhanced with Gamification
# ------------------------------------------
if "motivational_tip" not in st.session_state:
    st.session_state.motivational_tip = random.choice(MOTIVATIONAL_TIPS)

if "suggestion" not in st.session_state:
    st.session_state.suggestion = random.choice(SUGGESTIONS)

if "earned_badges" not in st.session_state:
    st.session_state.earned_badges = []

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

# NEW SESSION STATE VARIABLES FOR ADVANCED PROGRESS
if "weekly_history" not in st.session_state:
    st.session_state.weekly_history = {}
if "daily_progress" not in st.session_state:
    st.session_state.daily_progress = {}
if "progress_insights" not in st.session_state:
    st.session_state.progress_insights = []
if "current_health_tip" not in st.session_state:
    st.session_state.current_health_tip = random.choice(DAILY_HEALTH_TIPS)

# ------------------------------------------
# ADVANCED PROGRESS DASHBOARD FUNCTIONS
# ------------------------------------------
def track_daily_progress():
    """Track today's progress in session state"""
    today = datetime.date.today()
    today_str = today.isoformat()
    
    if today_str not in st.session_state.daily_progress:
        meds_today = [m for m in st.session_state.meds if m["date"] == today]
        total_today = len(meds_today)
        
        st.session_state.daily_progress[today_str] = {
            "date": today,
            "total": total_today,
            "taken": 0,
            "progress": 0.0,
            "updated_at": datetime.datetime.now()
        }
    
    meds_today = [m for m in st.session_state.meds if m["date"] == today]
    taken_today = len([m for m in meds_today if m["taken"]])
    total_today = len(meds_today)
    
    progress = (taken_today / total_today) if total_today > 0 else 0
    
    st.session_state.daily_progress[today_str].update({
        "total": total_today,
        "taken": taken_today,
        "progress": progress,
        "updated_at": datetime.datetime.now()
    })
    
    return progress

def generate_weekly_simulation():
    """Generate simulated past week data"""
    today = datetime.date.today()
    days_back = 6
    
    simulated_data = []
    
    for i in range(days_back, -1, -1):
        day_date = today - datetime.timedelta(days=i)
        day_str = day_date.isoformat()
        
        if i == 0:
            if day_str in st.session_state.daily_progress:
                data = st.session_state.daily_progress[day_str]
                simulated_data.append({
                    "date": day_date,
                    "progress": data["progress"],
                    "taken": data["taken"],
                    "total": data["total"],
                    "is_actual": True
                })
            else:
                simulated_data.append({
                    "date": day_date,
                    "progress": 0.0,
                    "taken": 0,
                    "total": 0,
                    "is_actual": False
                })
        else:
            base_score = 0.7
            if st.session_state.streak > 3:
                base_score += 0.15
            if st.session_state.points > 100:
                base_score += 0.1
            
            final_score = max(0.4, min(0.98, base_score + random.uniform(-0.1, 0.1)))
            
            weekday = day_date.weekday()
            if weekday >= 5:
                final_score = max(0.3, final_score - 0.1)
            
            simulated_data.append({
                "date": day_date,
                "progress": final_score,
                "taken": random.randint(2, 4) if final_score > 0.5 else random.randint(0, 2),
                "total": random.randint(3, 5),
                "is_actual": False
            })
    
    return simulated_data

def update_progress_insights():
    """Generate personalized insights"""
    insights = []
    
    today_progress = track_daily_progress()
    if today_progress == 1.0:
        insights.append("🎉 **Perfect day!** You've taken all medications today!")
    elif today_progress >= 0.5:
        insights.append(f"👍 **Good progress!** You're {int(today_progress*100)}% done for today.")
    else:
        insights.append("⏰ **Time for action!** Your medications are waiting.")
    
    if st.session_state.streak >= 7:
        insights.append(f"🔥 **Consistency Champion!** A {st.session_state.streak}-day streak is impressive!")
    elif st.session_state.streak >= 3:
        insights.append(f"📈 **Building momentum!** {st.session_state.streak} days in a row!")
    
    if st.session_state.points >= 200:
        insights.append(f"🏆 **Health Hero!** {st.session_state.points} points earned!")
    elif st.session_state.points >= 100:
        insights.append(f"⭐ **Great progress!** {st.session_state.points} points shows dedication.")
    
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        insights.append("🌅 **Morning reminder:** Take medications with breakfast.")
    elif 12 <= current_hour < 18:
        insights.append("☀️ **Afternoon check-in:** Don't forget midday medications!")
    
    st.session_state.progress_insights = insights[:4]
    return insights

def show_advanced_progress():
    """Show advanced progress dashboard"""
    
    today_progress = track_daily_progress()
    insights = update_progress_insights()
    weekly_data = generate_weekly_simulation()
    
    st.markdown("""
    <div style="
        background: dark blue;
        padding: 25px;
        border-radius: 20px;
        margin: 30px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
            <div style="font-weight: 700; color: #1e293b; font-size: 1.1rem;">📈 Weekly Progress Dashboard</div>
            <div style="font-size: 0.8rem; color: #64748b;">Live Tracking • Updated Just Now</div>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Daily Progress", "📈 Trends & Analytics", "💡 Personalized Insights"])
    
    with tab1:
        st.subheader("This Week at a Glance")
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        today = datetime.date.today()
        current_weekday = today.weekday()
        
        for i, day_data in enumerate(weekly_data):
            day_name = days[(current_weekday - (len(weekly_data) - 1 - i)) % 7]
            progress = day_data["progress"]
            
            col1, col2, col3, col4 = st.columns([1, 4, 2, 1])
            
            with col1:
                if i == len(weekly_data) - 1:
                    st.markdown(f"<h4 style='color: #6366f1; margin: 0;'>🎯 {day_name}</h4>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h4 style='margin: 0;'>{day_name}</h4>", unsafe_allow_html=True)
            
            with col2:
                if progress == 0:
                    bar_color = "#e2e8f0"
                elif progress >= 0.8:
                    bar_color = "#10b981"
                elif progress >= 0.6:
                    bar_color = "#f59e0b"
                else:
                    bar_color = "#ef4444"
                
                st.markdown(f"""
                <div style="background: #f1f5f9; border-radius: 10px; height: 24px; overflow: hidden; margin: 5px 0;">
                    <div style="background: {bar_color}; width: {progress*100}%; height: 100%; 
                            border-radius: 10px; display: flex; align-items: center; padding-left: 10px;">
                        <span style="color: white; font-weight: bold; font-size: 0.8rem;">
                            {int(progress*100)}%
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                if day_data["total"] > 0:
                    st.markdown(f"**{day_data['taken']}/{day_data['total']} doses**")
            
            with col4:
                if i == len(weekly_data) - 1:
                    if progress == 1.0:
                        st.success("✅")
                    elif progress > 0:
                        st.warning("⏳")
                    else:
                        st.error("❌")
                else:
                    if progress >= 0.8:
                        st.success("✅")
                    elif progress >= 0.6:
                        st.warning("⚠️")
                    elif progress > 0:
                        st.error("❌")
        
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            avg_progress = sum(d["progress"] for d in weekly_data) / len(weekly_data)
            st.metric("📊 Weekly Avg", f"{avg_progress*100:.0f}%")
        
        with col2:
            best_day = max(weekly_data, key=lambda x: x["progress"])
            best_day_name = days[best_day["date"].weekday()]
            st.metric("🏆 Best Day", f"{best_day_name} ({best_day['progress']*100:.0f}%)")
        
        with col3:
            consistency = min(100, st.session_state.streak * 12 + int(avg_progress * 40))
            st.metric("🔥 Consistency", f"{consistency}/100")
        
        with col4:
            monthly_estimate = int(avg_progress * 120)
            st.metric("📅 Monthly Est", f"{monthly_estimate}/120 doses")
    
    with tab2:
        st.subheader("Adherence Trends & Patterns")
        
        chart_data = pd.DataFrame([
            {
                "Date": d["date"],
                "Adherence %": d["progress"] * 100,
                "Type": "Actual" if d["is_actual"] else "Estimated"
            }
            for d in weekly_data
        ])
        
        st.line_chart(chart_data.set_index("Date")["Adherence %"])
        
        st.subheader("📋 Pattern Analysis")
        weekday_data = [d for d in weekly_data if d["date"].weekday() < 5]
        weekend_data = [d for d in weekly_data if d["date"].weekday() >= 5]
        
        if weekday_data and weekend_data:
            weekday_avg = sum(d["progress"] for d in weekday_data) / len(weekday_data)
            weekend_avg = sum(d["progress"] for d in weekend_data) / len(weekend_data)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Weekday Avg", f"{weekday_avg*100:.1f}%")
            with col2:
                st.metric("Weekend Avg", f"{weekend_avg*100:.1f}%")
            
            if weekend_avg < weekday_avg * 0.8:
                st.info("**Pattern detected:** Your adherence is lower on weekends.")
    
    with tab3:
        st.subheader("💡 Your Personalized Insights")
        
        for insight in st.session_state.progress_insights:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
                border-left: 4px solid #0ea5e9;
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
            ">
                {insight}
            </div>
            """, unsafe_allow_html=True)
        
        st.subheader("🎯 Recommended Actions")
        today = datetime.date.today()
        meds_today = [m for m in st.session_state.meds if m["date"] == today]
        upcoming = [m for m in meds_today if not m["taken"]]
        
        if upcoming:
            next_med = min(upcoming, key=lambda x: x["time"])
            time_str = next_med["time"].strftime("%I:%M %p")
            
            st.info(f"""
            **⏰ Next Medication Due:**
            - **Medicine:** {next_med['name']}
            - **Scheduled:** {time_str}
            - **Status:** Waiting
            """)
            
            if st.button(f"✅ Mark {next_med['name']} as Taken", type="primary", use_container_width=True):
                next_med["taken"] = True
                st.rerun()
        
        elif meds_today and all(m["taken"] for m in meds_today):
            st.success("**✅ All Caught Up!** You've taken all medications for today.")
        
        st.subheader("🏁 Weekly Goal Progress")
        goal_percentage = 90
        current_avg = sum(d["progress"] for d in weekly_data) / len(weekly_data) * 100
        
        col1, col2 = st.columns([3, 1])
        with col1:
            progress_to_goal = min(100, current_avg / goal_percentage * 100)
            st.progress(progress_to_goal / 100)
        with col2:
            st.metric("Goal", f"{current_avg:.0f}/{goal_percentage}%")
        
        if current_avg >= goal_percentage:
            st.success(f"🎉 You've achieved your weekly goal of {goal_percentage}%!")
    
    st.markdown("</div>", unsafe_allow_html=True)

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
        <div class="stat-value points-tooltip">{st.session_state.points}</div>
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
# MOTIVATIONAL BANNER
# ------------------------------------------
st.markdown(f"""
<div style="
        background: linear-gradient(135deg, #E0F2FE 0%, #F0F9FF 100%);
    border-left: 5px solid {st.session_state.motivational_tip['color']};
    padding: 20px;
    border-radius: 16px;
    margin: 20px 0;
    text-align: center;
    font-size: 1.1rem;
    font-weight: 500;
    color: #1e293b;
">
    ✨ {st.session_state.motivational_tip['tip']}
</div>
""", unsafe_allow_html=True)

# ------------------------------------------
# SUGGESTION & BADGE CAROUSEL
# ------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #E0F2FE 0%, #F0F9FF 100%);
        padding: 18px;
        border-radius: 16px;
        border: 2px solid #BAE6FD;
        margin-bottom: 20px;
    ">
        <div style="display: flex; align-items: center; gap: 12px; color: #0369A1;">
            <span style="font-size: 1.5rem;">💡</span>
            <div>
                <div style="font-weight: 600; font-size: 0.9rem; margin-bottom: 5px;">Smart Suggestion</div>
                <div style="font-size: 0.95rem;">{st.session_state.suggestion}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🔄 New Tip", use_container_width=True, key="new_tip_btn"):
        st.session_state.motivational_tip = random.choice(MOTIVATIONAL_TIPS)
        st.session_state.suggestion = random.choice(SUGGESTIONS)
        st.rerun()

# ------------------------------------------
# ADD MEDICINE SECTION
# ------------------------------------------
st.markdown('<div class="add-medicine-section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">➕ Add New Medication</div>', unsafe_allow_html=True)

# Use a form to capture Enter key
# Get time format from session state if it exists
if "time_format" not in st.session_state:
    st.session_state.time_format = "12-hour"

c1, c2, c3 = st.columns([3, 2, 2])

with c1:
    name = st.text_input("Medicine Name", placeholder="e.g., Vitamin D, Metformin...", key="med_name")

with c2:
    # Time format selection that updates immediately
    new_format = st.radio(
        "Select Time Format",
        ["12-hour", "24-hour"],
        horizontal=True,
        index=0 if st.session_state.time_format == "12-hour" else 1,
        key="time_format_radio"
    )
    
    # Update session state if format changed
    if new_format != st.session_state.time_format:
        st.session_state.time_format = new_format
        st.rerun()

with c3:
    if st.session_state.time_format == "12-hour":
        # 12-hour format with better layout
        st.markdown("<div style='font-size: 0.9rem; color: #64748b; margin-bottom: 5px;'>Set Time (12-hour)</div>", unsafe_allow_html=True)
        
        time_col1, time_col2, time_col3 = st.columns(3)
        
        with time_col1:
            hour = st.selectbox("Hour", list(range(1, 13)), index=8, key="hour_12", label_visibility="collapsed")
        
        with time_col2:
            minute_input = st.text_input("Minute", value="00", max_chars=2, key="minute_12", label_visibility="collapsed")
        
        with time_col3:
            am_pm = st.selectbox("AM/PM", ["AM", "PM"], index=0, key="am_pm", label_visibility="collapsed")
        
        # Add labels below for clarity
        st.markdown("""
        <div style='display: flex; justify-content: space-between; font-size: 0.7rem; color: #94a3b8; margin-top: -10px;'>
            <div>Hour</div>
            <div>Minute</div>
            <div>AM/PM</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Validate and convert minute
        try:
            minute_int = int(minute_input) if minute_input.isdigit() else 0
            if minute_int < 0 or minute_int > 59:
                minute_int = 0
        except:
            minute_int = 0
        
        # Convert 12-hour to 24-hour format
        hour_24 = hour
        if am_pm == "AM":
            if hour == 12:
                hour_24 = 0  # 12 AM = 00:00
            else:
                hour_24 = hour  # 1-11 AM = same hour
        else:  # PM
            if hour == 12:
                hour_24 = 12  # 12 PM = 12:00
            else:
                hour_24 = hour + 12  # 1-11 PM = hour + 12
        
        time = datetime.time(hour_24, minute_int)
        
    else:  # 24-hour format
        st.markdown("<div style='font-size: 0.9rem; color: #64748b; margin-bottom: 5px;'>Set Time (24-hour)</div>", unsafe_allow_html=True)
        
        time_col1, time_col2 = st.columns(2)
        
        with time_col1:
            hour_24 = st.selectbox("Hour", list(range(0, 24)), index=9, key="hour_24", label_visibility="collapsed")
        
        with time_col2:
            minute_input = st.text_input("Minute", value="00", max_chars=2, key="minute_24", label_visibility="collapsed")
        
        # Add labels below for clarity
        st.markdown("""
        <div style='display: flex; justify-content: space-around; font-size: 0.7rem; color: #94a3b8; margin-top: -10px;'>
            <div>Hour (0-23)</div>
            <div>Minute (0-59)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Validate minute
        try:
            minute_int = int(minute_input) if minute_input.isdigit() else 0
            if minute_int < 0 or minute_int > 59:
                minute_int = 0
        except:
            minute_int = 0
        
        time = datetime.time(hour_24, minute_int)

# Submit buttons in a new row
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
c4, c5 = st.columns(2)

# Create separate forms for the buttons to work properly
with c4:
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

with c5:
    if st.button("🎲 Quick Add", use_container_width=True, type="secondary"):
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
                    
                    # Create the card HTML
                    card_html = f'''
                    <div class="gamified-card">
                        <div class="medicine-card-content">
                    '''
                    
                    # Check if this medicine has an achievement
                    has_achievement = False
                    if med["taken"] and random.random() > 0.7:  # Random chance for demo
                        has_achievement = True
                        card_html += '<div class="achievement-badge">🏅</div>'
                    
                    # Medicine name
                    card_html += f'<div class="medication-name">{icon} {med["name"]}</div>'
                    
                    # Medicine time
                    card_html += f'''
                    <div class="medication-time">
                        <span>🕐</span> {med["time"].strftime("%I:%M %p")}
                    </div>
                    '''
                    
                    # Status badge
                    card_html += f'<span class="badge-gamified {badge}">{status}</span>'
                    
                    card_html += '''
                        </div>
                    </div>
                    '''
                    
                    # Render the card
                    st.markdown(card_html, unsafe_allow_html=True)
                    
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
                            
                            # Random chance to earn a badge (30% chance)
                            if random.random() > 0.7 and len(st.session_state.earned_badges) < len(BADGE_TYPES):
                                available_badges = [b for b in BADGE_TYPES.keys() if b not in st.session_state.earned_badges]
                                if available_badges:
                                    new_badge = random.choice(available_badges)
                                    st.session_state.earned_badges.append(new_badge)
                                    badge_info = BADGE_TYPES[new_badge]
                                    st.session_state.celebration = f"🎖️ New Badge Earned: {badge_info['name']} {badge_info['icon']}! +50 points"
                                    st.session_state.points += 50
                            
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
    else:
        st.markdown("""
        <div style="text-align: center; padding: 50px; background: black; border-radius: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <h3 style="color: #FFFFFF;">No medications scheduled for today</h3>
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

# ------------------------------------------
# HEALTH TIPS SIDEBAR
# ------------------------------------------
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

with st.container():
    # Header with title and refresh button
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown("#### 🌿 Daily Health Tip")
    
    with col2:
        # Refresh button
        if st.button("🔄 New", key="tip_refresh_header", use_container_width=True):
            st.session_state.current_health_tip = random.choice(DAILY_HEALTH_TIPS)
            st.rerun()
    
    # Tip content in a styled box
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #FEF3C7 0%, #FFFBEB 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        border: 2px solid #FBBF24;
        color: #78350F;
        font-size: 0.95rem;
        line-height: 1.5;
    ">
        {st.session_state.current_health_tip}
    </div>
    """, unsafe_allow_html=True)
    
    # Tip counter (optional)
    try:
        tip_index = DAILY_HEALTH_TIPS.index(st.session_state.current_health_tip) + 1
        st.caption(f"Tip {tip_index} of {len(DAILY_HEALTH_TIPS)} • Click 'New' for another tip")
    except ValueError:
        # If the current tip isn't in the list (shouldn't happen normally)
        st.caption("Daily health tip • Click 'New' for another")

# Add a proper refresh button below using Streamlit
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔄 New Health Tip", use_container_width=True, key="refresh_health_tip"):
        st.session_state.current_health_tip = random.choice(DAILY_HEALTH_TIPS)
        st.rerun()

# ------------------------------------------
# BADGE COLLECTION DISPLAY
# ------------------------------------------
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
st.markdown('<div class="section-title">🎖️ Your Badge Collection</div>', unsafe_allow_html=True)

# Display badges based on earned badges in session state
badge_cols = st.columns(5)
badge_keys = list(BADGE_TYPES.keys())

for idx in range(5):
    with badge_cols[idx]:
        if idx < len(badge_keys):
            badge_key = badge_keys[idx]
            badge_info = BADGE_TYPES[badge_key]
            is_earned = badge_key in st.session_state.earned_badges
            
            if is_earned:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {badge_info['color']}20 0%, {badge_info['color']}10 100%);
                    border: 2px solid {badge_info['color']};
                    padding: 20px;
                    border-radius: 20px;
                    text-align: center;
                    height: 140px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    box-shadow: 0 6px 12px rgba(0,0,0,0.05);
                ">
                    <div style="font-size: 2.5rem; margin-bottom: 10px;">{badge_info['icon']}</div>
                    <div style="font-weight: 700; color: #1e293b; font-size: 0.9rem;">{badge_info['name']}</div>
                    <div style="font-size: 0.7rem; color: #64748b; margin-top: 5px;">Earned Today!</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="
                    background: #F8FAFC;
                    border: 2px dashed #CBD5E1;
                    padding: 20px;
                    border-radius: 20px;
                    text-align: center;
                    height: 140px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    opacity: 0.6;
                ">
                    <div style="font-size: 2.5rem; margin-bottom: 10px; opacity: 0.4;">{badge_info['icon']}</div>
                    <div style="font-weight: 700; color: #94A3B8; font-size: 0.9rem;">{badge_info['name']}</div>
                    <div style="font-size: 0.7rem; color: #CBD5E1; margin-top: 5px;">Locked 🔒</div>
                </div>
                """, unsafe_allow_html=True)

# Add badge refresh button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎲 Randomize Badge Demo", use_container_width=True):
        # Randomly toggle some badges for demo
        for badge_key in BADGE_TYPES.keys():
            if random.random() > 0.5:
                if badge_key not in st.session_state.earned_badges:
                    st.session_state.earned_badges.append(badge_key)
            else:
                if badge_key in st.session_state.earned_badges:
                    st.session_state.earned_badges.remove(badge_key)
        st.rerun()

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
            st.session_state.earned_badges = []
            st.session_state.daily_progress = {}
            st.session_state.progress_insights = []
            st.rerun()
else:
    st.info("No report available yet. Start taking your medicines to generate a health report!")

# ------------------------------------------
# ADVANCED WEEKLY PROGRESS DASHBOARD
# ------------------------------------------
show_advanced_progress()

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
