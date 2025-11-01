# Deploying The Oracle to the Web

## 🌐 Quick Deployment Guide

Your Oracle app is ready to deploy! Here's how to get it online in minutes.

---

## ✅ Option 1: Streamlit Community Cloud (Recommended - FREE)

### Why Streamlit Cloud?
- ✅ **Completely FREE**
- ✅ **Takes 10 minutes**
- ✅ **No server management**
- ✅ **Automatic updates** when you push to GitHub
- ✅ **HTTPS included**
- ✅ **Perfect for this app**

### Step-by-Step Instructions

#### 1. Prepare Your Repository

**A. Create a GitHub Account** (if you don't have one)
- Go to https://github.com
- Sign up (free)

**B. Create a New Repository**
- Click "New Repository"
- Name it something like "oracle-reading-app"
- Make it **PUBLIC** (required for free tier)
- Don't initialize with README (you have files already)

**C. Upload Your Files**

You need to upload these files/folders to GitHub:

**Required Files:**
```
oracle_app.py
oracle_core.py
oracle_ai.py
oracle_markdown.py
requirements.txt
.gitignore
Runes/ (folder with all 24 rune files)
I Ching/ (folder with all 64 hexagram files)
Casting (optional, documentation)
```

**How to Upload:**
1. In your GitHub repo, click "Add file" → "Upload files"
2. Drag and drop all the files/folders listed above
3. Write commit message: "Initial commit"
4. Click "Commit changes"

**Important:** The `.gitignore` file will prevent your API key from being uploaded (security!)

#### 2. Deploy to Streamlit Cloud

**A. Sign Up**
- Go to https://share.streamlit.io/ (or https://streamlit.io/cloud)
- Click "Sign up" or "Continue with GitHub"
- Authorize Streamlit to access your GitHub

**B. Create New App**
- Click "New app"
- **Repository:** Select your oracle-reading-app repository
- **Branch:** main (or master)
- **Main file path:** oracle_app.py
- **App URL:** Choose a name like `oracle-readings` (will be `oracle-readings.streamlit.app`)

**C. Add Your API Key (IMPORTANT!)**
- Before clicking "Deploy", click "Advanced settings"
- Under "Secrets", paste this:
  ```toml
  GOOGLE_API_KEY = "AIzaSyDlnxu63hGJkagTzkwjWayr67TzaYln0ww"
  ```
- This keeps your API key secure and private

**D. Deploy!**
- Click "Deploy!"
- Wait 2-3 minutes while it installs dependencies
- Your app will be live at: `https://[your-app-name].streamlit.app`

### 3. Share Your Website!

Your Oracle is now live! Share the URL with anyone:
```
https://oracle-readings.streamlit.app
```

Anyone can:
- ✅ Generate readings
- ✅ Get AI interpretations
- ✅ Download markdown reports
- ✅ Use on any device (mobile, tablet, desktop)

---

## 🔄 Updating Your Live Website

When you make changes to your code:

1. **Edit files locally** (on your computer)
2. **Upload to GitHub:**
   - Go to your GitHub repository
   - Click "Add file" → "Upload files"
   - Upload the updated files
   - Commit changes
3. **Automatic deployment:**
   - Streamlit Cloud detects the changes
   - Rebuilds your app automatically
   - Takes 1-2 minutes
   - Your site is updated!

---

## 🔒 Security Best Practices

### ✅ What I've Already Done For You

1. **API Key Protection:**
   - Code now reads API key from Streamlit secrets
   - `.gitignore` prevents secrets from going to GitHub
   - API key stays private

2. **Safe for Public Use:**
   - No sensitive data in code
   - API key hidden from users
   - App works for everyone without exposing credentials

### ⚠️ Things to Know

**API Usage:**
- Your Gemini API key has a free tier (generous limits)
- If many people use your site, you might hit rate limits
- Monitor usage at: https://console.cloud.google.com/

**Cost:**
- Gemini 2.5 Flash is very cheap (~$0.0005 per reading)
- Free tier: thousands of readings per month
- You can set spending limits in Google Cloud Console

---

## 🎨 Option 2: Custom Domain (Optional)

Streamlit Cloud gives you: `your-app.streamlit.app`

**Want your own domain?** (e.g., `theoracle.com`)

1. **Buy a domain** (Namecheap, Google Domains, etc.)
2. **In Streamlit Cloud:**
   - Go to App settings
   - Click "Custom domain"
   - Follow instructions to add CNAME record
3. **Or upgrade to Streamlit Teams** (paid) for more features

---

## 💻 Option 3: Other Hosting Platforms

If you prefer alternatives to Streamlit Cloud:

### Railway.app (Easy, Paid)
- Connect GitHub repo
- Automatic deployments
- $5-10/month
- https://railway.app

### Heroku (Traditional, Paid)
- Requires `Procfile` configuration
- $7/month minimum
- https://heroku.com

### Your Own Server (Advanced)
```bash
# SSH into your server
git clone https://github.com/yourusername/oracle-reading-app
cd oracle-reading-app
pip install -r requirements.txt
streamlit run oracle_app.py --server.port 80
```

---

## 📱 Mobile Optimization

Your Streamlit app is **already mobile-friendly!**

Users can access on:
- ✅ iPhone/Android
- ✅ Tablets
- ✅ Desktop
- ✅ Any modern browser

The responsive design adapts automatically!

---

## 🔍 Monitoring Your Live Site

### View Analytics (Streamlit Cloud)
- Log in to https://share.streamlit.io/
- Click your app
- See visitor stats, uptime, logs

### Check API Usage (Google Cloud)
- Go to https://console.cloud.google.com/
- Navigate to "APIs & Services" → "Dashboard"
- View Gemini API usage and costs

---

## 🐛 Troubleshooting Deployment

### "ModuleNotFoundError"
**Problem:** Missing package in requirements.txt
**Solution:** Make sure `requirements.txt` includes:
```
streamlit
reportlab
google-generativeai
```

### "API Key Error"
**Problem:** Secrets not configured
**Solution:** 
- Go to App settings in Streamlit Cloud
- Add secret: `GOOGLE_API_KEY = "your-key-here"`
- Reboot app

### "File Not Found" for Runes/I Ching
**Problem:** Folders not uploaded to GitHub
**Solution:**
- Make sure `Runes/` and `I Ching/` folders are in your repository
- Each should contain all the .md files

### App is Slow
**Problem:** Cold start or heavy traffic
**Solution:**
- First visit after inactivity takes 10-15 seconds (normal)
- Streamlit Cloud spins down inactive apps
- Upgrade to Streamlit Teams for always-on apps

---

## ✨ Success Checklist

Before going live, verify:

- [ ] All files uploaded to GitHub
- [ ] Runes/ folder has 24 .md files
- [ ] I Ching/ folder has 64 .md files
- [ ] requirements.txt is present
- [ ] API key added to Streamlit secrets
- [ ] App deployed successfully
- [ ] Test a reading generation
- [ ] Test markdown download
- [ ] Test on mobile device
- [ ] Share URL with friends!

---

## 🎉 You're Live!

Your Oracle reading system is now accessible to anyone, anywhere in the world!

**Your live URL:**
```
https://[your-app-name].streamlit.app
```

**What users can do:**
- Generate personalized oracle readings
- Get unique AI interpretations
- Download beautiful markdown reports
- Access from any device
- No installation required

**Next steps:**
- Share on social media
- Add to your personal website
- Tell friends and family
- Monitor usage and feedback

---

## 📞 Support

**Streamlit Documentation:**
https://docs.streamlit.io/streamlit-community-cloud

**Deployment Issues:**
https://discuss.streamlit.io/

**This Project:**
All code is ready to deploy as-is. Just follow the steps above!

---

**Happy Deploying! 🚀🔮**

Your Oracle will be bringing wisdom to the world in just a few clicks!

