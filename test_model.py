import numpy as np
from src.feature_engineering import questionnaire_to_features
from src.predict import CareerPredictor

print("=" * 80)
print("COMPREHENSIVE MODEL TESTING - 4 DISTINCT PERSONALITY PROFILES")
print("=" * 80)

# Initialize predictor
try:
    predictor = CareerPredictor(
        'models/career_fit_model.h5',
        'models/label_encoder.pkl',
        'models/scaler.pkl',
        'data/onet_careers.csv'
    )
    print("[OK] Model loaded successfully\n")
except Exception as e:
    print(f"[ERROR] Error loading model: {e}")
    exit()

# ============================================================================
# PROFILE 1: RESEARCHER
# High Openness, High Conscientiousness, Low Extraversion
# Loves abstract problems, deep thinking, independent work
# ============================================================================
print("=" * 80)
print("PROFILE 1: RESEARCHER")
print("Traits: High Openness + High Conscientiousness + Low Extraversion")
print("=" * 80)

researcher_responses = [
    5,  # Q1: Prefer working alone (strongly agree)
    5,  # Q2: New challenges excite me (strongly agree)
    5,  # Q3: Organize thoughts before speaking (strongly agree)
    2,  # Q4: Read how others feel (disagree)
    5,  # Q5: Get restless with routine (strongly agree)
    5,  # Q6: Understand complex systems (strongly agree)
    5,  # Q7: Need independence/autonomy (strongly agree)
    1,  # Q8: Thrive in teamwork (strongly disagree)
    5,  # Q9: See the big picture (strongly agree)
    2,  # Q10: Helping gives purpose (disagree)
    4,  # Q11: Comfortable with risk (agree)
    5   # Q12: Details matter (strongly agree)
]

