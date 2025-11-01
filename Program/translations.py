"""
Translation system for The Oracle
Supports English (en) and Dutch (nl)
"""

# UI Text Translations
UI_TEXT = {
    'en': {
        # Header
        'title': 'The Oracle',
        'subtitle': 'Ancient Wisdom Through Runes & I Ching',
        'language_label': 'Language',
        
        # User Input Section
        'enter_name_header': 'Enter Your Name',
        'name_placeholder': 'Your name...',
        'question_header': 'Your Question (Optional)',
        'question_description': 'What do you seek guidance on?',
        'question_placeholder': 'E.g., How should I approach my current career decision?',
        
        # Rune Selection
        'select_runes_header': 'Select Your Runes',
        'rune1_description': 'Rune 1 (The Root) — Lower Trigram',
        'rune2_description': 'Rune 2 (The Context) — Upper Trigram',
        'select_rune1': 'Select Rune 1...',
        'select_rune2': 'Select Rune 2...',
        'rune_label': 'Rune',
        
        # Buttons
        'generate_button': '✨ Generate Reading ✨',
        'download_markdown': '📥 Download Markdown Report',
        
        # Draw Mode Selection
        'draw_mode_choice': 'How would you like to select your runes?',
        'manual_draw_button': '📝 Enter Runes Manually',
        'digital_draw_button': '🎴 Choose Cards Digitally',
        'select_first_card': 'Select your first rune (then confirm at the bottom)...',
        'select_second_card': 'Select your second rune (then confirm at the bottom)...',
        'choose_second_rune_button': 'Choose Second Rune',
        'first_rune_selected': 'First Rune Selected',
        'cards_selected': 'Cards Selected',
        'select_this_card': '▲',
        
        # Messages
        'error_name': '⚠️ Please enter your name before generating a reading.',
        'error_rune1': '⚠️ Please select Rune 1 before generating a reading.',
        'error_rune2': '⚠️ Please select Rune 2 before generating a reading.',
        'generating_interpretation': 'Generating interpretation... (this may take 10-15 seconds)',
        'using_template': 'Using template-based interpretation...',
        
        # Results
        'your_reading': 'Your Reading',
        'the_two_runes': 'The Two Runes',
        'rune_the_root': '(The Root)',
        'rune_the_context': '(The Context)',
        'lower_trigram': 'Lower Trigram',
        'upper_trigram': 'Upper Trigram',
        'influenced_by': 'influenced by',
        'the_resulting_hexagram': 'The Resulting Hexagram',
        'hexagram': 'Hexagram',
        'structure': 'Structure',
        'outer_strategy': 'Outer/Strategy',
        'inner_foundation': 'Inner/Foundation',
        'the_interpretation': 'The Oracle\'s Interpretation',
        
        # Footer
        'footer_note': 'May this reading illuminate your path forward.',
        
        # Expanders
        'literal_reading_title': '📜 Literal Reading',
        'interpretation_title': '🔮 Interpretation',
        'reading_for': 'Reading for',
        'interpretation_for': 'Interpretation for',
        'generated_label': 'Generated',
        'the_hexagram_label': 'The Hexagram',
        'save_to_answers': '💾 Save to Answers Folder',
        'files_saved': '✅ Files saved successfully to Answers folder!',
    },
    'nl': {
        # Header
        'title': 'Het Orakel',
        'subtitle': 'Oude Wijsheid via Runen & I Tjing',
        'language_label': 'Taal',
        
        # User Input Section
        'enter_name_header': 'Voer Je Naam In',
        'name_placeholder': 'Jouw naam...',
        'question_header': 'Jouw Vraag (Optioneel)',
        'question_description': 'Waarover zoek je begeleiding?',
        'question_placeholder': 'Bijv., Hoe moet ik mijn huidige carrièrebeslissing benaderen?',
        
        # Rune Selection
        'select_runes_header': 'Selecteer Je Runen',
        'rune1_description': 'Rune 1 (De Wortel) — Onderste Trigram',
        'rune2_description': 'Rune 2 (De Context) — Bovenste Trigram',
        'select_rune1': 'Selecteer Rune 1...',
        'select_rune2': 'Selecteer Rune 2...',
        'rune_label': 'Rune',
        
        # Buttons
        'generate_button': '✨ Genereer Lezing ✨',
        'download_markdown': '📥 Download Markdown Rapport',
        
        # Draw Mode Selection
        'draw_mode_choice': 'Hoe wil je je runen selecteren?',
        'manual_draw_button': '📝 Runen Handmatig Invoeren',
        'digital_draw_button': '🎴 Kaarten Digitaal Kiezen',
        'select_first_card': 'Selecteer je eerste rune (bevestig daarna onderaan)...',
        'select_second_card': 'Selecteer je tweede rune (bevestig daarna onderaan)...',
        'choose_second_rune_button': 'Kies Tweede Rune',
        'first_rune_selected': 'Eerste Rune Geselecteerd',
        'cards_selected': 'Kaarten Geselecteerd',
        'select_this_card': '▲',
        
        # Messages
        'error_name': '⚠️ Voer alsjeblieft je naam in voordat je een lezing genereert.',
        'error_rune1': '⚠️ Selecteer alsjeblieft Rune 1 voordat je een lezing genereert.',
        'error_rune2': '⚠️ Selecteer alsjeblieft Rune 2 voordat je een lezing genereert.',
        'generating_interpretation': 'Interpretatie genereren... (dit kan 10-15 seconden duren)',
        'using_template': 'Gebruik sjabloongebaseerde interpretatie...',
        
        # Results
        'your_reading': 'Jouw Lezing',
        'the_two_runes': 'De Twee Runen',
        'rune_the_root': '(De Wortel)',
        'rune_the_context': '(De Context)',
        'lower_trigram': 'Onderste Trigram',
        'upper_trigram': 'Bovenste Trigram',
        'influenced_by': 'beïnvloed door',
        'the_resulting_hexagram': 'Het Resulterende Hexagram',
        'hexagram': 'Hexagram',
        'structure': 'Structuur',
        'outer_strategy': 'Buitenkant/Strategie',
        'inner_foundation': 'Binnenkant/Fundament',
        'the_interpretation': 'De Interpretatie van het Orakel',
        
        # Footer
        'footer_note': 'Moge deze lezing je pad vooruit verlichten.',
        
        # Expanders
        'literal_reading_title': '📜 Letterlijke Lezing',
        'interpretation_title': '🔮 Interpretatie',
        'reading_for': 'Lezing voor',
        'interpretation_for': 'Interpretatie voor',
        'generated_label': 'Gegenereerd',
        'the_hexagram_label': 'Het Hexagram',
        'save_to_answers': '💾 Opslaan in Antwoorden Map',
        'files_saved': '✅ Bestanden succesvol opgeslagen in de Antwoorden map!',
    }
}

# Trigram Translations
TRIGRAM_NAMES = {
    'en': {
        'Heaven': 'Heaven',
        'Earth': 'Earth',
        'Thunder': 'Thunder',
        'Water': 'Water',
        'Mountain': 'Mountain',
        'Wind': 'Wind',
        'Fire': 'Fire',
        'Lake': 'Lake',
    },
    'nl': {
        'Heaven': 'Hemel',
        'Earth': 'Aarde',
        'Thunder': 'Donder',
        'Water': 'Water',
        'Mountain': 'Berg',
        'Wind': 'Wind',
        'Fire': 'Vuur',
        'Lake': 'Meer',
    }
}

def get_text(language, key):
    """
    Get translated text for a given key in the specified language.
    Falls back to English if key not found.
    """
    if language in UI_TEXT and key in UI_TEXT[language]:
        return UI_TEXT[language][key]
    elif key in UI_TEXT['en']:
        return UI_TEXT['en'][key]
    else:
        return key

def get_trigram_name(language, english_name):
    """
    Get translated trigram name.
    """
    if language in TRIGRAM_NAMES and english_name in TRIGRAM_NAMES[language]:
        return TRIGRAM_NAMES[language][english_name]
    return english_name

