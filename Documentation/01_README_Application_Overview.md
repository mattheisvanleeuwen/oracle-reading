# The Oracle - Web Interface Guide

## 🔮 Overview

The Oracle is a divination system that combines the Elder Futhark runes with the I Ching hexagrams to provide deep insights into your situation. This web interface provides a beautiful, modern way to generate readings.

**NEW:** ✨ **AI-Powered Interpretations** using OpenAI GPT-4o! Get unique, personalized readings tailored to your specific question and situation. See `AI_INTERPRETATION_GUIDE.md` for details.

## 🚀 Quick Start

### Running the Web Application

1. **Install Requirements** (first time only):
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the Web App**:
   ```bash
   streamlit run oracle_app.py
   ```

3. **Open in Browser**:
   - The app will automatically open in your default browser
   - If not, navigate to: `http://localhost:8501`

## 📖 How to Use

### Step 1: Enter Your Name
- Enter your name in the text field at the top
- Your name will appear in the reading and in the filename

### Step 2: Select Your Runes

**Rune 1 (The Root):**
- Determines the **Lower Trigram** (inner foundation)
- Choose from the dropdown menu
- Represents the "why" of your situation

**Rune 2 (The Context):**
- Determines the **Upper Trigram** (outer strategy)
- Choose from the dropdown menu
- Represents the "how-to" of your situation

### Step 3: Generate Reading
- Click the "✨ Generate Reading ✨" button
- The Oracle will combine your runes to create a hexagram

### Step 4: Explore Your Results

**Summary Card:**
- Shows the hexagram number and title
- Displays the trigram symbols
- Shows how your runes flavor each trigram

**Expandable Sections:**
- **📜 Literal Reading**: Full text of both runes and the hexagram
- **🔮 Interpretation**: The 4-step interpretive framework combining all elements

### Step 5: Download or Save

**PDF Report:**
- Click "📄 Download PDF Report" to get a beautifully formatted 2-page PDF
- PDF includes:
  - Large, emphasized symbols
  - Your name prominently displayed
  - Professional formatting
  - Complete reading and interpretation

**Save to Answers Folder:**
- Click "💾 Save to Answers Folder" to save markdown files
- Files are saved with your name and timestamp in the filename
- Format: `reading_YourName_YYYYMMDD_HHMMSS.md`

## 🎨 Features

### Visual Design
- Modern, mystical dark theme
- Gold and bronze color scheme
- Large, readable symbols (☳, ☷, ☶, etc.)
- Responsive layout
- Custom styling for an immersive experience

### PDF Reports
- Professional 2-page layout
- Page 1: The Literal Reading
  - Your name prominently displayed
  - Large trigram symbols
  - Two-column rune display
  - Complete hexagram text
- Page 2: The Interpretation
  - 4-step interpretive framework
  - Emphasized symbols throughout
  - Quick reference box

### Personalization
- Your name appears in:
  - The web interface results
  - PDF report headers
  - Saved file names
  - All generated content

## 📁 File Organization

```
The Oracle - Insight/
├── oracle_app.py          # Streamlit web interface
├── oracle_core.py         # Core logic and mappings
├── oracle_pdf.py          # PDF generation
├── oracle.py              # CLI version (still available)
├── requirements.txt       # Python dependencies
├── Runes/                 # 24 rune markdown files
├── I Ching/               # 64 hexagram markdown files
└── Answers/               # Generated readings saved here
```

## 🎯 The Oracle System

### The Rune-to-Trigram Mapping

The system uses the **Aett Stack** theory:
- 24 runes map to 8 trigrams based on position (1-8) across 3 Aetts
- Each trigram represents a fundamental force
- Each rune provides a specific "flavor" to that trigram

### The 4-Step Interpretive Framework

1. **The Landscape**: The hexagram provides the objective situation
2. **Inner Dimension**: Rune 1 → Lower Trigram (the "why")
3. **External Strategy**: Rune 2 → Upper Trigram (the "how-to")
4. **Synthesis**: Integration of all three elements

## 💡 Tips for Best Results

1. **Take Your Time**: Reflect on your question before selecting runes
2. **Read Both Sections**: The literal reading and interpretation complement each other
3. **Keep Your PDFs**: Build a personal archive of readings
4. **Use Your Name**: Personalization makes readings more meaningful
5. **Explore the Expandable Sections**: Don't miss the detailed content

## 🔧 Troubleshooting

**App won't start?**
- Make sure you've run `pip install -r requirements.txt`
- Check that you're in the correct directory

**Symbols not displaying?**
- Your browser should support Unicode characters
- Try a modern browser (Chrome, Firefox, Edge)

**PDF download not working?**
- Check your browser's download settings
- Ensure pop-ups aren't blocked

**Files not saving to Answers folder?**
- The folder will be created automatically if it doesn't exist
- Check file permissions

## 🆚 CLI vs Web Interface

**CLI (`oracle.py`):**
- Terminal-based
- Interactive prompts
- Saves markdown files only
- Good for quick readings

**Web Interface (`oracle_app.py`):**
- Beautiful visual interface
- Dropdown selectors
- PDF export with professional formatting
- Expandable sections for easy reading
- Personalized with your name
- Better for detailed, saved readings

Both versions work independently and can be used based on your preference!

## 🌟 Enjoy Your Readings!

The Oracle is now ready to provide guidance. May your readings bring clarity and insight!