try:
    features = questionnaire_to_features(researcher_responses)
    result = predictor.predict(features)
    print(f"[OK] Predicted Archetype: {result['archetype']}")
    print(f"[OK] Confidence: {result['confidence']*100:.1f}%")
    print(f"\nAll Probabilities (sorted):")
    for arch, prob in sorted(result['probs'].items(), key=lambda x: x[1], reverse=True):
        bar_length = int(prob * 50)
        bar = "X" * bar_length + "." * (50 - bar_length)
        print(f"  {arch:15} {prob*100:5.1f}% {bar}")
    print(f"\n[TARGET] Expected: Researcher")
    print(f"[MATCH] Match: {'YES' if result['archetype'] == 'Researcher' else 'NO (but reasonable)'}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# ============================================================================
# PROFILE 2: ENTREPRENEUR
# High Openness, Low Conscientiousness, High Extraversion
# Loves risk, change, autonomy, quick feedback
# ============================================================================
print("=" * 80)
print("PROFILE 2: ENTREPRENEUR")
print("Traits: High Openness + Low Conscientiousness + High Extraversion")
print("=" * 80)

entrepreneur_responses = [
    2,  # Q1: Prefer working alone (disagree)
    5,  # Q2: New challenges excite me (strongly agree)
    1,  # Q3: Organize thoughts before speaking (strongly disagree - spontaneous)
    3,  # Q4: Read how others feel (neutral)
    5,  # Q5: Get restless with routine (strongly agree)
    2,  # Q6: Understand complex systems (disagree)
    5,  # Q7: Need independence/autonomy (strongly agree)
    4,  # Q8: Thrive in teamwork (agree)
    4,  # Q9: See the big picture (agree)
    2,  # Q10: Helping gives purpose (disagree)
    5,  # Q11: Comfortable with risk (strongly agree)
    1   # Q12: Details matter (strongly disagree)
]

try:
    features = questionnaire_to_features(entrepreneur_responses)
    result = predictor.predict(features)
    print(f"[OK] Predicted Archetype: {result['archetype']}")
    print(f"[OK] Confidence: {result['confidence']*100:.1f}%")
    print(f"\nAll Probabilities (sorted):")
    for arch, prob in sorted(result['probs'].items(), key=lambda x: x[1], reverse=True):
        bar_length = int(prob * 50)
        bar = "X" * bar_length + "." * (50 - bar_length)
        print(f"  {arch:15} {prob*100:5.1f}% {bar}")
    print(f"\n[TARGET] Expected: Entrepreneur")
    print(f"[MATCH] Match: {'YES' if result['archetype'] == 'Entrepreneur' else 'NO (but reasonable)'}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# ============================================================================
# PROFILE 3: LEADER
# High Extraversion, High Conscientiousness, Moderate Openness
# Energized by people, organizing teams, clear goals
# ============================================================================
print("=" * 80)
print("PROFILE 3: LEADER")
print("Traits: High Extraversion + High Conscientiousness + Moderate Openness")
print("=" * 80)

leader_responses = [
    2,  # Q1: Prefer working alone (disagree - prefer groups)
    4,  # Q2: New challenges excite me (agree)
    5,  # Q3: Organize thoughts before speaking (strongly agree - structured)
    4,  # Q4: Read how others feel (agree - understand people)
    2,  # Q5: Get restless with routine (disagree - like structure)
    3,  # Q6: Understand complex systems (neutral)
    3,  # Q7: Need independence/autonomy (neutral)
    5,  # Q8: Thrive in teamwork (strongly agree)
    3,  # Q9: See the big picture (neutral)
    4,  # Q10: Helping gives purpose (agree)
    2,  # Q11: Comfortable with risk (disagree - prefer safety)
    4   # Q12: Details matter (agree)
]

try:
    features = questionnaire_to_features(leader_responses)
    result = predictor.predict(features)
    print(f"[OK] Predicted Archetype: {result['archetype']}")
    print(f"[OK] Confidence: {result['confidence']*100:.1f}%")
    print(f"\nAll Probabilities (sorted):")
    for arch, prob in sorted(result['probs'].items(), key=lambda x: x[1], reverse=True):
        bar_length = int(prob * 50)
        bar = "X" * bar_length + "." * (50 - bar_length)
        print(f"  {arch:15} {prob*100:5.1f}% {bar}")
    print(f"\n[TARGET] Expected: Leader")
    print(f"[MATCH] Match: {'YES' if result['archetype'] == 'Leader' else 'NO (but reasonable)'}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# ============================================================================
# PROFILE 4: HELPER
# High Agreeableness, Low Extraversion, Moderate Conscientiousness
# Empathetic, caring, people-focused, supportive
# ============================================================================
print("=" * 80)
print("PROFILE 4: HELPER/NURTURER")
print("Traits: High Agreeableness + Moderate Extraversion + People-Focused")
print("=" * 80)

helper_responses = [
    3,  # Q1: Prefer working alone (neutral)
    2,  # Q2: New challenges excite me (disagree)
    4,  # Q3: Organize thoughts before speaking (agree)
    5,  # Q4: Read how others feel (strongly agree - empathetic)
    2,  # Q5: Get restless with routine (disagree)
    2,  # Q6: Understand complex systems (disagree)
    3,  # Q7: Need independence/autonomy (neutral)
    4,  # Q8: Thrive in teamwork (agree)
    2,  # Q9: See the big picture (disagree)
    5,  # Q10: Helping gives purpose (strongly agree)
    1,  # Q11: Comfortable with risk (strongly disagree)
    2   # Q12: Details matter (disagree)
]

try:
    features = questionnaire_to_features(helper_responses)
    result = predictor.predict(features)
    print(f"[OK] Predicted Archetype: {result['archetype']}")
    print(f"[OK] Confidence: {result['confidence']*100:.1f}%")
    print(f"\nAll Probabilities (sorted):")
    for arch, prob in sorted(result['probs'].items(), key=lambda x: x[1], reverse=True):
        bar_length = int(prob * 50)
        bar = "X" * bar_length + "." * (50 - bar_length)
        print(f"  {arch:15} {prob*100:5.1f}% {bar}")
    print(f"\n[TARGET] Expected: Helper")
    print(f"[MATCH] Match: {'YES' if result['archetype'] == 'Helper' else 'NO (but reasonable)'}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print("""
If all 4 profiles got DIFFERENT predictions, your model is EXCELLENT! ✅
If 3/4 match expected, your model is VERY GOOD! ✅
If 2/4 match, your model is GOOD (feature engineering can improve)
If <2/4 match, your model needs adjustment

The probabilities should also be DIFFERENT for each profile.
""")