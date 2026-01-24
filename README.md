# 💊 MedTimer Pro - Gamified Medication Tracker
Design and Deploy Interactive Python Applications for Social Good
Build ShopImpact Conscious Shopping Dashboard using Python | Design MedTimer Daily Medicine Companion using Python

## 📋 Project Overview
MedTimer Pro is an interactive, gamified medication tracking application designed to help users manage their daily medication schedules effectively. Built using Python and Streamlit, this application transforms routine medication management into an engaging health journey with motivational features like points systems, achievement badges, and streak counters. The project addresses the common challenge of medication non-adherence by making the tracking process visual, rewarding, and interactive. The application features a colorful, animated interface with custom CSS styling, turtle graphics animations, and real-time progress tracking to encourage consistent medication use and promote better health outcomes.

## ✨ Key Features
### 🎮 Gamification System
Health Points: Earn points for adding and taking medications

Achievement Badges: Unlock special badges for consistency

Day Streaks: Build and maintain your medication streak

Level Progression: Level up as you accumulate points

### 📊 Smart Tracking
Daily Medication Dashboard: Visual cards with status indicators

Progress Analytics: Real-time progress tracking with visualizations

Weekly Trends: Sparkline charts showing adherence patterns

Exportable Reports: Download CSV reports of medication history

### 💡 Motivation & Support
Dynamic Tips: Rotating motivational messages

Celebration Animations: Visual feedback for achievements

Health Tips: Daily wellness advice

Smart Suggestions: Practical medication management tips

### 🎨 Modern UI
Beautiful Gradient Design: Clean, card-based interface

Responsive Layout: Works on desktop and mobile

Interactive Elements: Hover effects and animations

Status Visualizations: Color-coded badges (Taken/Missed/Upcoming)

## 🔧 Integration Details
The application integrates multiple Python libraries and custom modules to create a seamless user experience:

Streamlit: Serves as the main web framework for building the interactive dashboard

Pandas: Handles data manipulation and CSV export functionality for medication history

Datetime: Manages date and time operations for scheduling and tracking

Random: Generates random tips, suggestions, and badge awards

Custom CSS/HTML: Provides enhanced styling with gradients, animations, and responsive design

Turtle Graphics: Used for visual animations and interactive elements

### Key integration points include:

Session state management for persistent user data across interactions

Dynamic UI updates without page reloads using Streamlit's rerun functionality

Gamification logic that connects user actions to points, badges, and achievements

CSV export system for data portability and record-keeping

Responsive design that adapts to different screen sizes and devices

## 🚀 Deployment Instructions
### Prerequisites:
Python 3.8 or higher installed

pip package manager

Internet connection (for initial package installation)

### Local Deployment:
Clone the repository:

bash
```
 git clone https://github.com/MannPatel15012009/IDAI-1000428-Mann-Paresh-Patel-Python-SA.git
cd IDAI-1000428-Mann-Paresh-Patel-Python-SA
```
#### Install required dependencies:

bash
`pip install streamlit pandas`
Run the application:

bash
`streamlit run app.py`
#### Access the application:
Open your web browser and navigate to http://localhost:8501

### Cloud Deployment (Streamlit Cloud):
Create a requirements.txt file with the following content:

```
streamlit
pandas
```
Upload your project to GitHub 

Go to Streamlit Cloud (streamlit.io/cloud)

Sign in with your GitHub account

Click "New app" and select your repository

Set the main file path to app.py

Click "Deploy" - Streamlit Cloud will handle the rest



