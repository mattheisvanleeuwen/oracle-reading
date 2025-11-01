"""
Oracle Core Logic - Shared functions and data for the Oracle reading system.
"""

from pathlib import Path
import re
import os


# ============================================================================
# RUNE DATA AND MAPPINGS
# ============================================================================

RUNES = {
    # Aett 1: Freyr's Aett (1-8)
    1: {"name": "Fehu", "file": "1 - Fehu.md", "position": 1, "symbol": "ᚠ"},
    2: {"name": "Uruz", "file": "2 - Uruz.md", "position": 2, "symbol": "ᚢ"},
    3: {"name": "Thurisaz", "file": "3 - Thurisaz.md", "position": 3, "symbol": "ᚦ"},
    4: {"name": "Ansuz", "file": "4 - Ansuz.md", "position": 4, "symbol": "ᚫ"},
    5: {"name": "Raidho", "file": "5 - Raidho.md", "position": 5, "symbol": "ᚱ"},
    6: {"name": "Kenaz", "file": "6 - Kenaz.md", "position": 6, "symbol": "ᚲ"},
    7: {"name": "Gebo", "file": "7 - Gebo.md", "position": 7, "symbol": "ᚷ"},
    8: {"name": "Wunjo", "file": "8 - Wunjo.md", "position": 8, "symbol": "ᚹ"},
    # Aett 2: Heimdall's Aett (9-16)
    9: {"name": "Hagalaz", "file": "9 - Hagalaz.md", "position": 1, "symbol": "ᚺ"},
    10: {"name": "Nauthiz", "file": "10 - Nauthiz.md", "position": 2, "symbol": "ᚾ"},
    11: {"name": "Isa", "file": "11 - Isa.md", "position": 3, "symbol": "ᛁ"},
    12: {"name": "Jera", "file": "12 - Jera.md", "position": 4, "symbol": "ᛃ"},
    13: {"name": "Eihwaz", "file": "13 - Eihwaz.md", "position": 5, "symbol": "ᛇ"},
    14: {"name": "Perthro", "file": "14 - Perthro.md", "position": 6, "symbol": "ᛈ"},
    15: {"name": "Algiz", "file": "15 - Algiz.md", "position": 7, "symbol": "ᛉ"},
    16: {"name": "Sowilo", "file": "16 - Sowilo.md", "position": 8, "symbol": "ᛊ"},
    # Aett 3: Tyr's Aett (17-24)
    17: {"name": "Tiwaz", "file": "17 - Tiwaz.md", "position": 1, "symbol": "ᛏ"},
    18: {"name": "Berkano", "file": "18 - Berkano.md", "position": 2, "symbol": "ᛒ"},
    19: {"name": "Ehwaz", "file": "19 - Ehwaz.md", "position": 3, "symbol": "ᛖ"},
    20: {"name": "Mannaz", "file": "20 - Mannaz.md", "position": 4, "symbol": "ᛗ"},
    21: {"name": "Laguz", "file": "21 - Laguz.md", "position": 5, "symbol": "ᛚ"},
    22: {"name": "Ingwaz", "file": "22 - Ingwaz.md", "position": 6, "symbol": "ᛜ"},
    23: {"name": "Dagaz", "file": "23 - Dagaz.md", "position": 7, "symbol": "ᛞ"},
    24: {"name": "Othala", "file": "24 - Othala.md", "position": 8, "symbol": "ᛟ"},
}

POSITION_TO_TRIGRAM = {
    1: {"name": "Thunder", "chinese": "Zhèn", "symbol": "☳"},
    2: {"name": "Earth", "chinese": "Kūn", "symbol": "☷"},
    3: {"name": "Mountain", "chinese": "Gèn", "symbol": "☶"},
    4: {"name": "Heaven", "chinese": "Qián", "symbol": "☰"},
    5: {"name": "Water", "chinese": "Kǎn", "symbol": "☵"},
    6: {"name": "Fire", "chinese": "Lí", "symbol": "☲"},
    7: {"name": "Wind", "chinese": "Xùn", "symbol": "☴"},
    8: {"name": "Lake", "chinese": "Duí", "symbol": "☱"},
}

