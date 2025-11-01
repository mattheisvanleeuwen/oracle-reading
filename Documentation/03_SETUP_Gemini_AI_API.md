# Oracle with Google Gemini AI

## ✅ Setup Complete!

The Oracle has been configured to use **Google Gemini Pro** for AI-powered interpretations instead of OpenAI.

## 🎉 What This Means

### Advantages of Gemini

1. **Cost Effective:**
   - **Free tier** with generous rate limits (60 requests/minute)
   - Paid tier: ~$0.001-$0.002 per reading (vs $0.02-$0.05 for OpenAI)
   - 10-20x cheaper than GPT-4!

2. **High Quality:**
   - Gemini Pro provides excellent, nuanced interpretations
   - Great at understanding context and symbolism
   - Natural, flowing language

3. **Easy Setup:**
   - No credit card required for free tier
   - Simple API key generation
   - Your key is already configured in the app!

## 🔑 Your API Key

Your Google API key has been pre-configured in the app:
```
AIzaSyDlnxu63hGJkagTzkwjWayr67TzaYln0ww
```

**⚠️ Security Note:** The key is embedded in the code for convenience. For production use, you should:
- Set it as an environment variable instead
- Don't share your code publicly with the key in it

## 🚀 Quick Start

### 1. Install Dependencies

Run the installation script:
```bash
.\install_dependencies.bat
```

Or manually:
```bash
pip install streamlit reportlab google-generativeai
```

### 2. Launch the App

```bash
python -m streamlit run oracle_app.py
```

### 3. Generate AI Reading

1. App will open in your browser
2. ✅ API key is already configured (sidebar will show green checkmark)
3. ☑️ "Use AI-Powered Interpretation" is checked by default
4. Enter your name
5. Select your runes
6. (Optional) Add your question in sidebar
7. Click "Generate Reading"
8. Wait ~5-10 seconds
9. **Get unique AI interpretation!** 🎉

## 💰 Cost Comparison

| Provider | Free Tier | Paid Cost/Reading | Quality |
|----------|-----------|-------------------|---------|
| **Gemini Pro** | ✅ Yes | $0.001-$0.002 | Excellent |
| OpenAI GPT-4o | ❌ No | $0.02-$0.05 | Excellent |

**Savings:** 10-20x cheaper with Gemini!

## 🎯 API Usage

### Free Tier Limits
- **60 requests per minute**
- **Daily quota:** Thousands of requests
- **Perfect for personal use**

### Paid Tier (Optional)
- Only if you exceed free tier
- Enable in Google Cloud Console
- Pay-as-you-go pricing
- Still much cheaper than OpenAI

## 🔧 How It Works

1. **User Input:**
   - Name: Sarah
   - Rune 1: Fehu (wealth/cattle)
   - Rune 2: Kenaz (torch/skill)
   - Result: Hexagram 55 (Abundance)
   - Question: "How should I approach my career?"

2. **Sent to Gemini:**
   - Complete hexagram text
   - Both rune meanings
   - Trigram associations
   - User's question

3. **Gemini Creates:**
   - Unique 500-700 word interpretation
   - Weaves together all elements
   - Addresses user by name
   - Incorporates their question
   - Provides practical guidance

4. **You Receive:**
   - Original, personalized reading
   - Never the same twice
   - Deep symbolic connections
   - Actionable advice

## 📊 Example Output

**Template Interpretation (Free):**
> "At the core lies Fehu, which manifests as Thunder..."

**Gemini AI Interpretation (Free or $0.001):**
> "Sarah, you stand at the ZENITH of your powers, and this isn't mere chance—it's the culmination of Fehu's energy, the moveable wealth that's been rumbling beneath your foundation like Thunder. Your cattle are in motion, your resources circulating. Regarding your career decision: Kenaz now lights your path with the torch of applied skill..."

Much more personalized and insightful!

## 🛡️ Privacy & Security

### Your API Key
- Currently embedded in the app for convenience
- Only used to call Google's API
- Never shared elsewhere

### Your Readings
- Sent to Google Gemini API for interpretation
- Google's privacy policy applies
- Not used to train models (API usage)
- Can be deleted from your Google account

### Best Practices
1. **For production:** Use environment variable instead:
   ```powershell
   $env:GOOGLE_API_KEY = "your-key-here"
   ```
2. **Don't share** your API key publicly
3. **Monitor usage** at Google AI Studio

## 🎨 Features

✅ AI-powered unique interpretations
✅ Pre-configured with your API key
✅ Free tier (no credit card needed)
✅ 10-20x cheaper than OpenAI
✅ Optional user question field
✅ Template fallback always available
✅ PDF export with AI interpretation
✅ Beautiful web interface
✅ Sidebar configuration

## 🔄 Switching Back to OpenAI (If Needed)

If you ever want to use OpenAI instead:
1. Change `requirements.txt`: `google-generativeai` → `openai`
2. Get OpenAI API key
3. Update `oracle_ai.py` to use OpenAI
4. Update `oracle_app.py` environment variable checks

But Gemini is recommended for cost and quality!

## 📖 Documentation

- **`AI_INTERPRETATION_GUIDE.md`** - General AI features (mostly still applies)
- **`AI_IMPLEMENTATION_SUMMARY.md`** - Technical details
- **`GEMINI_SETUP.md`** - This file

## 🎯 Ready to Use!

Everything is configured and ready. Just:

1. Run `.\install_dependencies.bat` (or pip install manually)
2. Run `python -m streamlit run oracle_app.py`
3. Generate readings with AI interpretations!

**No additional setup needed** - your API key is already configured! 🚀✨

---

**Enjoy free (or very cheap) AI-powered oracle readings with Google Gemini!** 🔮


