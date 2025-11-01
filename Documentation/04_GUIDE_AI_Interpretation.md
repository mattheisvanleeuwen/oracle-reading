# AI-Powered Oracle Interpretations Guide

## 🤖 What is AI Interpretation?

The Oracle now features **AI-powered interpretations** using OpenAI's GPT-4o model. This means each reading is completely unique, personalized, and tailored to your specific rune combination, hexagram, and optional question.

## ✨ How It Works

### Traditional Template vs. AI Interpretation

**Template Interpretation (Always Available):**
- Uses pre-written text patterns
- Combines rune and hexagram meanings using fixed structures
- Fast and free
- Consistent format

**AI Interpretation (Optional, Enhanced):**
- **Truly unique** - never the same twice
- Deep analysis of how runes interact with hexagram
- Natural, flowing narrative style
- Can incorporate your specific question
- Poetic yet practical guidance
- Costs ~$0.02-$0.05 per reading

### What Makes AI Interpretation Special

The AI doesn't just combine text templates. It:

1. **Understands context:** Knows how "Fehu = cattle/wealth" specifically impacts "Hexagram 55 = Abundance"
2. **Finds connections:** Sees subtle relationships between rune energies and hexagram situations
3. **Personalizes:** Incorporates your name and question naturally
4. **Adapts tone:** Balances mystical wisdom with practical advice
5. **Creates narrative flow:** Tells a cohesive story, not bullet points

### Example Comparison

**Template Interpretation:**
> "Your reading reveals the landscape of ZENITH (ABUNDANCE). At the core lies Fehu, which manifests as Thunder in your inner world. Fehu is the rune of primal, creative potential..."

**AI Interpretation:**
> "Sarah, you stand at the peak moment of ZENITH, where the longest day meets its fullness before the inevitable turn toward winter. But this is not a passive abundance—it is rooted in Fehu, the moveable wealth of cattle, the dynamic energy of resources in motion. Your Thunder foundation shakes not with chaos, but with the productive rumble of generative force..."

The AI weaves specific details, uses metaphor, and creates a unique voice.

## 🔑 Getting Your OpenAI API Key

### Step 1: Create Account
1. Visit https://platform.openai.com/api-keys
2. Sign up or log in with your existing account
3. You'll need to verify your email

### Step 2: Add Billing
1. Go to https://platform.openai.com/account/billing
2. Add a payment method
3. Add credits (minimum $5 recommended)
   - $5 = ~100-250 readings
   - $10 = ~200-500 readings

### Step 3: Create API Key
1. Navigate to API Keys section
2. Click "Create new secret key"
3. Give it a name (e.g., "Oracle Reading App")
4. **IMPORTANT:** Copy the key immediately - you can't see it again!
5. Keep it secure - don't share it publicly

### Step 4: Use in App

**Method 1: Environment Variable (Recommended)**

Windows PowerShell:
```powershell
# Set for current session:
$env:OPENAI_API_KEY = "sk-your-key-here"

# Set permanently:
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'sk-your-key-here', 'User')
```

**Method 2: Enter in App Sidebar**
- Just paste your key in the sidebar when running the app
- It's stored only for your session (not saved to disk)

## 💰 Cost & Usage

### Pricing
- **Per Reading:** ~$0.02 to $0.05
- **Model:** GPT-4o (optimized for cost/quality)
- **Tokens:** ~1,000-2,500 per interpretation
- **You only pay for what you use**

### Cost Examples
- **$5 credit:** ~100-250 AI readings
- **$10 credit:** ~200-500 AI readings
- **$20 credit:** ~400-1,000 AI readings

### When You're Charged
- Only when AI interpretation is generated
- NOT charged for:
  - Template interpretations
  - Viewing readings
  - Downloading PDFs
  - Using the app without AI enabled

## 🎯 Using AI Interpretation

### In the App

1. **Launch the app:**
   ```bash
   python -m streamlit run oracle_app.py
   ```

2. **Configure in Sidebar:**
   - If you set environment variable: AI will be ready automatically
   - Otherwise: Paste your API key in the sidebar
   - Check "Use AI-Powered Interpretation"

3. **Optional - Add Your Question:**
   - Enter a specific question for more targeted guidance
   - Example: "How should I navigate my career transition?"
   - The AI will incorporate your question into the interpretation

4. **Generate Reading:**
   - Enter your name
   - Select your two runes
   - Click "Generate Reading"
   - Wait 10-15 seconds for AI to create your interpretation

5. **View Results:**
   - AI interpretation appears in the 🔮 Interpretation section
   - You can also expand to see the template interpretation for comparison

### In the PDF

- AI interpretation (if generated) is automatically included in the PDF
- Replaces the template interpretation
- Exported with proper formatting

## 🛡️ Privacy & Security

### Your API Key
- Stored only in memory during your session
- Never written to disk
- Not shared or transmitted anywhere except OpenAI

### Your Readings
- Sent to OpenAI API for interpretation
- OpenAI's privacy policy applies
- Not used to train models (with API use)
- Not stored by OpenAI after 30 days

### Best Practices
1. **Don't share your API key** in screenshots or files
2. **Use environment variables** for better security
3. **Monitor your usage** at https://platform.openai.com/usage
4. **Set spending limits** in your OpenAI account

## 🔧 Troubleshooting

### "No API key found"
- Make sure you've entered it in the sidebar OR
- Set the environment variable correctly OR
- Check spelling: `OPENAI_API_KEY`

### "Error generating AI interpretation"
**Check:**
- Is your API key valid?
- Do you have credits in your account?
- Is your internet connection working?
- Did you exceed rate limits? (unlikely for personal use)

**Solution:**
- Template interpretation is automatically used as fallback
- Check your OpenAI account at https://platform.openai.com

### "Interpretation takes too long"
- AI generation takes 10-15 seconds (normal)
- Complex questions may take slightly longer
- If it times out, try again

### "Cost concerns"
- Each reading costs $0.02-$0.05
- Set spending limits in OpenAI dashboard
- Use template interpretation for free readings
- AI is optional - you control when it's used

## 📊 Comparison: Template vs. AI

| Feature | Template | AI (GPT-4o) |
|---------|----------|-------------|
| Cost | Free | ~$0.02-$0.05 |
| Speed | Instant | 10-15 sec |
| Uniqueness | Consistent | Every reading unique |
| Personalization | Name only | Name + question + context |
| Depth | Good | Excellent |
| Metaphor/Poetry | Limited | Rich |
| Specific connections | Basic | Deep insights |
| Understanding | Pattern-based | Conceptual |
| Best for | Quick readings | Deep guidance |

## 🌟 Tips for Best AI Interpretations

1. **Provide a specific question** in the sidebar for more targeted guidance
2. **Be patient** - AI needs 10-15 seconds to craft a unique reading
3. **Compare both** - Look at template and AI interpretations together
4. **Save meaningful readings** - Download the PDF for your records
5. **Reflect on the narrative** - AI interpretations tell a story, not just facts

## 🔄 Future Enhancements

Potential upcoming features:
- Choice of AI models (Claude, Gemini, etc.)
- Adjustable interpretation length
- Different tone options (scholarly, poetic, practical)
- Multi-language support
- Conversation mode (ask follow-up questions)

## 📞 Support

**For OpenAI API Issues:**
- https://help.openai.com

**For App Issues:**
- Check the README_WEB_APP.md
- Ensure all dependencies are installed
- Verify Python version (3.11+)

---

**Remember:** AI interpretation is an enhancement, not a requirement. The Oracle works beautifully with template interpretations, and you can choose what works best for each reading! 🔮✨