TRIGRAM_TO_HEXAGRAM = {
    ("Heaven", "Heaven"): 1, ("Heaven", "Earth"): 11, ("Heaven", "Thunder"): 34, ("Heaven", "Water"): 5,
    ("Heaven", "Mountain"): 26, ("Heaven", "Wind"): 9, ("Heaven", "Fire"): 14, ("Heaven", "Lake"): 43,
    ("Earth", "Heaven"): 12, ("Earth", "Earth"): 2, ("Earth", "Thunder"): 16, ("Earth", "Water"): 8,
    ("Earth", "Mountain"): 23, ("Earth", "Wind"): 20, ("Earth", "Fire"): 35, ("Earth", "Lake"): 45,
    ("Thunder", "Heaven"): 25, ("Thunder", "Earth"): 24, ("Thunder", "Thunder"): 51, ("Thunder", "Water"): 3,
    ("Thunder", "Mountain"): 27, ("Thunder", "Wind"): 42, ("Thunder", "Fire"): 21, ("Thunder", "Lake"): 17,
    ("Water", "Heaven"): 6, ("Water", "Earth"): 7, ("Water", "Thunder"): 40, ("Water", "Water"): 29,
    ("Water", "Mountain"): 4, ("Water", "Wind"): 59, ("Water", "Fire"): 64, ("Water", "Lake"): 47,
    ("Mountain", "Heaven"): 33, ("Mountain", "Earth"): 15, ("Mountain", "Thunder"): 62, ("Mountain", "Water"): 39,
    ("Mountain", "Mountain"): 52, ("Mountain", "Wind"): 53, ("Mountain", "Fire"): 56, ("Mountain", "Lake"): 31,
    ("Wind", "Heaven"): 44, ("Wind", "Earth"): 46, ("Wind", "Thunder"): 32, ("Wind", "Water"): 48,
    ("Wind", "Mountain"): 18, ("Wind", "Wind"): 57, ("Wind", "Fire"): 50, ("Wind", "Lake"): 28,
    ("Fire", "Heaven"): 13, ("Fire", "Earth"): 36, ("Fire", "Thunder"): 55, ("Fire", "Water"): 63,
    ("Fire", "Mountain"): 22, ("Fire", "Wind"): 37, ("Fire", "Fire"): 30, ("Fire", "Lake"): 49,
    ("Lake", "Heaven"): 10, ("Lake", "Earth"): 19, ("Lake", "Thunder"): 54, ("Lake", "Water"): 60,
    ("Lake", "Mountain"): 41, ("Lake", "Wind"): 61, ("Lake", "Fire"): 38, ("Lake", "Lake"): 58,
}

