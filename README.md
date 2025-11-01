# The Oracle - Insight

A mystical divination system combining Elder Futhark runes with I Ching hexagrams, powered by AI interpretation.

## Quick Start

### Installation
```batch
install_dependencies.bat
```

### Run the Application
```batch
python -m streamlit run Program\oracle_app.py
```

## Project Structure

```
The Oracle - Insight/
├── Program/                    # All Python application files
│   ├── oracle_app.py          # Main Streamlit web application
│   ├── oracle_core.py         # Core reading logic
│   ├── oracle_ai.py           # AI interpretation (Gemini)
│   ├── oracle_markdown.py     # Markdown generation
│   ├── oracle_pdf.py          # PDF generation
│   ├── oracle_digital_draw.py # Digital card drawing interface
│   ├── translations.py        # Multi-language support
│   └── backup_project.py      # Backup system
│
├── Documentation/              # All guides and documentation
│   ├── 01_README_Application_Overview.md
│   ├── 02_GUIDE_Deployment.md
│   ├── 03_SETUP_Gemini_AI_API.md
│   ├── 04_GUIDE_AI_Interpretation.md
│   ├── 05_SUMMARY_AI_Implementation.md
│   ├── 06_FEATURE_Digital_Draw.md
│   ├── 07_FEATURE_Dutch_Language.md
│   ├── 08_GUIDE_Wix_Integration.md
│   └── 09_CHANGELOG_Updates.md
│
├── I Ching/                    # 64 I Ching hexagram files
├── Runes/                      # 24 Elder Futhark rune files
├── Casting                     # Physical casting reference
├── Answers/                    # Generated readings saved here
├── Backups/                    # Versioned project backups
├── .streamlit/                 # Streamlit configuration
├── requirements.txt            # Python dependencies
└── install_dependencies.bat    # Dependency installer

```

## Features

- **Rune-Hexagram System**: Unique divination combining Norse and Chinese wisdom
- **AI Interpretation**: Powered by Google Gemini for personalized insights
- **Multi-language**: English and Dutch support
- **Digital Draw**: Interactive card selection interface
- **PDF Export**: Save readings as beautiful PDFs
- **Backup System**: Version-controlled backups with restore instructions

## Backup System

Create a backup anytime by saying "backup now" or running:
```batch
python Program\backup_project.py
```

Backups are stored in `Backups/` with version numbers and timestamps.

## Documentation

All documentation is organized in the `Documentation/` folder:
- Start with `01_README_Application_Overview.md` for detailed app info
- See `02_GUIDE_Deployment.md` for deployment instructions
- Check `03_SETUP_Gemini_AI_API.md` for AI setup

## Support

For questions or issues, refer to the documentation files in the `Documentation/` folder.

---
*The Oracle - Insight: Where Ancient Wisdom Meets Modern AI*

