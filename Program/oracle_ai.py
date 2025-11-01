"""
Oracle AI Interpretation - Google Gemini-powered dynamic interpretations
"""

import os
import google.generativeai as genai


def generate_ai_interpretation(reading_data, api_key=None, user_question=None, language='en'):
    """
    Generate a unique, AI-powered interpretation using Google Gemini.
    
    Args:
        reading_data: Dictionary with reading information
        api_key: Google API key (optional, will use env var if not provided)
        user_question: Optional user's specific question for the reading
        language: Language for interpretation ('en' for English, 'nl' for Dutch)
    
    Returns:
        String containing the AI-generated interpretation
    """
    # Get API key from parameter, environment, or return error
    if api_key is None:
        api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        return """<i>AI interpretation requires a Google API key. Please set your GOOGLE_API_KEY environment variable or enter it in the app settings.</i>
        
<b>To get an API key:</b>
1. Visit https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your environment or enter it in the app

For now, you can use the template-based interpretation above."""
    
    # Configure Gemini
    try:
        genai.configure(api_key=api_key)
        # Use Gemini 2.5 Flash - stable, fast, excellent quality
        model = genai.GenerativeModel('models/gemini-2.5-flash')
    except Exception as e:
        return f"<i>Error initializing Gemini: {str(e)}</i>"
    
    # Extract reading information
    hex_num = reading_data['hexagram']['number']
    hex_title = reading_data['hexagram']['title']
    hex_content = reading_data['hexagram']['content']
    
    rune1_name = reading_data['rune1']['name']
    rune1_symbol = reading_data['rune1']['symbol']
    rune1_oracle = reading_data['rune1']['oracle']
    rune1_lens = reading_data['rune1']['lens']
    
    rune2_name = reading_data['rune2']['name']
    rune2_symbol = reading_data['rune2']['symbol']
    rune2_oracle = reading_data['rune2']['oracle']
    rune2_lens = reading_data['rune2']['lens']
    
    lower_trigram = reading_data['lower_trigram']
    upper_trigram = reading_data['upper_trigram']
    
    user_name = reading_data.get('user_name', 'the seeker')
    
    # Build the prompt for Gemini
    prompt = f"""You are an expert oracle reader who specializes in combining the wisdom of the Elder Futhark runes with the I Ching hexagrams. Your interpretations are deep, insightful, poetic, and practical. You weave together ancient wisdom with modern understanding.

Generate a comprehensive oracle reading interpretation for {user_name}.

**THE HEXAGRAM:**
Hexagram {hex_num}: {hex_title}

{hex_content}

**RUNE 1 (THE ROOT - Lower Trigram):**
{rune1_name} {rune1_symbol} → {lower_trigram['symbol']} {lower_trigram['name']} ({lower_trigram['chinese']})

Rune Meaning: {rune1_oracle}

How it influences the trigram: {rune1_lens if rune1_lens else 'This rune brings its essential qualities to the ' + lower_trigram['name'] + ' trigram.'}

**RUNE 2 (THE CONTEXT - Upper Trigram):**
{rune2_name} {rune2_symbol} → {upper_trigram['symbol']} {upper_trigram['name']} ({upper_trigram['chinese']})

Rune Meaning: {rune2_oracle}

How it influences the trigram: {rune2_lens if rune2_lens else 'This rune brings its essential qualities to the ' + upper_trigram['name'] + ' trigram.'}
"""

    if user_question:
        prompt += f"\n\n**THE SEEKER'S QUESTION:**\n{user_question}\n"
    
    # Language-specific instructions
    language_instructions = {
        'en': f"""
Create a flowing, narrative interpretation that weaves all of these elements together. Structure it as:

1. **Opening:** Set the scene with the hexagram and address {user_name} directly
2. **The Inner Foundation:** Explain how {rune1_name} as {lower_trigram['name']} is the WHY (be specific about what {rune1_name} represents - for example, if {rune1_name} means wealth or cattle, explain how that manifests in this situation)
3. **The Outer Strategy:** Explain how {rune2_name} as {upper_trigram['name']} is the HOW (be specific about what {rune2_name} represents - use its literal meaning to illuminate the path)
4. **Integration:** Show how these forces work together and provide practical, actionable guidance

Make it personal, insightful, and actionable. Use poetic language but remain grounded and practical. The interpretation should feel like wisdom from an ancient oracle speaking directly to {user_name} about their unique situation. Draw specific connections between the rune meanings and the hexagram - don't just list them separately, show how they interact and inform each other.

Write approximately 500-700 words in a flowing narrative style IN ENGLISH.""",
        'nl': f"""
Creëer een vloeiende, narratieve interpretatie die al deze elementen met elkaar verweft. Structureer het als volgt:

1. **Opening:** Schets de situatie met het hexagram en spreek {user_name} direct aan
2. **Het Innerlijke Fundament:** Leg uit hoe {rune1_name} als {lower_trigram['name']} het WAAROM is (wees specifiek over wat {rune1_name} vertegenwoordigt - bijvoorbeeld, als {rune1_name} rijkdom of vee betekent, leg uit hoe dat zich manifesteert in deze situatie)
3. **De Uiterlijke Strategie:** Leg uit hoe {rune2_name} als {upper_trigram['name']} de HOE is (wees specifiek over wat {rune2_name} vertegenwoordigt - gebruik de letterlijke betekenis om het pad te verlichten)
4. **Integratie:** Laat zien hoe deze krachten samenwerken en bied praktische, bruikbare begeleiding

Maak het persoonlijk, inzichtelijk en bruikbaar. Gebruik poëtische taal maar blijf gegrond en praktisch. De interpretatie moet voelen als wijsheid van een oud orakel dat direct tot {user_name} spreekt over hun unieke situatie. Maak specifieke verbindingen tussen de runen betekenissen en het hexagram - lijst ze niet alleen apart op, maar laat zien hoe ze interacteren en elkaar informeren.

Schrijf ongeveer 500-700 woorden in een vloeiende verhalende stijl VOLLEDIG IN HET NEDERLANDS."""
    }
    
    prompt += language_instructions.get(language, language_instructions['en'])
    
    # Call Gemini API
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.8,  # Creative but not too random
                max_output_tokens=8000,  # Increased significantly to avoid cutoff
            )
        )
        
        interpretation = response.text
        
        # Return interpretation without attribution
        return interpretation
        
    except Exception as e:
        return f"""<i>Error generating AI interpretation: {str(e)}</i>

<b>Please check:</b>
- Your API key is valid
- You have quota available in your Google Cloud account
- Your internet connection is working

Using template interpretation as fallback:

{reading_data.get('narrative_interpretation', 'Template interpretation not available.')}"""


