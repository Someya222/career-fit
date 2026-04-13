import streamlit as st

def apply_custom_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Inter:wght@400;500;600&display=swap');
        @import url('https://fonts.googleapis.com/icon?family=Material+Icons+Outlined');

        /* ========== GLOBAL ========== */
        .stApp {
            background-color: #F8FAFC !important;
            color: #1E293B !important;
            font-family: 'Inter', sans-serif !important;
        }

        h1, h2, h3, h4 {
            font-family: 'Manrope', sans-serif !important;
            font-weight: 800 !important;
            color: #0F172A !important;
            letter-spacing: -0.03em !important;
        }

        /* ========== SIDEBAR CLEANUP ========== */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #F1F5F9 !important;
        }

        /* HIDE DEFAULT STREAMLIT NAV */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }

        [data-testid="stSidebar"] * {
            color: #1E293B !important;
        }

        /* ========== CARDS ========== */
        [data-testid="stVerticalBlock"] > div > div[style*="border"] {
            background-color: #FFFFFF !important;
            border: 1px solid #F1F5F9 !important;
            border-radius: 24px !important;
            box-shadow: 0 12px 24px -10px rgba(0, 0, 0, 0.04) !important;
            padding: 48px 56px !important;
            margin-bottom: 40px !important;
        }

        /* dna-card class */
        .dna-card {
            background: #FFFFFF;
            padding: 40px;
            border-radius: 24px;
            border: 1px solid #F1F5F9;
            box-shadow: 0 12px 24px -10px rgba(0, 0, 0, 0.04);
            margin-bottom: 24px;
        }

        /* ========== LIKERT SCALE (600px FIXED) ========== */
        .stRadio div[role="radiogroup"] {
            background-color: #F1F5F9 !important;
            border-radius: 100px !important;
            padding: 8px !important;
            display: flex !important;
            width: 600px !important;
            justify-content: space-between !important;
            border: none !important;
            margin: 24px 0 12px 0 !important;
        }

        /* Hide radio dots */
        .stRadio div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }

        /* Pill labels */
        .stRadio label[data-baseweb="radio"] {
            background-color: transparent !important;
            flex: 1 !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            height: 52px !important;
            border-radius: 100px !important;
            transition: all 0.2s ease !important;
        }

        /* Selected pill */
        .stRadio label[data-baseweb="radio"]:has(input:checked) {
            background-color: #0D9488 !important;
        }

        .stRadio label[data-baseweb="radio"]:has(input:checked) p {
            color: #FFFFFF !important;
            font-weight: 800 !important;
        }

        /* Unselected pill text */
        .stRadio label[data-baseweb="radio"] p {
            color: #94A3B8 !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            margin: 0 !important;
        }

        /* ========== PROGRESS BAR ========== */
        div[data-testid="stProgress"] > div > div > div > div {
            background-color: #0D9488 !important;
        }

        /* ========== BUTTONS ========== */
        button[kind="primary"] {
            background-color: #0D9488 !important;
            color: #FFFFFF !important;
            padding: 14px 40px !important;
            font-weight: 800 !important;
            border-radius: 16px !important;
            border: none !important;
        }

        /* Secondary/Clear Button Fix */
        .secondary-btn button {
            background-color: #FFFFFF !important;
            color: #475569 !important;
            border: 1px solid #CBD5E1 !important;
            padding: 14px 40px !important;
            font-weight: 700 !important;
            border-radius: 16px !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
        }
        
        .secondary-btn button:hover {
            border-color: #0D9488 !important;
            color: #0D9488 !important;
            background-color: #F0FDFA !important;
        }

        div.stButton > button {
            border-radius: 14px !important;
            font-weight: 600 !important;
            padding: 10px 24px !important;
        }

        /* ========== TOP NAV BAR ========== */
        .top-nav-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 0;
            margin-bottom: 8px;
            border-bottom: 1px solid #F1F5F9;
        }

        .top-nav-left {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.8rem;
            color: #94A3B8;
        }

        .top-nav-right {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .top-nav-search {
            background: #F8FAFC;
            border: 1px solid #F1F5F9;
            border-radius: 10px;
            padding: 8px 16px;
            font-size: 0.8rem;
            color: #94A3B8;
            min-width: 200px;
        }

        .top-nav-icon {
            width: 36px;
            height: 36px;
            background: #F8FAFC;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            color: #64748B;
        }

        .top-nav-avatar {
            width: 36px;
            height: 36px;
            background: #0D9488;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 0.8rem;
        }

        /* ========== BREADCRUMB ========== */
        .breadcrumb {
            font-size: 0.8rem;
            color: #94A3B8;
            margin-bottom: 4px;
        }
        .breadcrumb a {
            color: #94A3B8;
            text-decoration: none;
        }
        .breadcrumb .current {
            color: #0F172A;
            font-weight: 600;
        }

        /* ========== NAV LINK OVERRIDE ========== */
        .nav-link-active {
            background: #F0FDFA !important;
            color: #0D9488 !important;
            font-weight: 700 !important;
            border-radius: 12px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 4px;
            cursor: pointer;
        }

        .nav-link {
            color: #64748B !important;
            font-weight: 500;
            border-radius: 12px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 4px;
            cursor: pointer;
            text-decoration: none;
        }
        .nav-link:hover {
            background: #F8FAFC;
        }

        /* ========== HIDE STREAMLIT CHROME ========== */
        header, footer { visibility: hidden; }
        </style>
    """, unsafe_allow_html=True)


def sidebar_header():
    """Render the prototype sidebar header with logo and status indicator."""
    st.markdown("""
        <div style="padding: 8px 0 24px 0;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                <span style="font-size: 1.5rem;">🧬</span>
                <div>
                    <div style="font-weight: 800; font-size: 1.1rem; font-family: Manrope; color: #0F172A;">DNA-Level Career Fit</div>
                    <div style="font-weight: 800; font-size: 0.75rem; color: #0D9488; letter-spacing: 0.1em;">PREDICTOR</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")


def sidebar_nav(active_page="assessment"):
    """Render the simplified sidebar navigation with only 3 links."""
    st.page_link("app.py", label="Assessment")
    st.page_link("pages/results.py", label="Results")
    st.page_link("pages/stats.py", label="Stats")

def sidebar_status():
    pass

def sidebar_model_version():
    pass

def sidebar_researcher_profile():
    pass


def top_nav_bar(session_id="492-X"):
    """Render the top navigation bar matching the prototype."""
    st.markdown(f"""
        <div class="top-nav-bar">
            <div class="top-nav-left">
                <span style="font-weight: 600; color: #94A3B8;">Session: {session_id}</span>
            </div>
            <div class="top-nav-right">
                <div class="top-nav-search">
                    <span style="margin-right: 6px;">🔍</span> Search parameters...
                </div>
                <div class="top-nav-icon">🔔</div>
                <div class="top-nav-avatar">U</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def breadcrumb(items):
    """Render a breadcrumb trail.
    items: list of (label, is_current) tuples
    """
    parts = []
    for i, (label, is_current) in enumerate(items):
        if is_current:
            parts.append(f'<span class="current">{label}</span>')
        else:
            parts.append(f'<span>{label}</span>')
        if i < len(items) - 1:
            parts.append(' <span style="margin: 0 6px; color: #CBD5E1;">/</span> ')
    
    st.markdown(f'<div class="breadcrumb">{"".join(parts)}</div>', unsafe_allow_html=True)


def info_box(title, subtitle):
    st.markdown(f"""
        <div style="background: #FFFFFF; padding: 28px; border-radius: 20px; border: 1px solid #F1F5F9; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
            <div style="font-weight: 800; font-family: Manrope; color: #0F172A; margin-bottom: 6px; font-size: 1.05rem;">{title}</div>
            <div style="font-size: 13px; color: #64748B;">{subtitle}</div>
        </div>
    """, unsafe_allow_html=True)


def dark_footer():
    st.markdown("""
        <div style="background: #0F172A; color: #FFFFFF; padding: 64px; border-radius: 32px; margin-top: 64px;">
            <div style="font-size: 11px; font-weight: 700; color: #94A3B8; letter-spacing: 0.2em; margin-bottom: 24px;">SCIENTIFIC PROTOCOL V.2.4</div>
            <h2 style="color: #FFFFFF !important; font-size: 2rem; margin-bottom: 20px; letter-spacing: -0.02em;">How we calculate your fit.</h2>
            <p style="color: #94A3B8; max-width: 600px; line-height: 1.8; margin-bottom: 28px; font-size: 15px;">Our algorithm processes your DNA-level cognitive markers against a database of 4,000+ specialized career paths. This is not a simple personality test; it's a structural alignment of neuro-capabilities.</p>
            <a href="#" style="color: #FFFFFF; text-decoration: underline; font-weight: 700; font-size: 0.9rem;">Review the methodology &rarr;</a>
        </div>
    """, unsafe_allow_html=True)


def clinical_footer():
    """Bottom-of-page clinical editorial standard line."""
    st.markdown("""
        <div style="text-align: center; color: #CBD5E1; font-size: 0.7rem; margin-top: 80px; padding-bottom: 32px; letter-spacing: 0.12em; font-weight: 600;">
            CLINICAL EDITORIAL STANDARD &bull; GENERATED FOR SCIENTIFIC REVIEW &bull; SYSTEM LOG: 932-AX-CAREER
        </div>
    """, unsafe_allow_html=True)
