import streamlit as st
import plotly.graph_objects as go
import numpy as np
from src.theme import (apply_custom_theme, sidebar_header, sidebar_nav, 
                       breadcrumb, clinical_footer)

st.set_page_config(page_title="📊 Neural Stats", layout="wide")
apply_custom_theme()

# ── Sidebar ──
with st.sidebar:
    sidebar_header()
    sidebar_nav(active_page="stats")

# ── Top Nav ──
breadcrumb([("Dashboard", False), ("Stats for Nerds", True)])

# ═══════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.title("Technical Overview")
st.markdown("<p style='font-size: 1.05rem; color: #64748B; max-width: 800px; line-height: 1.7;'>How the neural architecture maps biological markers to psychometric professional outcomes.</p>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# METRICS SECTION
# ═══════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 1rem; border: 1px solid #F1F5F9;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">ACCURACY</div>
            <div style="display: flex; align-items: baseline; gap: 0.5rem; margin-top: 8px;">
                <span style="font-size: 1.8rem; font-weight: 800; color: #0F172A;">0.892</span>
                <span style="font-size: 0.75rem; color: #EF4444; font-weight: 600;">-1.4%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 1rem; border: 1px solid #F1F5F9;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">F1 SCORE</div>
            <div style="display: flex; align-items: baseline; gap: 0.5rem; margin-top: 8px;">
                <span style="font-size: 1.8rem; font-weight: 800; color: #0F172A;">0.874</span>
                <span style="font-size: 0.75rem; color: #10B981; font-weight: 600;">+0.8%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 1rem; border: 1px solid #F1F5F9;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">MSE</div>
            <div style="display: flex; align-items: baseline; gap: 0.5rem; margin-top: 8px;">
                <span style="font-size: 1.8rem; font-weight: 800; color: #0F172A;">0.121</span>
                <span style="font-size: 0.75rem; color: #EF4444; font-weight: 600;">-0.003</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 1rem; border: 1px solid #F1F5F9;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">DATASET SIZE</div>
            <div style="display: flex; align-items: baseline; gap: 0.5rem; margin-top: 8px;">
                <span style="font-size: 1.8rem; font-weight: 800; color: #0F172A;">10,000</span>
                <span style="font-size: 0.75rem; color: #94A3B8; font-weight: 600;">Samples</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# PERFORMANCE CURVES
# ═══════════════════════════════════════════════════════
col_loss, col_acc = st.columns(2)

with col_loss:
    st.markdown('<div class="dna-card">', unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span class="material-icons-outlined" style="font-size: 1.2rem; color: #0D9488;">show_chart</span>
                <span style="font-weight: 700; font-size: 1.05rem; color: #0F172A;">Loss Curve</span>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="font-size: 0.7rem; font-weight: 600; color: #0D9488;">● train_loss: .248</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    try:
        st.image('models/loss_curve.png', use_container_width=True)
    except:
        st.info("Loss curve visualization offline")
    st.markdown('</div>', unsafe_allow_html=True)

with col_acc:
    st.markdown('<div class="dna-card">', unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span class="material-icons-outlined" style="font-size: 1.2rem; color: #7C3AED;">insights</span>
                <span style="font-weight: 700; font-size: 1.05rem; color: #0F172A;">Accuracy Curve</span>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="font-size: 0.7rem; font-weight: 600; color: #7C3AED;">● validation: 0.88</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    try:
        st.image('models/accuracy_curve.png', use_container_width=True)
    except:
        st.info("Accuracy curve visualization offline")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# CONFUSION MATRIX - Interactive Heatmap
# ═══════════════════════════════════════════════════════
st.markdown('<div class="dna-card">', unsafe_allow_html=True)

col_cm_title, col_cm_controls = st.columns([2, 1])
with col_cm_title:
    st.markdown("### Confusion Matrix")
    st.markdown("<p style='font-size: 0.85rem; color: #64748B;'>Distribution of predicted career clusters vs. true genetic phenotypes.</p>", unsafe_allow_html=True)
with col_cm_controls:
    col_norm, col_cluster = st.columns(2)
    with col_norm:
        normalize = st.toggle("Normalized", value=True)
    with col_cluster:
        st.markdown("<span style='font-size: 0.7rem; font-weight: 600; color: #94A3B8;'>CLUSTER: K=8</span>", unsafe_allow_html=True)

st.image('models/confusion_matrix.png', use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# MODEL ARCHITECTURE + DATA PIPELINE
# ═══════════════════════════════════════════════════════
col_arch, col_pipe = st.columns(2)

with col_arch:
    st.markdown('<div class="dna-card">', unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 20px;">
            <span class="material-icons-outlined" style="font-size: 1.2rem; color: #0D9488;">hub</span>
            <span style="font-weight: 700; font-size: 1.15rem; color: #0F172A;">Model Architecture</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Input layer
    st.markdown("""
        <div style="background: #F8FAFC; border: 1px solid #F1F5F9; border-radius: 12px; padding: 16px; text-align: center; margin-bottom: 16px;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.05em;">INPUT LAYER</div>
            <div style="font-size: 0.85rem; font-weight: 600; color: #1E293B; margin-top: 4px;">(16 × 1) Feature Vector</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Arrow
    st.markdown("<div style='text-align: center; color: #CBD5E1; font-size: 1.2rem; margin: 8px 0;'>↓</div>", unsafe_allow_html=True)
    
    # Hidden layers
    layers = [
        ("DENSE_01", "Relu / 512"),
        ("DENSE_02", "Relu / 256"),
        ("DENSE_03", "Dropout 0.3"),
    ]
    
    col_l1, col_l2, col_l3 = st.columns(3)
    for col, (name, desc) in zip([col_l1, col_l2, col_l3], layers):
        with col:
            st.markdown(f"""
                <div style="background: #0D9488; border-radius: 12px; padding: 14px; text-align: center;">
                    <div style="font-size: 0.65rem; font-weight: 700; color: rgba(255,255,255,0.7); letter-spacing: 0.05em;">{name}</div>
                    <div style="font-size: 0.8rem; font-weight: 600; color: white; margin-top: 2px;">{desc}</div>
                </div>
            """, unsafe_allow_html=True)
    
    # Arrow
    st.markdown("<div style='text-align: center; color: #CBD5E1; font-size: 1.2rem; margin: 12px 0;'>↓</div>", unsafe_allow_html=True)
    
    # Output layer
    st.markdown("""
        <div style="background: #7C3AED; border-radius: 12px; padding: 16px; text-align: center;">
            <div style="font-size: 0.65rem; font-weight: 700; color: rgba(255,255,255,0.7); letter-spacing: 0.05em;">SOFTMAX OUTPUT</div>
            <div style="font-size: 0.85rem; font-weight: 600; color: white; margin-top: 2px;">(8 Career Archetypes)</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_pipe:
    st.markdown('<div class="dna-card">', unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 20px;">
            <span class="material-icons-outlined" style="font-size: 1.2rem; color: #7C3AED;">alt_route</span>
            <span style="font-weight: 700; font-size: 1.15rem; color: #0F172A;">Data Pipeline</span>
        </div>
    """, unsafe_allow_html=True)
    
    pipeline = [
        ("Questionnaire", "Self-reported psychometric data", "#F1F5F9", "#64748B"),
        ("Feature Engineering", "Dimensionality reduction & PCA", "#F1F5F9", "#64748B"),
        ("Scaling", "Z-score normalization of metrics", "#F1F5F9", "#64748B"),
        ("Inference Model", "Neural processing of markers", "#F1F5F9", "#64748B"),
        ("Career Prediction", "Final probability distribution", "#0D9488", "#FFFFFF"),
    ]
    
    for i, (title, desc, bg, text_col) in enumerate(pipeline):
        icon_bg = "#0D9488" if i == len(pipeline) - 1 else "#F1F5F9"
        icon_color = "white" if i == len(pipeline) - 1 else "#64748B"
        st.markdown(f"""
            <div style="display: flex; gap: 1rem; margin-bottom: 2rem; position: relative;">
                <div style="background: {icon_bg}; color: {icon_color}; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; z-index: 2; font-size: 0.8rem; font-weight: 700;">{i+1}</div>
                <div>
                    <div style="font-weight: 700; font-size: 0.9rem; color: #0F172A;">{title}</div>
                    <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 2px;">{desc}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ──
clinical_footer()