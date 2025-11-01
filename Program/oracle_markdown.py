"""
Oracle Markdown Generator - Creates formatted markdown reports
"""

from datetime import datetime


# Markdown labels in different languages
MARKDOWN_LABELS = {
    'en': {
        'title': 'Oracle Reading for',
        'generated': 'Generated',
        'the_hexagram': 'The Hexagram',
        'hexagram': 'Hexagram',
        'structure': 'Structure',
        'upper_trigram': 'Upper Trigram (Outer/Strategy)',
        'lower_trigram': 'Lower Trigram (Inner/Foundation)',
        'influenced_by': 'influenced by',
        'the_two_runes': 'The Two Runes',
        'rune': 'Rune',
        'the_root': 'The Root',
        'the_context': 'The Context',
        'the_hexagram_reading': 'The Hexagram Reading',
        'oracle_interpretation': 'Oracle Interpretation',
        'quick_reference': 'Quick Reference',
        'reading_for': 'Reading for',
        'date': 'Date',
        'via': 'via',
        'footer': 'The Oracle: Rune-Hexagram Divination System'
    },
    'nl': {
        'title': 'Orakel Lezing voor',
        'generated': 'Gegenereerd',
        'the_hexagram': 'Het Hexagram',
        'hexagram': 'Hexagram',
        'structure': 'Structuur',
        'upper_trigram': 'Bovenste Trigram (Buitenkant/Strategie)',
        'lower_trigram': 'Onderste Trigram (Binnenkant/Fundament)',
        'influenced_by': 'beïnvloed door',
        'the_two_runes': 'De Twee Runen',
        'rune': 'Rune',
        'the_root': 'De Wortel',
        'the_context': 'De Context',
        'the_hexagram_reading': 'De Hexagram Lezing',
        'oracle_interpretation': 'Orakel Interpretatie',
        'quick_reference': 'Snelle Referentie',
        'reading_for': 'Lezing voor',
        'date': 'Datum',
        'via': 'via',
        'footer': 'Het Orakel: Rune-Hexagram Divinatie Systeem'
    }
}


def generate_markdown_report(reading_data, language='en'):
    """
    Generate a comprehensive markdown report for an oracle reading.
    
    Args:
        reading_data: Dictionary with reading information from oracle_core.generate_reading_data()
        language: Language code ('en' or 'nl')
    
    Returns:
        String containing the formatted markdown report
    """
    
    # Get labels for the selected language
    labels = MARKDOWN_LABELS.get(language, MARKDOWN_LABELS['en'])
    
    user_name = reading_data.get('user_name', 'Unknown')
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    rune1 = reading_data['rune1']
    rune2 = reading_data['rune2']
    lower_trigram = reading_data['lower_trigram']
    upper_trigram = reading_data['upper_trigram']
    hexagram = reading_data['hexagram']
    
    markdown = f"""# {labels['title']} {user_name}

**{labels['generated']}:** {timestamp}

---

## {labels['the_hexagram']}

### {upper_trigram['symbol']} {lower_trigram['symbol']} {labels['hexagram']} {hexagram['number']}: {hexagram['title']}

**{labels['structure']}:**
- **{labels['upper_trigram']}:** {upper_trigram['symbol']} {upper_trigram['name']} ({upper_trigram['chinese']}) — {labels['influenced_by']} {rune2['name']} {rune2['symbol']}
- **{labels['lower_trigram']}:** {lower_trigram['symbol']} {lower_trigram['name']} ({lower_trigram['chinese']}) — {labels['influenced_by']} {rune1['name']} {rune1['symbol']}

---

## {labels['the_two_runes']}

### {labels['rune']} 1: {rune1['name']} {rune1['symbol']} ({labels['the_root']})

**{labels['lower_trigram'].split('(')[0].strip()}:** {lower_trigram['symbol']} {lower_trigram['name']} ({lower_trigram['chinese']})

{rune1['content']}

---

### {labels['rune']} 2: {rune2['name']} {rune2['symbol']} ({labels['the_context']})

**{labels['upper_trigram'].split('(')[0].strip()}:** {upper_trigram['symbol']} {upper_trigram['name']} ({upper_trigram['chinese']})

{rune2['content']}

---

## {labels['the_hexagram_reading']}

{hexagram['content']}

---

## {labels['oracle_interpretation']}

"""
    
    # Add AI interpretation if available, otherwise template
    interpretation = reading_data.get('ai_interpretation') or reading_data.get('narrative_interpretation', '')
    markdown += interpretation
    
    markdown += f"""

---

## {labels['quick_reference']}

- **{labels['reading_for']}:** {user_name}
- **{labels['date']}:** {timestamp}
- **{labels['hexagram']}:** {hexagram['number']} - {hexagram['title']}
- **{labels['lower_trigram'].split('(')[0].strip()}:** {lower_trigram['symbol']} {lower_trigram['name']} {labels['via']} {rune1['name']} {rune1['symbol']}
- **{labels['upper_trigram'].split('(')[0].strip()}:** {upper_trigram['symbol']} {upper_trigram['name']} {labels['via']} {rune2['name']} {rune2['symbol']}

---

*{labels['footer']}*
"""
    
    return markdown

