import datetime

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)


def generate_insight_and_action(user_data):

    hour = datetime.datetime.now().hour
    bmi = user_data["bmi"]

    # Insight Logic
    if hour > 19:
        insight = "Late evening sugar may reduce your sleep quality."
    elif bmi > 25:
        insight = "Higher BMI may make sugar spikes stronger."
    else:
        insight = "Frequent sugar can impact your daily energy levels."

    # Action Logic
    if bmi > 25:
        action = "Try a protein snack instead next time."
    elif hour > 19:
        action = "Avoid sugar after 7PM today."
    else:
        action = "Take a 10-minute walk now."

    return insight, action
