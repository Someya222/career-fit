import pandas as pd

def load_onet_careers():
    """Load career mapping"""
    return pd.read_csv('data/onet_careers.csv')

def get_archetype_description(archetype):
    """Return description for each archetype"""
    descriptions = {
        'Researcher': 'You thrive on abstract problems, deep focus, and intellectual novelty.',
        'Entrepreneur': 'You crave autonomy, risk, and immediate feedback. Comfort with uncertainty.',
        'Leader': 'People energize you. You naturally organize and motivate teams.',
        'Helper': 'Genuine care for others is your superpower. Helping = fulfillment.',
        'Analyst': 'You love patterns and systems. Detail work energizes you.',
        'Creator': 'Creative synthesis is natural. You see possibilities others miss.',
        'Strategist': 'Big-picture thinker. You see patterns and connections across domains.',
        'Builder': 'You turn ideas into reality. Tangible outputs energize you.'
    }
    return descriptions.get(archetype, '')

def get_group_role(archetype):
    """Return group role recommendation"""
    roles = {
        'Researcher': 'Problem-Solver & Strategist',
        'Entrepreneur': 'Risk-Taker & Opportunity Finder',
        'Leader': 'Motivator & Organizer',
        'Helper': 'Supporter & Team Player',
        'Analyst': 'Quality Controller & Detail Expert',
        'Creator': 'Innovator & Visionary',
        'Strategist': 'Strategic Planner & Vision Setter',
        'Builder': 'Executor & Technical Lead'
    }
    return roles.get(archetype, '')