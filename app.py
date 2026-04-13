import streamlit as st
from src.feature_engineering import questionnaire_to_features
from src.predict import CareerPredictor
from src.theme import apply_custom_theme, info_box, dark_footer, sidebar_header, sidebar_nav

st.set_page_config(page_title="🧬 DNA-Level Career Fit", layout="wide")
apply_custom_theme()

# Unified Sidebar
with st.sidebar:
    sidebar_header()
    sidebar_nav(active_page="assessment")

# Persistent storage for responses
if "persistent_responses" not in st.session_state:
    st.session_state.persistent_responses = {i: None for i in range(1, 13)}

def update_persistent_response(idx):
    st.session_state.persistent_responses[idx] = st.session_state[f"val_{idx}"]

# Header Section
st.title("DNA-Level Career Fit Predictor")
st.markdown("<p style='font-size: 1.1rem; color: #64748B; max-width: 800px;'>Discover careers aligned with your personality and cognitive traits through our advanced neural-mapping assessment.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Info Cards and Progress
col_info1, col_info2, col_prog = st.columns([1, 1, 1])
with col_info1:
    info_box("Takes 2 minutes", "Rapid Response Protocol")
with col_info2:
    info_box("ML-Driven Engine", "Predictive Trait Mapping")
with col_prog:
    answered = sum(1 for v in st.session_state.persistent_responses.values() if v is not None)
    progress = answered / 12
    st.markdown("<div style='margin-left: 1rem;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: 800; font-size: 1.25rem; margin-bottom: 0.5rem;'>PROGRESS</p>", unsafe_allow_html=True)
    st.progress(progress)
    st.markdown(f"<p style='font-size: 0.8rem; color: #64748B; margin-top: 0.5rem;'>{answered} / 12 units mapped</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

questions = [
    "I prefer working alone over working in groups",
    "New and challenging problems excite me",
    "I organize my thoughts before speaking",
    "I can read how others feel without them saying it",
    "I get restless when work becomes routine",
    "I'm good at understanding complex systems",
    "I need independence and autonomy in work",
    "I thrive when working closely with a team",
    "I can see the big picture in complex situations",
    "Helping others gives me sense of purpose",
    "I'm comfortable with risk and uncertainty",
    "I prefer detailed work over abstract concepts"
]

responses = []
for idx, question in enumerate(questions, start=1):
    with st.container(border=True):
        col_idx, col_q = st.columns([1, 10])
        with col_idx:
            st.markdown(f'<div class="q-num">0{idx if idx < 10 else idx}</div>', unsafe_allow_html=True)
        with col_q:
            st.markdown(f"<div style='font-weight: 600; font-size: 1.25rem; color: #1E293B; margin-bottom: 1.5rem; margin-top: 0.5rem;'>{question}</div>", unsafe_allow_html=True)
            
            # Unified Interaction Block (Pill + Labels)
            val = st.radio(
                f"q_{idx}",
                options=[1, 2, 3, 4, 5],
                index=None if st.session_state.persistent_responses[idx] is None else st.session_state.persistent_responses[idx] - 1,
                key=f"val_{idx}",
                on_change=update_persistent_response,
                args=(idx,),
                label_visibility="collapsed",
                horizontal=True
            )
            responses.append(val)
            
            # Grid-based Label Alignment
            st.markdown(f"""
                <div style="display: grid; grid-template-columns: repeat(5, 1fr); width: 600px; margin-top: 10px;">
                    <div style="text-align: center; font-size: 0.7rem; font-weight: 800; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em;">Strongly<br>Disagree</div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div style="text-align: center; font-size: 0.7rem; font-weight: 800; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em;">Strongly<br>Agree</div>
                </div>
            """, unsafe_allow_html=True)

# Navigation Button
st.markdown("<br><br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("Get Career Recommendations", type="primary", use_container_width=True):
        # Fallback to neutral (3) for any skipped questions
        processed_responses = [r if r is not None else 3 for r in responses]
        features = questionnaire_to_features(processed_responses)
        
        @st.cache_resource
        def get_predictor():
            return CareerPredictor()
            
        predictor = get_predictor()
        result = predictor.predict(features)
        
        st.session_state.result = result
        st.session_state.features = features
        st.switch_page("pages/results.py")