## 🌐 Live Web App Link
The deployed application is accessible at: 
[Live Web App Link](https://idai-1000428-mann-paresh-patel-python-sa-3phcftgfqv79lotmp2vbq.streamlit.app/)

## 📁 Project Development Stages
### Stage 1: Sketching & Planning
Created rough digital sketches to model the app 
<img width="1279" height="830" alt="Screenshot 2026-01-24 175755" src="https://github.com/user-attachments/assets/d16be106-1d54-4e60-9754-eb8019a9dd6e" />
<img width="1412" height="703" alt="Screenshot 2026-01-24 175732" src="https://github.com/user-attachments/assets/5bf7ddb1-b726-4fb8-81b6-f0fd017ec23c" />

## 🏆 Gamification System Details
### Points System
#### Action	Points
Add a new medicine	+10
Take a medicine on time	+20
Earn a new badge	+50
Achieve 5-day streak	+100
Achieve 10-day streak	+250
#### Badges & Achievements
🌅 Early Bird: Take morning medications consistently

🦉 Night Owl: Take evening medications consistently

🏆 Perfect Week: 7 days of perfect adherence

👑 Consistency King: Long-term consistency

⚔️ Weekend Warrior: Maintain schedule on weekends

### Level System
Level 1: 0-99 points (Beginner)

Level 2: 100-199 points (Intermediate)

Level 3: 200-299 points (Advanced)

Level 4: 300+ points (Health Hero)

### 📊 User Tips & Best Practices
#### Daily Usage Tips
Set Daily Reminders: Use the app consistently at the same time each day

Track Side Effects: Use the notes feature to record any medication reactions

Stay Hydrated: Drink water with medications for better absorption

Weekly Review: Check your progress report every Sunday

Backup Plan: Always keep emergency doses available

#### Medication Management
💡 Set a daily reminder 5 minutes before medicine time

💡 Keep medicines visible but out of reach of children

💡 Drink a full glass of water with your medicine

💡 Track side effects in the notes section

💡 Set up a weekly pill organizer for convenience

💡 Always check expiration dates monthly

💡 Keep a backup supply for emergencies

💡 Store medicines away from heat and humidity

## 🛠️ Technical Architecture
### Built With
Streamlit: Web application framework

Pandas: Data manipulation and CSV export

HTML/CSS: Custom styling and animations

Python: Backend logic and gamification system

### Project Structure
text
```
IDAI-1000428-Mann-Paresh-Patel-Python-SA/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── Interactive Links/ # Deployment and access links

```
### Key Components
Session Management: Persistent user state across sessions

Gamification Engine: Points, badges, and streak calculations

UI Components: Custom cards, progress bars, and animations

Data Export: CSV generation and download functionality

Responsive Design: Mobile-friendly interface

## 🔧 Customization Guide
Changing Visual Themes
Edit the CSS variables in the custom styles section:

css
```
.main-header {
    background: linear-gradient(90deg, #NEW_COLOR_1 0%, #NEW_COLOR_2 100%);
}
```
### Adding New Features
New Badge Types: Extend the BADGE_TYPES dictionary

Additional Points: Modify points values in the gamification logic

New UI Components: Add custom Streamlit elements with matching CSS

### Extending Functionality
Connect to calendar APIs for automated reminders

Integrate with health tracking devices

Add social features for community support

Implement prescription management system
## Visuals of the App
<img width="1920" height="1080" alt="Screenshot (137)" src="https://github.com/user-attachments/assets/7e8081d8-7ed3-4236-864b-abc1db651c94" />
<img width="1920" height="1080" alt="Screenshot (138)" src="https://github.com/user-attachments/assets/6abeda41-5c97-43e2-af80-f2e0efb6d227" />
<img width="1920" height="1080" alt="Screenshot (139)" src="https://github.com/user-attachments/assets/e162afc1-0380-4d00-addf-3788b93e449f" />
<img width="1920" height="1080" alt="Screenshot (140)" src="https://github.com/user-attachments/assets/5c1a1701-4951-42de-aa5e-afa1b43eaf80" />
<img width="1920" height="1080" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/00ef2f97-234f-4919-b47b-df2404252e0b" />


## 🤝 Testing & Feedback
### Testing Methodology
Unit Testing: Individual component functionality

Integration Testing: End-to-end user workflows

User Acceptance Testing: Real-world usage scenarios

Performance Testing: Load and response time evaluation

### Feedback Collection
The application includes built-in mechanisms for:

User rating systems

Suggestion submission forms

Bug reporting interfaces

Usage analytics (with user consent)



Note: This tool is for tracking purposes only. Always consult with healthcare professionals regarding medication management.

## 🙏 Acknowledgments
Streamlit team for the amazing framework

Health professionals for medication management insights

Open source community for inspiration and tools

Educators and mentors for guidance throughout the project




###Track • Motivate • Thrive • Level Up Your Health Journey

