import streamlit as st
import datetime
import random
from utils import generate_insight_and_action, calculate_bmi

st.set_page_config(page_title="Beat the Sugar Spike", page_icon="🍬")

# ---------------- SESSION STATE ---------------- #

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "last_log_date" not in st.session_state:
    st.session_state.last_log_date = None

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# ---------------- ONBOARDING ---------------- #

if not st.session_state.user_data:

    st.title("🍬 Beat the Sugar Spike")

    st.subheader("Let's set up your profile")

    age = st.slider("Your Age", 16, 40)
    height = st.slider("Height (cm)", 140, 200)
    weight = st.slider("Weight (kg)", 40, 120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    if st.button("Start"):
        bmi = calculate_bmi(height, weight)
        st.session_state.user_data = {
            "age": age,
            "height": height,
            "weight": weight,
            "gender": gender,
            "bmi": bmi
        }
        st.success("Profile Created! 🎉")
        st.rerun()

# ---------------- MAIN APP ---------------- #

else:

    st.title("🔥 Daily Sugar Log")

    st.write(f"XP: {st.session_state.xp}")
    st.write(f"🔥 Streak: {st.session_state.streak} days")

    st.progress(min(st.session_state.streak / 30, 1.0))

    st.subheader("Log Your Sugar (Under 10 seconds!)")

    col1, col2 = st.columns(2)

    sugar_choice = None

    if col1.button("☕ Chai"):
        sugar_choice = "Chai"
    if col2.button("🍫 Sweet"):
        sugar_choice = "Sweet"
    if col1.button("🥤 Cold Drink"):
        sugar_choice = "Cold Drink"
    if col2.button("🍪 Snack"):
        sugar_choice = "Snack"

    if sugar_choice:

        today = datetime.date.today()

        # STREAK LOGIC
        if st.session_state.last_log_date:
            difference = (today - st.session_state.last_log_date).days
            if difference == 1:
                st.session_state.streak += 1
            elif difference > 1:
                st.session_state.streak = 1
        else:
            st.session_state.streak = 1

        st.session_state.last_log_date = today

        # VARIABLE XP
        xp_earned = random.randint(3, 7)
        st.session_state.xp += xp_earned

        # ML LOGIC
        insight, action = generate_insight_and_action(st.session_state.user_data)

        st.success(f"+{xp_earned} XP 🎉")
        st.info(f"💡 Insight: {insight}")
        st.warning(f"👉 Action: {action}")