def estimate_cost():
    """Return estimated cost per AI interpretation."""
    return "Free (with rate limits) or ~$0.001 - $0.002 per reading with paid tier"


def get_api_key_instructions():
    """Return instructions for getting a Google API key."""
    return """
## How to Get Your Google API Key

1. **Visit Google AI Studio:** https://makersuite.google.com/app/apikey
2. **Sign In** with your Google account
3. **Create API Key:**
   - Click "Create API Key"
   - Select a Google Cloud project (or create new one)
   - Copy the key immediately
4. **Enable Billing (Optional):**
   - Free tier includes generous rate limits
   - For higher volume, enable billing in Google Cloud Console
   - Paid tier is very inexpensive (~$0.001 per reading)

## How to Use the API Key

**Option 1: Set Environment Variable (Recommended)**
```
# Windows PowerShell:
$env:GOOGLE_API_KEY="your-key-here"

# Or add permanently via System Properties > Environment Variables
```

**Option 2: Enter in App**
Just paste your key in the sidebar when you run the app.

## Cost Information
- **Free Tier:** 60 requests per minute, generous daily quota
- **Paid Tier:** ~$0.001 to $0.002 per reading (very affordable!)
- **No credit card required** for free tier
- Much cheaper than OpenAI while still high quality
"""