HEXAGRAM_FILES = {
    1: "1 - CREATIVE POWER  (THE CREATIVE).md", 2: "2 - NATURAL RESPONSE (THE RECEPTIVE).md",
    3: "3 - DIFFICULT BEGINNINGS.md", 4: "4 - INEXPERIENCE (YOUTHFUL FOLLY).md",
    5: "5 - CALCULATED WAITING.md", 6: "6 - CONFLICT.md", 7: "7 - COLLECTIVE FORCE (THE ARMY).md",
    8: "8 - UNITY.md", 9: "9 - RESTRAINED.md", 10: "10 - CONDUCT.md", 11: "11 - PROSPERING (PEACE).md",
    12: "12 - STAGNATION.md", 13: "13 - COMMUNITY (FELLOWSHIP WITH MEN).md",
    14: "14 - SOVEREIGNTY (POSSESSION IN GREAT MEASURE).md", 15: "15 - MODERATION (MODESTY).md",
    16: "16 - HARMONIZE (ENTHUSIASM).md", 17: "17 - ADAPTING (FOLLOWING).md", 18: "18 - REPAIR (DECAY).md",
    19: "19 - PROMOTION.md", 20: "20 - CONTEMPLATING.md", 21: "21 - REFORM (BITING THROUGH).md",
    22: "22 - GRACE.md", 23: "23 - DETERIORATION (SPLITTING APART).md", 24: "24 - RETURNING.md",
    25: "25 - INNOCENCE.md", 26: "26 - POTENTIAL ENERGY (THE TAMING POWER OF THE GREAT).md",
    27: "27 - NOURISHING.md", 28: "28 - CRITICAL MASS (PREPONDERANCE OF THE GREAT).md",
    29: "29 - DANGER.md", 30: "30 - SYNERGY (THE CLINGING).md", 31: "31 - ATTRACTION.md",
    32: "32 - CONTINUING (ENDURING).md", 33: "33 - RETREAT.md", 34: "34 - GREAT POWER.md",
    35: "35 - PROGRESS.md", 36: "36 - CENSORSHIP (DARKENING OF THE LIGHT).md", 37: "37 - FAMILY.md",
    38: "38 - CONTRADICTION (OPPOSITION).md", 39: "39 - NEW SCAN NECESSARY.md",
    40: "40 - LIBERATION (DELIVERANCE).md", 41: "41 - DECLINE.md", 42: "42 - BENEFIT (INCREASE)..md",
    43: "43 - RESOLUTION.md", 44: "44 - TEMPTATION.md", 45: "45 - ASSEMBLING.md",
    46: "46 - ADVANCEMENT (PUSHING UPWARD).md", 47: "47 - ADVERSITY.md",
    48: "48 - THE SOURCE (THE WELL).md", 49: "49 - CHANGING (REVOLUTION).md",
    50: "50 - COSMIC ORDER (THE CAULDRON).md", 51: "51 - SHOCKING.md",
    52: "52 - MEDITATION (KEEPING STILL).md", 53: "53 - DEVELOPING.md",
    54: "54 - SUBORDINATE (THE MARRYING MAIDEN).md", 55: "55 - ZENITH (ABUNDANCE).md",
    56: "56 - TRAVELING.md", 57: "57 - PENETRATING INFLUENCE (THE GENTLE).md",
    58: "58 - ENCOURAGING (JOY).md", 59: "59 - REUNITING (DISPERSION).md", 60: "60 - LIMITATIONS.md",
    61: "61 - INSIGHT (INNER TRUTH).md", 62: "62 - CONSCIENTIOUSNESS (PREPONDERANCE OF THE SMALL).md",
    63: "63 - AFTER THE END.md", 64: "64 - BEFORE THE END.md",
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_rune_by_input(user_input):
    """Parse user input and return rune number. Accepts name or number (1-24)."""
    user_input = str(user_input).strip()
    
    try:
        num = int(user_input)
        if 1 <= num <= 24:
            return num
    except ValueError:
        pass
    
    user_input_lower = user_input.lower()
    for num, rune_data in RUNES.items():
        if rune_data["name"].lower() == user_input_lower:
            return num
    
    return None


def get_trigram_from_rune(rune_num):
    """Convert a rune number to its corresponding trigram."""
    position = RUNES[rune_num]["position"]
    return POSITION_TO_TRIGRAM[position]


def get_hexagram_from_trigrams(lower_trigram, upper_trigram):
    """Get hexagram number from lower and upper trigrams."""
    key = (upper_trigram["name"], lower_trigram["name"])
    return TRIGRAM_TO_HEXAGRAM.get(key)


def read_file_content(filepath):
    """Read and return the content of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"[File not found: {filepath}]"
    except Exception as e:
        return f"[Error reading file: {e}]"


def extract_interpretive_lens(rune_content):
    """Extract the 'Interpretive Lens' section from rune content."""
    match = re.search(r'\*\*Interpretive Lens.*?\*\*:(.*?)(?=\n###|\n\*\*[A-Z]|\Z)', 
                     rune_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_oracle_interpretation(rune_content):
    """Extract the 'Oracle Interpretation' section from rune content."""
    match = re.search(r'\*\*Oracle Interpretation:\*\*(.*?)(?=\n\*|\Z)', 
                     rune_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_hexagram_title(hexagram_content):
    """Extract the hexagram title from content."""
    match = re.search(r'CHAPTER \d+:\s*\*\*(.+?)\*\*', hexagram_content)
    if match:
        return match.group(1).strip()
    return "Unknown Hexagram"


def get_base_path():
    """Get the base path for file operations."""
    # Return project root (parent of Program folder)
    return Path(__file__).parent.parent


def read_rune_file(rune_num):
    """Read and return rune file content."""
    base_path = get_base_path()
    rune_path = base_path / "Runes" / RUNES[rune_num]["file"]
    return read_file_content(rune_path)


def read_hexagram_file(hexagram_num):
    """Read and return hexagram file content."""
    base_path = get_base_path()
    hex_path = base_path / "I Ching" / HEXAGRAM_FILES[hexagram_num]
    return read_file_content(hex_path)


def generate_narrative_interpretation(reading_data):
    """
    Generate a cohesive narrative interpretation that weaves together
    the hexagram meaning with both rune meanings.
    """
    hex_title = reading_data['hexagram']['title']
    hex_num = reading_data['hexagram']['number']
    
    rune1_name = reading_data['rune1']['name']
    rune1_oracle = reading_data['rune1']['oracle']
    lower_trigram = reading_data['lower_trigram']['name']
    
    rune2_name = reading_data['rune2']['name']
    rune2_oracle = reading_data['rune2']['oracle']
    upper_trigram = reading_data['upper_trigram']['name']
    
    # Extract key concepts from hexagram (first paragraph usually has the essence)
    hex_content = reading_data['hexagram']['content']
    hex_paragraphs = [p.strip() for p in hex_content.split('\n\n') if p.strip() and not p.strip().startswith('#')]
    hex_essence = hex_paragraphs[0] if hex_paragraphs else ""
    
    narrative = f"""Your reading reveals the landscape of <b>{hex_title}</b> (Hexagram {hex_num}), a profound situation shaped by two powerful forces working in concert.

<b>The Situation:</b> {hex_essence}

<b>The Inner Foundation - {rune1_name} as {lower_trigram}:</b><br/>
At the core of this situation lies {rune1_name}, which manifests as the {lower_trigram} trigram in your inner world. {rune1_oracle} This internal energy colors everything you're experiencing from within. The {lower_trigram} force of {rune1_name} is the WHY behind this hexagram's manifestation in your life—it is the deep current flowing beneath the surface, the foundation upon which your current reality rests.

When {rune1_name} flavors the {lower_trigram} aspect of {hex_title}, it means that the very essence of this situation is rooted in the qualities of {rune1_name}. This is not just happening TO you; it is arising FROM the {rune1_name} energy within your inner world. The {lower_trigram} trigram represents your foundation, your core motivation, and the unconscious forces at work.

<b>The Outer Strategy - {rune2_name} as {upper_trigram}:</b><br/>
The path through this landscape is illuminated by {rune2_name}, which manifests as the {upper_trigram} trigram in how you engage with the world. {rune2_oracle} This external energy shapes your approach and defines HOW you should navigate the situation described in {hex_title}.

{rune2_name} flavoring the {upper_trigram} aspect means that your strategy, your visible actions, and your conscious approach should embody the wisdom of {rune2_name}. The {upper_trigram} trigram is your outer face, your method of engagement, the tool you wield as you move through this time.

<b>The Integration - Your Path Forward:</b><br/>
This reading calls you to recognize that {hex_title} is not a static situation but a dynamic interplay. Your internal reality ({rune1_name}/{lower_trigram}) is seeking expression and resolution through the external strategy ({rune2_name}/{upper_trigram}). 

The wisdom here is to honor both forces: ground yourself in the {rune1_name} energy that forms your foundation while actively employing the {rune2_name} approach in your outward actions. When you align your inner {lower_trigram} nature with your outer {upper_trigram} strategy, you move in harmony with the natural flow of {hex_title}.

This is your moment to embody the full teaching of this hexagram, informed by the specific runic energies you've drawn. Let {rune1_name} be your anchor, and {rune2_name} be your sail."""

    return narrative


def translate_text(text, api_key=None):
    """
    Translate text from English to Dutch using Google Gemini.
    Returns translated text or original if translation fails.
    """
    try:
        import google.generativeai as genai
        
        # Get API key
        if api_key is None:
            api_key = os.getenv('GOOGLE_API_KEY')
        
        if not api_key:
            return text  # Return original if no API key
        
        # Configure and translate
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        prompt = f"""Translate the following oracle/divination text from English to Dutch. 
Maintain the mystical, ancient tone and keep all formatting (markdown, bold, italics, etc.). 
Translate naturally while preserving the spiritual and divinatory nature of the text.
Do not add any explanations or comments, only provide the translation.

TEXT TO TRANSLATE:
{text}

TRANSLATION IN DUTCH:"""
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.3,  # Lower temperature for more consistent translation
                max_output_tokens=8000,
            )
        )
        
        return response.text.strip()
    except Exception as e:
        # Fail silently and return original text
        print(f"Translation error: {e}")
        return text


