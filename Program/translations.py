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
        'instructions_button': '📖 How to Use The Oracle',
        'instructions_title': 'How to Use The Oracle',
        'instructions_content': '''
**The Goal of The Oracle:**
The Oracle combines ancient runic wisdom with I Ching hexagrams to provide guidance and insight into your situation. By drawing two runes, you generate a unique hexagram that reveals the landscape of your circumstances and offers strategic wisdom.

**Selecting Your Runes:**

1. **If you have already drawn runes physically:**
   - Choose "📝 Enter Runes Manually" when prompted
   - Use the dropdown menus to select the two runes you drew
   - This preserves your physical card draw

2. **If you want to draw runes digitally:**
   - Choose "🎴 Choose Cards Digitally" when prompted
   - Click on cards in a shuffled grid to reveal and select your runes
   - The cards will reshuffle between your first and second draw
   - This creates a digital card draw experience

**The Process:**
- Enter your name and optionally a question you seek guidance on
- Select or draw two runes: Rune 1 (The Root) and Rune 2 (The Context)
- The Oracle combines these runes to form a hexagram
- You'll receive a complete reading with interpretations tailored to your specific rune combination

**Understanding Your Reading:**
- **Rune 1 (The Root)**: Represents the inner foundation and the "why" of your situation
- **Rune 2 (The Context)**: Represents the outer strategy and the "how-to" of your situation
- **The Hexagram**: The objective landscape that emerges from combining these forces
''',
        'why_it_works_button': '🧠 Why The Oracle Works',
        'why_it_works_title': 'Why The Oracle Works',
        'why_it_works_content': '''
**How The Oracle Helps You Find Your Own Answers**

The oracle doesn't predict the future—it helps you discover wisdom that's already inside you. Here's how it works in five simple steps:

**1. The Ritual: Making It Matter**
When you take time to form a question and select your runes, you're investing effort. Because you've put in this effort, your mind naturally wants the reading to be meaningful and valuable. This makes you more open to finding guidance.

**2. The Prompt: Breaking Your Thought Patterns**
When you feel stuck, your usual ways of thinking keep going in circles. The oracle gives you something unexpected—a reading that doesn't immediately make sense. This makes your brain pause and ask: "How does this relate to my situation?" Your mind starts searching for connections.

**3. The "Aha!" Moment: Finding a New View**
The insight doesn't come from the runes—it comes from your own brain making new connections. This process helps you in two ways:
- **Seeing Things Differently:** Instead of "I'm failing," you might see "I'm rebuilding my life."
- **Getting Some Distance:** The symbolic language helps you step back from intense emotions and think more clearly.

**4. The "Click": Making It Personal**
Because you had to think about how the reading applies to you, it feels deeply personal—like it was meant for you. Since you did the mental work to understand it, the insight feels like your own discovery, not someone else's advice.

**5. The Action: Making It Real**
When you feel you've discovered something yourself, you're more likely to act on it. This insight becomes a personal mission. Your new belief (like "I can handle this") leads to new actions. Those actions are what actually create positive change in your life.

**The Big Picture**
The oracle is like a mirror—it reflects back what's already inside you, but in a way that helps you see it clearly. Instead of feeling like life just happens to you, you start feeling like you're actively creating your path forward.
''',
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
        'instructions_button': '📖 Hoe Het Orakel Te Gebruiken',
        'instructions_title': 'Hoe Het Orakel Te Gebruiken',
        'instructions_content': '''
**Het Doel van Het Orakel:**
Het Orakel combineert oude runische wijsheid met I Tjing hexagrammen om begeleiding en inzicht in jouw situatie te bieden. Door twee runen te trekken, genereer je een uniek hexagram dat het landschap van jouw omstandigheden onthult en strategische wijsheid biedt.

**Jouw Runen Selecteren:**

1. **Als je al fysiek runen hebt getrokken:**
   - Kies "📝 Runen Handmatig Invoeren" wanneer daarom wordt gevraagd
   - Gebruik de dropdown menu's om de twee runen te selecteren die je hebt getrokken
   - Dit behoudt je fysieke kaarttrekking

2. **Als je runen digitaal wilt trekken:**
   - Kies "🎴 Kaarten Digitaal Kiezen" wanneer daarom wordt gevraagd
   - Klik op kaarten in een geschudde grid om je runen te onthullen en te selecteren
   - De kaarten worden opnieuw geschud tussen je eerste en tweede trekking
   - Dit creëert een digitale kaarttrekkingservaring

**Het Proces:**
- Voer je naam in en optioneel een vraag waarover je begeleiding zoekt
- Selecteer of trek twee runen: Rune 1 (De Wortel) en Rune 2 (De Context)
- Het Orakel combineert deze runen om een hexagram te vormen
- Je ontvangt een complete lezing met interpretaties afgestemd op je specifieke rune combinatie

**Jouw Lezing Begrijpen:**
- **Rune 1 (De Wortel)**: Vertegenwoordigt het innerlijke fundament en het "waarom" van jouw situatie
- **Rune 2 (De Context)**: Vertegenwoordigt de externe strategie en het "hoe" van jouw situatie
- **Het Hexagram**: Het objectieve landschap dat ontstaat uit het combineren van deze krachten
''',
        'why_it_works_button': '🧠 Waarom Het Orakel Werkt',
        'why_it_works_title': 'Waarom Het Orakel Werkt',
        'why_it_works_content': '''
**Hoe Het Orakel Je Helpt Jouw Eigen Antwoorden Te Vinden**

Het orakel voorspelt de toekomst niet—het helpt je wijsheid te ontdekken die al in je zit. Dit is hoe het werkt in vijf eenvoudige stappen:

**1. Het Ritueel: Het Belangrijk Maken**
Wanneer je de tijd neemt om een vraag te formuleren en je runen te selecteren, investeer je inspanning. Omdat je deze moeite hebt gedaan, wil je geest van nature dat de lezing betekenisvol en waardevol is. Dit maakt je meer open voor het vinden van begeleiding.

**2. De Prompt: Je Denkpatronen Doorbreken**
Wanneer je je vast voelt zitten, blijven je gebruikelijke manieren van denken in cirkels ronddraaien. Het orakel geeft je iets onverwachts—een lezing die niet meteen duidelijk is. Dit doet je brein pauzeren en vragen: "Hoe heeft dit te maken met mijn situatie?" Je geest begint verbanden te zoeken.

**3. Het "Aha!" Moment: Een Nieuwe Kijk Vinden**
Het inzicht komt niet van de runen—het komt van je eigen brein dat nieuwe verbanden legt. Dit proces helpt je op twee manieren:
- **Anders Naar Dingen Kijken:** In plaats van "Ik faal," zie je misschien "Ik bouw mijn leven opnieuw op."
- **Afstand Nemen:** De symbolische taal helpt je om een stap terug te doen van intense emoties en helderder te denken.

**4. De "Klik": Het Persoonlijk Maken**
Omdat je moest nadenken over hoe de lezing op jou van toepassing is, voelt het diep persoonlijk—alsof het voor jou bedoeld was. Omdat je het mentale werk hebt gedaan om het te begrijpen, voelt het inzicht als je eigen ontdekking, niet als iemand anders advies.

**5. De Actie: Het Werkelijkheid Maken**
Wanneer je voelt dat je iets zelf hebt ontdekt, ben je eerder geneigd om ernaar te handelen. Dit inzicht wordt een persoonlijke missie. Je nieuwe overtuiging (zoals "Ik kan dit aan") leidt tot nieuwe acties. Die acties zijn wat daadwerkelijk positieve verandering in je leven creëert.

**Het Grote Plaatje**
Het orakel is als een spiegel—het reflecteert terug wat al in je zit, maar op een manier die je helpt het duidelijk te zien. In plaats van te voelen dat het leven je gewoon overkomt, begin je te voelen dat je actief je pad vooruit creëert.
''',
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

