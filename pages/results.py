import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from src.utils import get_archetype_description, get_group_role
from src.theme import (apply_custom_theme, sidebar_header, sidebar_nav, 
                       breadcrumb, clinical_footer)

st.set_page_config(page_title="✨ Neural Fit Results", layout="wide")
apply_custom_theme()

# ── Sidebar ──
with st.sidebar:
    sidebar_header()
    sidebar_nav(active_page="results")

# ── Top Nav + Breadcrumb ──
breadcrumb([("Dashboard", False), ("Career DNA Analysis", True)])

if 'result' not in st.session_state:
    st.warning("⬅️ Complete neural mapping first!")
    st.stop()

result = st.session_state.result
features = st.session_state.features.flatten()

# ═══════════════════════════════════════════════════════
# HEADER SECTION - Archetype Card + DNA Visual
# ═══════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
col_header_text, col_header_img = st.columns([2, 1])

with col_header_text:
    # Determine burnout level
    burnout_val = features[-1]
    if burnout_val < 40:
        burnout_label = "Low"
        burnout_color = "#10B981"
    elif burnout_val < 60:
        burnout_label = "Moderate"
        burnout_color = "#F59E0B"
    else:
        burnout_label = "High"
        burnout_color = "#EF4444"

    st.markdown(f"""
        <div style="background: white; padding: 3rem; border-radius: 1.5rem; border: 1px solid #F1F5F9; height: 100%;">
            <div style="background: #F3E8FF; color: #7C3AED; font-weight: 700; font-size: 0.75rem; padding: 0.25rem 0.75rem; border-radius: 2rem; display: inline-block; margin-bottom: 1.5rem; letter-spacing: 0.05em;">ARCHETYPE IDENTIFIED</div>
            <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">The {result['archetype']}</h1>
            <p style="font-size: 1.1rem; color: #64748B; line-height: 1.6;">{get_archetype_description(result['archetype'])}</p>
            <div style="display: flex; gap: 4rem; margin-top: 2rem;">
                <div>
                    <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">CAREER MATCH %</div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: #0D9488;">{result['confidence']*100:.1f}%</div>
                </div>
                <div>
                    <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">BURNOUT RISK</div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: {burnout_color};">● {burnout_label}</div>
                </div>
            </div>
            <div style="margin-top: 1.5rem; font-size: 0.7rem; color: #CBD5E1; letter-spacing: 0.05em;">Sequence Log: {result['confidence']*514.8:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col_header_img:
    st.markdown("""
        <div style="background: #0D9488; height: 100%; min-height: 350px; border-radius: 1.5rem; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
            <div style="width: 200px; height: 200px; border: 2px solid rgba(255,255,255,0.2); border-radius: 50%; position: absolute;"></div>
            <div style="width: 150px; height: 150px; border: 2px solid rgba(255,255,255,0.4); border-radius: 50%; position: absolute;"></div>
            <div style="width: 100px; height: 100px; border: 2px solid rgba(255,255,255,0.6); border-radius: 50%; position: absolute;"></div>
            <div style="font-size: 3rem; position: absolute;">🧬</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# TRAITS + SIMILARITY INDEX
# ═══════════════════════════════════════════════════════
col_radar, col_similarity = st.columns(2)

with col_radar:
    st.markdown('<div class="dna-card">', unsafe_allow_html=True)
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; margin-bottom: 12px;'>BIG FIVE TRAIT DISTRIBUTION</div>", unsafe_allow_html=True)
    traits = ['OPENNESS', 'CONSCIENTIOUSNESS', 'EXTRAVERSION', 'AGREEABLENESS', 'NEUROTICISM']
    values = list(features[:5])

    fig = go.Figure(data=go.Scatterpolar(
        r=values, 
        theta=traits, 
        fill='toself',
        fillcolor='rgba(13, 148, 136, 0.2)',
        line=dict(color='#0D9488', width=2)
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], showticklabels=False)),
        showlegend=False, margin=dict(t=30, b=30, l=60, r=60),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_similarity:
    st.markdown('<div class="dna-card">', unsafe_allow_html=True)
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; margin-bottom: 24px;'>SIMILARITY INDEX</div>", unsafe_allow_html=True)
    
    # Sort archetypes by probability, take top 4
    sorted_archetypes = sorted(result['all_archetypes'], key=lambda x: x[1], reverse=True)[:4]
    
    for arc, prob in sorted_archetypes:
        prob_pct = prob * 100
        bar_color = "#0D9488" if prob_pct > 50 else "#0D9488"
        st.markdown(f"""
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 500; margin-bottom: 0.5rem;">
                    <span style="font-weight: 600; color: #1E293B;">{arc}</span>
                    <span style="font-weight: 700; color: #0D9488;">{prob_pct:.1f}%</span>
                </div>
                <div style="background: #F1F5F9; height: 6px; border-radius: 3px;">
                    <div style="background: {bar_color}; width: {prob_pct}%; height: 100%; border-radius: 3px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# OPTIMAL CAREER PATHS
# ═══════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)

col_career_title, col_career_link = st.columns([3, 1])
with col_career_title:
    st.markdown("## Optimal Career Paths")
with col_career_link:
    st.markdown("<div style='text-align: right; padding-top: 16px;'><a href='#' style='color: #64748B; font-size: 0.85rem; font-weight: 600; text-decoration: none;'>View Full Clinical List →</a></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Career card metadata
career_tags = ["HIGH DEMAND", "BEST MATCH", "GROWTH ZONE", "NICHE FIT"]
career_tag_colors = [
    ("#F0FDFA", "#0D9488"),
    ("#FFF7ED", "#EA580C"),
    ("#F0FDF4", "#16A34A"),
    ("#F5F3FF", "#7C3AED")
]
career_salaries = ["$160k+", "$145k+", "$180k+", "$130k+"]
career_descriptions = [
    "Extracting patterns from genomic complexity.",
    "Directing complex laboratory operations.",
    "Engineering foundational digital structures.",
    "Navigating technical-moral landscapes."
]

career_cols = st.columns(4)
for i, career in enumerate(result['careers'][:4]):
    with career_cols[i]:
        tag = career_tags[i]
        bg, fg = career_tag_colors[i]
        salary = career_salaries[i]
        desc = career_descriptions[i] if i < len(career_descriptions) else "Specialized professional role."
        
        st.markdown(f"""
            <div style="background: white; padding: 2rem; border-radius: 1rem; border: 1px solid #F1F5F9; text-align: left; height: 100%;">
                <div style="background: #F8FAFC; width: 40px; height: 40px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; font-size: 1.2rem;">💼</div>
                <h4 style="margin-bottom: 0.5rem; font-size: 1.05rem;">{career}</h4>
                <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 2rem; line-height: 1.5;">{desc}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="background: {bg}; color: {fg}; font-size: 0.65rem; font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 0.25rem; letter-spacing: 0.03em;">{tag}</span>
                    <span style="font-weight: 700; font-size: 0.85rem; color: #1E293B;">{salary}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><hr style='border: none; border-top: 1px solid #F1F5F9;'><br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# WHY THIS FITS + ALIGNMENT SCORES
# ═══════════════════════════════════════════════════════
col_quote, col_stats = st.columns(2)

with col_quote:
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; margin-bottom: 16px;'>WHY THIS FITS YOU</div>", unsafe_allow_html=True)
    
    archetype_quotes = {
        'Researcher': "Your genetic markers show a high density of receptors associated with deep analytical processing. Your cognitive architecture is optimized for sustained abstract thought, making you an outlier in intellectual endurance.",
        'Entrepreneur': "Your neural patterns indicate an unusually high tolerance for ambiguity combined with rapid decision-making circuits. Where others see chaos, your brain maps opportunity structures in real-time.",
        'Leader': "Your genetic markers show elevated social-cognitive processing and organizational instincts. Your brain naturally models group dynamics and optimizes team configurations for maximum output.",
        'Helper': "Your neural architecture shows exceptional empathic resonance patterns. Your cognitive load actually decreases when supporting others, making altruistic work genuinely sustaining rather than draining.",
        'Analyst': "Your genetic markers show high-density pattern recognition receptors. Your cognitive architecture thrives on structured data processing, making detailed analytical work deeply satisfying.",
        'Creator': "Your neural pathways show enhanced divergent thinking capacity. Your brain generates novel connections between disparate concepts at 3x the rate of typical profiles.",
        'Strategist': "Your genetic markers show a high density of receptors associated with long-term pattern recognition. Unlike most, your cognitive load decreases as system complexity increases, making you an outlier in strategic resilience.",
        'Builder': "Your neural architecture shows exceptional spatial-mechanical processing. Your cognitive system is optimized for translating abstract concepts into concrete, functional implementations."
    }
    
    quote_text = archetype_quotes.get(result['archetype'], 
        "Your genetic markers show a high density of receptors associated with long-term pattern recognition. Unlike most, your cognitive load decreases as system complexity increases, making you an outlier in strategic resilience.")
    
    st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 1rem; border-left: 4px solid #0D9488;">
            <p style="font-style: italic; color: #475569; line-height: 1.8;">"{quote_text}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; margin-bottom: 16px;'>YOUR ROLE IN A TEAM</div>", unsafe_allow_html=True)
    
    group_role = get_group_role(result['archetype'])
    role_title = group_role.split('&')[0].strip() if '&' in group_role else group_role
    
    archetype_role_desc = {
        'Researcher': "You function as the intellectual anchor, providing deep analysis that grounds team decisions in evidence and rigorous methodology.",
        'Entrepreneur': "You act as the catalyst for action, pushing teams past analysis paralysis and turning abstract ideas into executable ventures.",
        'Leader': "You naturally organize and optimize team dynamics, ensuring every member contributes at their peak capacity.",
        'Helper': "You act as the emotional intelligence core, sensing team dynamics and mediating conflicts before they escalate.",
        'Analyst': "You serve as the quality assurance backbone, catching critical errors that others miss and ensuring data integrity.",
        'Creator': "You generate the novel solutions that break through conventional thinking, providing fresh perspectives on stale problems.",
        'Strategist': "You act as the north star for operational teams, identifying pitfalls six to twelve months before they manifest. You prefer quiet influence over loud leadership.",
        'Builder': "You transform team visions into tangible deliverables, bridging the gap between ideation and execution."
    }
    
    role_desc = archetype_role_desc.get(result['archetype'], 
        "You act as the north star for operational teams, identifying pitfalls six to twelve months before they manifest.")
    
    st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 1rem; display: flex; gap: 1.5rem; align-items: center;">
            <div style="background: #7C3AED; color: white; padding: 1rem; border-radius: 0.5rem; font-size: 1.2rem; flex-shrink: 0;">👥</div>
            <div>
                <div style="font-weight: 700; color: #7C3AED; font-size: 1.05rem;">The {role_title}</div>
                <div style="font-size: 0.85rem; color: #64748B; line-height: 1.6; margin-top: 4px;">{role_desc}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_stats:
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; margin-bottom: 16px;'>ALIGNMENT SCORES</div>", unsafe_allow_html=True)
    scores = [
        ("Energy Sustainability", features[-4]),
        ("Values Congruence", features[-3]),
        ("Intellectual Growth Potency", features[-2]),
        ("Burnout Resilience", 100 - features[-1])
    ]
    
    for label, score in scores:
        # Color coding based on score
        if score >= 70:
            bar_color = "#0D9488"
            score_color = "#0D9488"
        elif score >= 40:
            bar_color = "#F59E0B"
            score_color = "#F59E0B"
        else:
            bar_color = "#EF4444"
            score_color = "#EF4444"
        
        st.markdown(f"""
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 500; margin-bottom: 0.5rem;">
                    <span style="color: #1E293B; font-weight: 600;">{label}</span>
                    <span style="color: {score_color}; font-weight: 700;">{score:.0f}/100</span>
                </div>
                <div style="background: #F1F5F9; height: 8px; border-radius: 4px;">
                    <div style="background: {bar_color}; width: {score}%; height: 100%; border-radius: 4px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("📥 Download Clinical PDF Report", type="primary", use_container_width=True):
        st.success("Report generated (simulated)")

# ── Footer ──
clinical_footer()