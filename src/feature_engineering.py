import numpy as np
def questionnaire_to_features(responses):
    """Convert 12 Likert responses to 16 features"""
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12 = responses
    
    def scale(val):
        return (val - 1) / 4 * 100
    
    openness = (scale(q2) + scale(q5) + scale(q9)) / 3
    conscientiousness = (scale(q3) + scale(q12)) / 2
    
    agreeableness = (scale(q4) + scale(q10)) / 2
    neuroticism = 50 - (scale(q3) + scale(q6) + scale(q8)) / 3
    extraversion = (scale(8-q1) * 0.3 + scale(q8) * 0.7)
    logical_iq = (scale(q6) + scale(q9) + scale(q12)) / 3
    spatial_iq = (scale(q6) + scale(q9)) / 2
    interpersonal_iq = (scale(q4) + scale(q8) + scale(q10)) / 3
    
    autonomy_need = (scale(q7) + scale(q5) + scale(q1)) / 3
    collaboration_need = (scale(q8) + scale(6-q1)) / 2
    purpose_value = (scale(q10) + scale(q2)) / 2
    money_value = 50
    
    energy_alignment = 100 - abs(extraversion - 55)
    values_alignment = (purpose_value + autonomy_need) / 2
    growth_potential = (openness + conscientiousness) / 2
    burnout_risk = (neuroticism + (100 - autonomy_need)) / 2
    
    # Return 16 features
    return np.array([[
        openness, conscientiousness, extraversion, agreeableness, neuroticism,
        logical_iq, spatial_iq, interpersonal_iq,
        autonomy_need, collaboration_need, purpose_value, money_value,
        energy_alignment, values_alignment, growth_potential, burnout_risk
    ]])

