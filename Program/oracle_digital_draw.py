"""
Oracle Digital Draw Module - Interactive card selection interface
Allows users to select runes by clicking on animated cards in a grid.
"""

import streamlit as st
import random
from oracle_core import RUNES
from translations import get_text


def render_card_grid(language='en'):
    """
    Render the interactive card selection grid.
    Manages the two-step draw process with shuffling between draws.
    
    Args:
        language: Language code ('en' or 'nl')
    
    Returns:
        Tuple of (rune1_num, rune2_num) when both cards are selected, or (None, None) if incomplete
    """
    # Initialize session state for digital draw
    if 'digital_draw_step' not in st.session_state:
        st.session_state['digital_draw_step'] = 1  # Step 1 or 2
        st.session_state['digital_rune1'] = None
        st.session_state['digital_rune2'] = None
        st.session_state['card_order'] = None
        st.session_state['selected_card_index'] = None
    
    # Get current step
    step = st.session_state['digital_draw_step']

    # Ensure selected card index resets when step changes
    if 'last_step' not in st.session_state or st.session_state['last_step'] != step:
        st.session_state['selected_card_index'] = None
        st.session_state['last_step'] = step

    # Display instruction based on step
    if step == 1:
        st.markdown(f"<h3 style='color: #ffd700; text-align: center;'>{get_text(language, 'select_first_card')}</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color: #ffd700; text-align: center;'>{get_text(language, 'select_second_card')}</h3>", unsafe_allow_html=True)
    
    # Generate or regenerate shuffled card order for new step
    if st.session_state['card_order'] is None:
        # Create shuffled list of rune numbers (1-24)
        card_order = list(range(1, 25))
        random.shuffle(card_order)
        st.session_state['card_order'] = card_order
    
    # Add custom CSS for cards
    st.markdown("""
    <style>
        .rune-card {
            width: 100%;
            height: 180px;
            background: #000000;
            border: 2px solid #d4af37;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            color: #FFD700;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 10px;
        }
        .rune-card:focus {
            outline: none;
        }
        .rune-card-back {
            cursor: default;
        }
        .rune-card-back:hover {
            border-color: #d4af37;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
            transform: none;
        }
        .rune-card-back .gold-circle {
            width: 60px;
            height: 60px;
            border: 3px solid #FFD700;
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
        }
        .rune-card-front {
            border-color: #00ff00;
            box-shadow: 0 0 30px rgba(0, 255, 0, 0.5);
            cursor: default;
        }
        .rune-card-front:hover {
            transform: none;
            border-color: #00ff00;
            box-shadow: 0 0 30px rgba(0, 255, 0, 0.5);
        }
        .rune-symbol {
            font-size: 3rem;
            color: #FFD700;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
            margin-bottom: 10px;
        }
        .rune-name {
            font-size: 0.85rem;
            color: #FFD700;
            font-weight: bold;
            text-align: center;
            font-family: Georgia, serif;
        }
        /* Style selection buttons below cards */
        div[data-testid="column"] button[type="primary"] {
            background: linear-gradient(135deg, #d4af37 0%, #b8941f 100%) !important;
            border: 2px solid #ffd700 !important;
            color: #000000 !important;
            font-weight: bold !important;
            padding: 0.5rem 1rem !important;
            margin-top: -10px !important;
            border-radius: 8px !important;
            box-shadow: 0 4px 8px rgba(212, 175, 55, 0.3) !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            font-size: 1.5rem !important;
            line-height: 1 !important;
        }
        div[data-testid="column"] button[type="primary"]:hover {
            background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%) !important;
            box-shadow: 0 6px 12px rgba(255, 215, 0, 0.5) !important;
            transform: translateY(-2px) !important;
        }
        div[data-testid="column"] button[type="primary"]:focus {
            outline: none !important;
            box-shadow: 0 0 0 2px rgba(255, 215, 0, 0.4) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Render the card grid
    selected_card = render_interactive_cards(
        st.session_state['card_order'],
        language=language,
        step=step
    )
    
    # Handle card selection and progression
    if selected_card is not None:
        if step == 1:
            # Store the first selected rune
            st.session_state['digital_rune1'] = selected_card
            
            # Show the selected card info and a button to continue
            st.markdown("<br>", unsafe_allow_html=True)
            rune1_data = RUNES[selected_card]
            st.markdown(f"""
            <div style='text-align: center; margin: 1rem 0; padding: 1.5rem; 
                        background: linear-gradient(135deg, #2d3561 0%, #1f2937 100%); 
                        border-radius: 15px; border: 2px solid #00ff00;
                        box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);'>
                <h3 style='color: #00ff00; margin-bottom: 0.5rem;'>{get_text(language, 'first_rune_selected')}</h3>
                <p style='color: #ffd700; font-size: 1.5rem; margin: 0;'>{rune1_data['name']} {rune1_data['symbol']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Button to proceed to second draw
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button(get_text(language, 'choose_second_rune_button'), use_container_width=True, type="primary"):
                    st.session_state['digital_draw_step'] = 2
                    st.session_state['card_order'] = None  # Force reshuffle
                    st.session_state['selected_card_index'] = None  # Reset selection
                    st.rerun()
                    
        elif step == 2:
            # Store the second selected rune
            st.session_state['digital_rune2'] = selected_card
            # Both runes selected - return to main workflow
            return (st.session_state['digital_rune1'], st.session_state['digital_rune2'])
    
    # Show previously selected first rune if in step 2 (before selecting second card)
    if step == 2 and st.session_state.get('digital_rune1') is not None and selected_card is None:
        rune1_data = RUNES[st.session_state['digital_rune1']]
        st.markdown(f"""
        <div style='text-align: center; margin: 1rem 0; padding: 1rem; 
                    background: rgba(212, 175, 55, 0.1); border-radius: 10px; border: 2px solid #d4af37;'>
            <span style='color: #ffd700; font-size: 1.1rem;'>
                {get_text(language, 'first_rune_selected')}: {rune1_data['name']} {rune1_data['symbol']}
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    return (None, None)


def render_interactive_cards(card_order, language='en', step=1):
    """
    Render the interactive card grid using Streamlit columns with clickable card areas.
    
    Args:
        card_order: List of rune numbers in shuffled order
        language: Language code
        step: Current draw step (1 or 2)
    
    Returns:
        Selected card number or None
    """
    selected_card = None

    # Create 4 rows of 6 cards each
    for row in range(4):
        cols = st.columns(6)
        for col_idx in range(6):
            card_idx = row * 6 + col_idx
            if card_idx < 24:
                rune_num = card_order[card_idx]
                rune = RUNES[rune_num]
                
                with cols[col_idx]:
                    # Check if this card was clicked
                    is_flipped = st.session_state.get('selected_card_index') == card_idx
                    
                    if not is_flipped:
                        # Perfect card visual (already works)
                        st.markdown(f'''
                        <div class="rune-card rune-card-back">
                            <div class="gold-circle"></div>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        # Clearly labeled button below card
                        button_text = get_text(language, 'select_this_card')
                        clicked = st.button(
                            button_text,
                            key=f"card_{step}_{card_idx}",
                            use_container_width=True,
                            type="primary"
                        )
                        if clicked:
                            st.session_state['selected_card_index'] = card_idx
                            st.rerun()
                    else:
                        # Show flipped card front
                        st.markdown(f"""
                        <div class="rune-card rune-card-front">
                            <div class="rune-symbol">{rune['symbol']}</div>
                            <div class="rune-name">{rune['name']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Card is flipped, capture the selection
                        selected_card = rune_num

    return selected_card


def reset_digital_draw():
    """Reset the digital draw session state."""
    if 'digital_draw_step' in st.session_state:
        del st.session_state['digital_draw_step']
    if 'digital_rune1' in st.session_state:
        del st.session_state['digital_rune1']
    if 'digital_rune2' in st.session_state:
        del st.session_state['digital_rune2']
    if 'card_order' in st.session_state:
        del st.session_state['card_order']
    if 'selected_card_index' in st.session_state:
        del st.session_state['selected_card_index']
    if 'last_step' in st.session_state:
        del st.session_state['last_step']

