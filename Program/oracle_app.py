"""
Oracle Reading Generator - Streamlit Web Interface
A modern, mystical interface for generating I Ching readings based on runes.
"""

import streamlit as st
from datetime import datetime, timedelta
from pathlib import Path
import re
import os

from oracle_core import (
    RUNES, generate_reading_data, extract_hexagram_title
)
from oracle_markdown import generate_markdown_report
from oracle_ai import generate_ai_interpretation, get_api_key_instructions
from oracle_digital_draw import render_card_grid, reset_digital_draw
from translations import get_text, get_trigram_name


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="The Oracle - Rune Hexagram Reading",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================================
# CUSTOM STYLING
# ============================================================================

st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Header styling */
    .oracle-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #2d3561 0%, #1f2937 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    
    .oracle-title {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(135deg, #ffd700 0%, #ff8c00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-family: 'Georgia', serif;
    }
    
    .oracle-subtitle {
        font-size: 1.2rem;
        color: #d4af37;
        margin-bottom: 0;
        font-style: italic;
    }
    
    /* Result card styling */
    .result-card {
        background: linear-gradient(135deg, #2d3561 0%, #1f2937 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        border: 2px solid #d4af37;
    }
    
    .hexagram-display {
        text-align: center;
        font-size: 4rem;
        margin: 1rem 0;
        color: #ffd700;
    }
    
    .hexagram-title {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #ffd700;
        margin: 1rem 0;
        font-family: 'Georgia', serif;
    }
    
    .trigram-info {
        background: rgba(212, 175, 55, 0.1);
        border-left: 4px solid #d4af37;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
        color: #e5e5e5;
    }
    
    /* Expander customization - smaller size */
    .streamlit-expanderHeader {
        background-color: rgba(45, 53, 97, 0.6) !important;
        border-radius: 8px;
        font-weight: bold;
        font-size: 0.9rem !important;
        padding: 0.5rem 1rem !important;
    }
    
    /* Make expander content wider for better readability */
    .streamlit-expanderContent {
        max-width: 100% !important;
    }
    
    /* Ensure expander content uses full available width */
    div[data-testid="stExpander"] > div {
        width: 100% !important;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background-color: rgba(45, 53, 97, 0.4);
        color: #ffffff;
        border: 2px solid #d4af37;
        border-radius: 8px;
    }
    
    .stSelectbox > div > div > select {
        background-color: rgba(45, 53, 97, 0.4);
        color: #ffffff;
        border: 2px solid #d4af37;
        border-radius: 8px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #aa8e39 100%);
        color: #1a1a2e;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%);
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4);
    }
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, #4a5568 0%, #2d3748 100%);
        color: #ffd700;
        font-weight: bold;
        border: 2px solid #d4af37;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #5a6578 0%, #3d4758 100%);
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4);
    }
    
    /* Info messages */
    .info-text {
        color: #d4af37;
        font-style: italic;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ============================================================================
# CONFIGURATION
# ============================================================================

# Get API key from Streamlit secrets (secure for deployment)
# Falls back to environment variable for local development
try:
    api_key_to_use = st.secrets["GOOGLE_API_KEY"]
except:
    api_key_to_use = os.getenv('GOOGLE_API_KEY', None)

use_ai = True

# Store in session state
st.session_state['use_ai'] = use_ai
st.session_state['api_key'] = api_key_to_use

# Initialize language in session state (default to English)
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

# Initialize draw mode in session state
if 'draw_mode' not in st.session_state:
    st.session_state['draw_mode'] = None  # None = not chosen yet, 'manual' or 'digital'

# Initialize rate limiting
if 'rate_limit_count' not in st.session_state:
    st.session_state['rate_limit_count'] = 0
if 'rate_limit_time' not in st.session_state:
    st.session_state['rate_limit_time'] = datetime.now()


# ============================================================================
# HEADER WITH LANGUAGE TOGGLE
# ============================================================================

# Language toggle at the top
col_lang1, col_lang2, col_lang3 = st.columns([1, 1, 1])
with col_lang2:
    st.markdown("<div style='text-align: center; margin-bottom: 1rem;'>", unsafe_allow_html=True)
    col_en, col_nl = st.columns(2)
    with col_en:
        if st.button("🇬🇧 English", use_container_width=True, type="secondary" if st.session_state['language'] == 'nl' else "primary"):
            st.session_state['language'] = 'en'
            st.rerun()
    with col_nl:
        if st.button("🇳🇱 Nederlands", use_container_width=True, type="secondary" if st.session_state['language'] == 'en' else "primary"):
            st.session_state['language'] = 'nl'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Get current language
lang = st.session_state['language']

# Dynamic header based on language
st.markdown(f"""
<div class="oracle-header">
    <div class="oracle-title">🔮 {get_text(lang, 'title')} 🔮</div>
    <div class="oracle-subtitle">{get_text(lang, 'subtitle')}</div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# INTRODUCTION
# ============================================================================

intro_text = {
    'en': 'This oracle combines the wisdom of the Elder Futhark runes with the I Ching to provide deep insight into your situation. Draw two runes to reveal your path forward.',
    'nl': 'Dit orakel combineert de wijsheid van de Oudere Futhark runen met de I Tjing om diep inzicht te geven in jouw situatie. Trek twee runen om je pad vooruit te onthullen.'
}

st.markdown(f"""
<p style='text-align: center; color: #b8b8b8; font-size: 1.1rem; margin-bottom: 2rem;'>
{intro_text[lang]}
</p>
""", unsafe_allow_html=True)


# ============================================================================
# INPUT SECTION
# ============================================================================

# Create columns for better layout - wider center column for content
col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    # Instructions buttons side by side (smaller, at top)
    col_instr1, col_instr2 = st.columns([1, 1])
    
    with col_instr1:
        with st.expander(get_text(lang, 'instructions_button'), expanded=False):
            st.markdown(get_text(lang, 'instructions_content'), unsafe_allow_html=True)
    
    with col_instr2:
        with st.expander(get_text(lang, 'why_it_works_button'), expanded=False):
            st.markdown(get_text(lang, 'why_it_works_content'), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # User name input
    st.markdown(f"<h3 style='color: #ffd700; text-align: center;'>{get_text(lang, 'enter_name_header')}</h3>", unsafe_allow_html=True)
    user_name = st.text_input("", placeholder=get_text(lang, 'name_placeholder'), label_visibility="collapsed", key="user_name")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Question input (optional)
    st.markdown(f"<h3 style='color: #ffd700; text-align: center;'>{get_text(lang, 'question_header')}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #d4af37; text-align: center; font-style: italic; font-size: 0.9rem;'>{get_text(lang, 'question_description')}</p>", unsafe_allow_html=True)
    user_question = st.text_area(
        "",
        placeholder=get_text(lang, 'question_placeholder'),
        label_visibility="collapsed",
        height=80,
        key="user_question_input"
    )
    
    # Store question in session state
    st.session_state['user_question'] = user_question if user_question.strip() else None
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Draw Mode Selection (only show if name is entered and mode not yet chosen)
    if user_name.strip() and st.session_state['draw_mode'] is None:
        st.markdown(f"<h3 style='color: #ffd700; text-align: center;'>{get_text(lang, 'draw_mode_choice')}</h3>", unsafe_allow_html=True)
        
        col_manual, col_digital = st.columns(2)
        with col_manual:
            if st.button(get_text(lang, 'manual_draw_button'), use_container_width=True):
                st.session_state['draw_mode'] = 'manual'
                st.rerun()
        with col_digital:
            if st.button(get_text(lang, 'digital_draw_button'), use_container_width=True):
                st.session_state['draw_mode'] = 'digital'
                reset_digital_draw()  # Reset any previous digital draw state
                st.rerun()
    
    # Allow changing draw mode if already selected (small reset button)
    if user_name.strip() and st.session_state['draw_mode'] is not None:
        if st.button("🔄 Change Selection Method", use_container_width=False, type="secondary"):
            st.session_state['draw_mode'] = None
            reset_digital_draw()
            st.rerun()
    
    # Initialize rune selections
    rune1_selection = None
    rune2_selection = None
    
    # Show appropriate rune selection interface based on draw mode
    if st.session_state['draw_mode'] == 'digital':
        # Digital Draw Mode
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Render card grid
        selected_runes = render_card_grid(language=lang)
        
        if selected_runes[0] is not None and selected_runes[1] is not None:
            # Both runes selected via digital draw
            st.session_state['digital_rune1'] = selected_runes[0]
            st.session_state['digital_rune2'] = selected_runes[1]
            
            # Show selected runes
            st.markdown(f"""
            <div style='text-align: center; margin: 2rem 0; padding: 1.5rem; 
                        background: linear-gradient(135deg, #2d3561 0%, #1f2937 100%); 
                        border-radius: 15px; border: 2px solid #d4af37;'>
                <h3 style='color: #ffd700; margin-bottom: 1rem;'>{get_text(lang, 'cards_selected')}</h3>
                <p style='color: #ffd700; font-size: 1.2rem;'>
                    {get_text(lang, 'rune_label')} 1: {RUNES[selected_runes[0]]['name']} {RUNES[selected_runes[0]]['symbol']}<br>
                    {get_text(lang, 'rune_label')} 2: {RUNES[selected_runes[1]]['name']} {RUNES[selected_runes[1]]['symbol']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Set selections for the generate logic
            rune1_selection = f"{selected_runes[0]}. {RUNES[selected_runes[0]]['name']} {RUNES[selected_runes[0]]['symbol']}"
            rune2_selection = f"{selected_runes[1]}. {RUNES[selected_runes[1]]['name']} {RUNES[selected_runes[1]]['symbol']}"
            
            # Show generate button
            st.markdown("<br>", unsafe_allow_html=True)
            generate_button = st.button(get_text(lang, 'generate_button'), use_container_width=True)
        else:
            generate_button = False
            
    elif st.session_state['draw_mode'] == 'manual':
        # Manual Selection Mode (original dropdown interface)
        st.markdown(f"<h3 style='color: #ffd700; text-align: center;'>{get_text(lang, 'select_runes_header')}</h3>", unsafe_allow_html=True)
        
        st.markdown(f"<p style='color: #d4af37; text-align: center; font-style: italic;'>{get_text(lang, 'rune1_description')}</p>", unsafe_allow_html=True)
        rune1_options = [get_text(lang, 'select_rune1')] + [f"{num}. {RUNES[num]['name']} {RUNES[num]['symbol']}" for num in range(1, 25)]
        rune1_selection = st.selectbox(
            get_text(lang, 'rune_label') + " 1",
            rune1_options,
            label_visibility="collapsed",
            key="rune1",
            index=0
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"<p style='color: #d4af37; text-align: center; font-style: italic;'>{get_text(lang, 'rune2_description')}</p>", unsafe_allow_html=True)
        rune2_options = [get_text(lang, 'select_rune2')] + [f"{num}. {RUNES[num]['name']} {RUNES[num]['symbol']}" for num in range(1, 25)]
        rune2_selection = st.selectbox(
            get_text(lang, 'rune_label') + " 2",
            rune2_options,
            label_visibility="collapsed",
            key="rune2",
            index=0
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Generate button
        generate_button = st.button(get_text(lang, 'generate_button'), use_container_width=True)
    else:
        # No draw mode selected yet
        generate_button = False


# ============================================================================
# READING GENERATION
# ============================================================================

# Rate limiting configuration
RATE_LIMIT_COUNT = 5  # Max 5 readings
RATE_LIMIT_WINDOW = 3600  # Per hour (in seconds)

# Check if rate limit exceeded (only if button was clicked)
if generate_button:
    # Check if rate limit exceeded
    time_since_first = (datetime.now() - st.session_state['rate_limit_time']).total_seconds()
    
    if time_since_first > RATE_LIMIT_WINDOW:
        # Reset if hour has passed
        st.session_state['rate_limit_count'] = 0
        st.session_state['rate_limit_time'] = datetime.now()
    
    if st.session_state['rate_limit_count'] >= RATE_LIMIT_COUNT:
        remaining_time = int((RATE_LIMIT_WINDOW - time_since_first) / 60)
        st.error(f"⏱️ Rate limit reached. Please wait {remaining_time} minutes before generating another reading. (Limit: {RATE_LIMIT_COUNT} per hour)")
        generate_button = False

if generate_button:
    if not user_name.strip():
        st.warning(get_text(lang, 'error_name'))
    elif rune1_selection is None or (isinstance(rune1_selection, str) and rune1_selection.startswith("Select" if lang == 'en' else "Selecteer")):
        st.warning(get_text(lang, 'error_rune1'))
    elif rune2_selection is None or (isinstance(rune2_selection, str) and rune2_selection.startswith("Select" if lang == 'en' else "Selecteer")):
        st.warning(get_text(lang, 'error_rune2'))
    else:
        # Extract rune numbers from selections
        rune1_num = int(rune1_selection.split('.')[0])
        rune2_num = int(rune2_selection.split('.')[0])
        
        # Generate reading data
        consulting_text = "Het Orakel raadplegen..." if lang == 'nl' else "Consulting the Oracle..."
        with st.spinner(consulting_text):
            reading_data = generate_reading_data(rune1_num, rune2_num, user_name.strip(), language=lang)
        
        # Generate interpretation if enabled
        if st.session_state.get('use_ai', False) and st.session_state.get('api_key'):
            with st.spinner(f"✨ {get_text(lang, 'generating_interpretation')}"):
                ai_interpretation = generate_ai_interpretation(
                    reading_data, 
                    api_key=st.session_state['api_key'],
                    user_question=st.session_state.get('user_question'),
                    language=lang
                )
                reading_data['ai_interpretation'] = ai_interpretation
        
        # Store in session state
        st.session_state['reading_data'] = reading_data
        st.session_state['generated'] = True
        
        # Increment rate limit counter
        st.session_state['rate_limit_count'] += 1
        
        # Reset draw mode for next reading
        st.session_state['draw_mode'] = None
        reset_digital_draw()


# ============================================================================
# DISPLAY RESULTS
# ============================================================================

if st.session_state.get('generated', False):
    reading_data = st.session_state['reading_data']
    
    # Result card
    st.markdown(f"""
    <div class="result-card">
        <div class="hexagram-display">{reading_data['upper_trigram']['symbol']}<br>{reading_data['lower_trigram']['symbol']}</div>
        <div class="hexagram-title">{get_text(lang, 'hexagram')} {reading_data['hexagram']['number']}: {reading_data['hexagram']['title']}</div>
        <div class="trigram-info">
            <strong>{get_text(lang, 'upper_trigram')} ({get_text(lang, 'outer_strategy')}):</strong> {reading_data['upper_trigram']['symbol']} {reading_data['upper_trigram']['name']} 
            — {get_text(lang, 'influenced_by')} {reading_data['rune2']['name']} {reading_data['rune2']['symbol']}
        </div>
        <div class="trigram-info">
            <strong>{get_text(lang, 'lower_trigram')} ({get_text(lang, 'inner_foundation')}):</strong> {reading_data['lower_trigram']['symbol']} {reading_data['lower_trigram']['name']} 
            — {get_text(lang, 'influenced_by')} {reading_data['rune1']['name']} {reading_data['rune1']['symbol']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Expandable sections
    with st.expander(get_text(lang, 'literal_reading_title'), expanded=False):
        st.markdown(f"### {get_text(lang, 'reading_for')} {reading_data['user_name']}")
        st.markdown(f"*{get_text(lang, 'generated_label')}: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")
        st.markdown("---")
        
        # Two columns for runes
        col_r1, col_r2 = st.columns(2)
        
        with col_r1:
            st.markdown(f"#### {get_text(lang, 'rune_label')} 1: {reading_data['rune1']['name']} {reading_data['rune1']['symbol']}")
            st.markdown(f"**{get_text(lang, 'lower_trigram')}:** {reading_data['lower_trigram']['symbol']} {reading_data['lower_trigram']['name']}")
            st.markdown(reading_data['rune1']['content'])
        
        with col_r2:
            st.markdown(f"#### {get_text(lang, 'rune_label')} 2: {reading_data['rune2']['name']} {reading_data['rune2']['symbol']}")
            st.markdown(f"**{get_text(lang, 'upper_trigram')}:** {reading_data['upper_trigram']['symbol']} {reading_data['upper_trigram']['name']}")
            st.markdown(reading_data['rune2']['content'])
        
        st.markdown("---")
        st.markdown(f"### {get_text(lang, 'the_hexagram_label')}: {reading_data['hexagram']['title']}")
        st.markdown(reading_data['hexagram']['content'])
    
    with st.expander(get_text(lang, 'interpretation_title'), expanded=True):
        st.markdown(f"### {get_text(lang, 'interpretation_for')} {reading_data['user_name']}")
        st.markdown(f"*{get_text(lang, 'generated_label')}: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")
        st.markdown("---")
        
        # Display interpretation
        if reading_data.get('ai_interpretation'):
            st.markdown(reading_data['ai_interpretation'], unsafe_allow_html=True)
        else:
            st.markdown(reading_data.get('narrative_interpretation', ''), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Markdown Download button
    col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
    with col_d2:
        # Generate Markdown report in selected language
        markdown_report = generate_markdown_report(reading_data, language=lang)
        
        # Create filename with user name and timestamp
        safe_name = re.sub(r'[^\w\s-]', '', reading_data['user_name']).strip().replace(' ', '_')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        markdown_filename = f"oracle_reading_{safe_name}_{timestamp}.md"
        
        st.download_button(
            label=get_text(lang, 'download_markdown'),
            data=markdown_report,
            file_name=markdown_filename,
            mime="text/markdown",
            use_container_width=True
        )
        
        # Also save markdown files to Answers folder
        if st.button(get_text(lang, 'save_to_answers'), use_container_width=True):
            from datetime import datetime
            from pathlib import Path
            
            # Create Answers directory (in project root)
            answers_dir = Path(__file__).parent.parent / "Answers"
            answers_dir.mkdir(exist_ok=True)
            
            # Generate literal reading markdown
            literal_md = f"""# Oracle Reading
**For:** {reading_data['user_name']}
**Generated:** {datetime.now().strftime("%B %d, %Y at %I:%M:%S %p")}

---

## The Two Runes

### Rune 1: {reading_data['rune1']['name']} {reading_data['rune1']['symbol']} (The Root)
**Lower Trigram:** {reading_data['lower_trigram']['symbol']} {reading_data['lower_trigram']['name']}

{reading_data['rune1']['content']}

### Rune 2: {reading_data['rune2']['name']} {reading_data['rune2']['symbol']} (The Context)
**Upper Trigram:** {reading_data['upper_trigram']['symbol']} {reading_data['upper_trigram']['name']}

{reading_data['rune2']['content']}

---

## The Resulting Hexagram

### Hexagram {reading_data['hexagram']['number']}: {reading_data['hexagram']['title']}

{reading_data['hexagram']['content']}
"""
            
            # Save files
            reading_file = answers_dir / f"reading_{safe_name}_{timestamp}.md"
            with open(reading_file, 'w', encoding='utf-8') as f:
                f.write(literal_md)
            
            st.success(get_text(lang, 'files_saved'))


# ============================================================================
# FOOTER
# ============================================================================

footer_text = {
    'en': 'The Oracle combines the Elder Futhark runes with the I Ching hexagrams for a unique divination system based on ancient wisdom.',
    'nl': 'Het Orakel combineert de Oudere Futhark runen met de I Tjing hexagrammen voor een uniek divinatiesysteem gebaseerd op oude wijsheid.'
}

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align: center; color: #666; font-size: 0.9rem; padding: 2rem 0;'>
    <p>{footer_text[lang]}</p>
</div>
""", unsafe_allow_html=True)