def generate_reading_data(rune1_num, rune2_num, user_name="", language='en'):
    """
    Generate complete reading data for the given runes.
    Returns a dictionary with all reading information.
    
    Args:
        rune1_num: Number of first rune (1-24)
        rune2_num: Number of second rune (1-24)
        user_name: Name of the person receiving the reading
        language: Language code ('en' or 'nl')
    """
    # Get rune and trigram data
    rune1_name = RUNES[rune1_num]["name"]
    rune2_name = RUNES[rune2_num]["name"]
    rune1_symbol = RUNES[rune1_num]["symbol"]
    rune2_symbol = RUNES[rune2_num]["symbol"]
    
    lower_trigram = get_trigram_from_rune(rune1_num)
    upper_trigram = get_trigram_from_rune(rune2_num)
    
    hexagram_num = get_hexagram_from_trigrams(lower_trigram, upper_trigram)
    
    # Read files
    rune1_content = read_rune_file(rune1_num)
    rune2_content = read_rune_file(rune2_num)
    hexagram_content = read_hexagram_file(hexagram_num)
    
    hex_title = extract_hexagram_title(hexagram_content)
    
    # Extract interpretive data
    rune1_lens = extract_interpretive_lens(rune1_content)
    rune2_lens = extract_interpretive_lens(rune2_content)
    rune1_oracle = extract_oracle_interpretation(rune1_content)
    rune2_oracle = extract_oracle_interpretation(rune2_content)
    
    data = {
        "user_name": user_name,
        "rune1": {
            "number": rune1_num,
            "name": rune1_name,
            "symbol": rune1_symbol,
            "content": rune1_content,
            "oracle": rune1_oracle,
            "lens": rune1_lens,
        },
        "rune2": {
            "number": rune2_num,
            "name": rune2_name,
            "symbol": rune2_symbol,
            "content": rune2_content,
            "oracle": rune2_oracle,
            "lens": rune2_lens,
        },
        "lower_trigram": lower_trigram,
        "upper_trigram": upper_trigram,
        "hexagram": {
            "number": hexagram_num,
            "title": hex_title,
            "content": hexagram_content,
        }
    }
    
    # Translate content to Dutch if requested
    if language == 'nl':
        api_key = os.getenv('GOOGLE_API_KEY')
        if api_key:
            # Translate rune content
            data["rune1"]["content"] = translate_text(rune1_content, api_key)
            data["rune2"]["content"] = translate_text(rune2_content, api_key)
            data["hexagram"]["content"] = translate_text(hexagram_content, api_key)
            
            # Translate extracted interpretations
            if rune1_oracle:
                data["rune1"]["oracle"] = translate_text(rune1_oracle, api_key)
            if rune2_oracle:
                data["rune2"]["oracle"] = translate_text(rune2_oracle, api_key)
            if rune1_lens:
                data["rune1"]["lens"] = translate_text(rune1_lens, api_key)
            if rune2_lens:
                data["rune2"]["lens"] = translate_text(rune2_lens, api_key)
            
            # Translate hexagram title
            data["hexagram"]["title"] = translate_text(hex_title, api_key)
    
    # Generate template narrative interpretation (always available as fallback)
    data["narrative_interpretation"] = generate_narrative_interpretation(data)
    
    # AI interpretation will be added separately when requested
    data["ai_interpretation"] = None
    
    return data


