# Integrating The Oracle into Your Wix Website

## 🎯 Overview

You **cannot** run Python/Streamlit directly on Wix, but you **can** embed your Oracle app that's hosted elsewhere (like Streamlit Cloud) into your Wix website using an iframe.

**Result:** Visitors to your Wix site can use the Oracle without leaving your website!

---

## 📋 Prerequisites

Before integrating with Wix, you need:

1. ✅ **Deployed Oracle App** - Host on Streamlit Cloud (FREE)
   - Follow `DEPLOYMENT_GUIDE.md` first
   - Get your live URL: `https://your-oracle-app.streamlit.app`

2. ✅ **Wix Website** - Any Wix plan works
   - Free or paid plan
   - Access to Wix Editor

---

## 🚀 Integration Method 1: Full Page Embed (Recommended)

This creates a dedicated Oracle page on your Wix site.

### Step 1: Deploy to Streamlit Cloud

```bash
1. Upload code to GitHub
2. Deploy to Streamlit Cloud (free)
3. Get your URL: https://oracle-app.streamlit.app
```

### Step 2: Create Oracle Page in Wix

**A. Add New Page:**
1. Open Wix Editor
2. Click **"Pages & Menu"** (left sidebar)
3. Click **"+ Add Page"**
4. Select **"Blank Page"**
5. Name it: "Oracle Reading" or "Divination"

**B. Remove Default Elements:**
1. Delete any default text boxes, images
2. Leave the page clean and empty

### Step 3: Add iframe Element

**A. Insert iframe:**
1. Click **"Add Elements"** (+ button, left sidebar)
2. Scroll to **"Embed"** section
3. Click **"HTML iframe"**
4. Drag it onto your page

**B. Resize & Position:**
1. Drag corners to fill most of the page
2. Leave ~50px margin on sides
3. Position it centered

### Step 4: Configure iframe Code

**A. Enter Code:**
1. Click on the iframe element
2. Click **"Enter Code"** button (appears above element)
3. **Delete** any default code
4. **Paste** this:

```html
<iframe 
  src="https://your-oracle-app.streamlit.app/?embed=true" 
  width="100%" 
  height="1400px" 
  frameborder="0"
  allowfullscreen
  style="border: none;">
</iframe>
```

5. Replace `your-oracle-app` with YOUR actual Streamlit app name
6. Click **"Update"**

**B. Adjust Height:**
- Start with 1400px
- Preview your page
- Adjust height so scrollbars work well
- Ideal: 1200-1600px depending on your design

### Step 5: Add to Navigation

1. In **"Pages & Menu"**, ensure "Oracle Reading" is in your menu
2. Visitors can now click to access it!

### Step 6: Publish!

1. Click **"Publish"** (top right)
2. Your Oracle is now live on your Wix site!

**Example:** `https://yoursite.wixsite.com/mysite/oracle-reading`

---

## 🎨 Integration Method 2: Section Embed

Embed the Oracle as a section within an existing page.

### When to Use This
- Part of a services page
- Section of your homepage
- Among other offerings

### Steps

1. **Go to desired page** in Wix Editor

2. **Add Header Section:**
   - Add text: "Consult The Oracle"
   - Add description paragraph
   - Style to match your site

3. **Add iframe Below:**
   - Same as Method 1
   - Smaller height (800-1000px)
   - Visitors scroll within your page

4. **Add Footer Text** (optional):
   - Explain the Oracle
   - Add testimonials

---

## 💡 Integration Method 3: Button Link (Simplest)

Don't embed - just link to your Streamlit app.

### Steps

1. **Add Button on Wix Page:**
   - Text: "Get Your Oracle Reading"
   - Style: Match your site

2. **Link to Streamlit URL:**
   - Click button → Link settings
   - External URL: `https://your-oracle-app.streamlit.app`
   - Open in: **New tab** ✅

3. **Done!**
   - Users click button → Oracle opens in new tab
   - Simplest integration
   - No iframe issues

---

## 🔧 Advanced: Using Wix Velo (Optional)

For developers who want more control.

### Create Modal/Popup Oracle

```javascript
// In Wix Velo Code Panel (Developer Tools)

$w.onReady(function () {
    $w("#oracleButton").onClick(() => {
        $w("#oracleModal").show();
    });
    
    $w("#closeButton").onClick(() => {
        $w("#oracleModal").hide();
    });
});
```

**Setup:**
1. Enable Velo (Wix's coding platform)
2. Create a lightbox (modal)
3. Add iframe inside lightbox
4. Add button to trigger modal
5. Users click button → Oracle pops up

---

## 📱 Mobile Optimization

Your embedded Oracle works on mobile! But consider:

### Tips for Mobile Experience

1. **Responsive iframe:**
```html
<iframe 
  src="https://your-oracle-app.streamlit.app/?embed=true" 
  width="100%" 
  height="1200px" 
  frameborder="0"
  style="border: none; max-width: 100%;">
</iframe>
```

2. **Mobile Settings in Wix:**
   - Switch to mobile editor
   - Adjust iframe height for mobile (maybe 1000px)
   - Test on actual device

3. **Consider Button Link for Mobile:**
   - On mobile: show button that opens new tab
   - On desktop: show embedded iframe
   - Cleaner mobile experience

---

## 🎨 Styling to Match Your Wix Site

### Match Your Wix Theme Colors

Update `.streamlit/config.toml`:

```toml
[theme]
base = "dark"
primaryColor = "#YOUR_WIX_ACCENT_COLOR"
backgroundColor = "#YOUR_WIX_BACKGROUND"
secondaryBackgroundColor = "#YOUR_WIX_SECONDARY"
textColor = "#YOUR_WIX_TEXT_COLOR"
```

Get colors from Wix:
1. Wix Editor → Site Design → Site Colors
2. Copy hex codes
3. Update config.toml
4. Redeploy to Streamlit Cloud

### Add Wix Styling Around iframe

```html
<style>
  .oracle-wrapper {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
  }
</style>

<div class="oracle-wrapper">
  <iframe 
    src="https://your-oracle-app.streamlit.app/?embed=true" 
    width="100%" 
    height="1200px" 
    frameborder="0"
    style="border: none; border-radius: 10px;">
  </iframe>
</div>
```

---

## 🐛 Troubleshooting

### iframe Not Showing

**Problem:** Blank space where iframe should be
**Solutions:**
- Check Streamlit app is actually deployed and accessible
- Try the URL directly in browser first
- Clear Wix editor cache and refresh
- Check for typos in URL

### iframe Too Small/Large

**Problem:** Content cut off or too much white space
**Solutions:**
- Adjust `height="1400px"` value
- Test different heights: 1000px, 1200px, 1600px
- On mobile, might need different height

### Scrollbars Within Scrollbars

**Problem:** Double scrolling (page + iframe)
**Solutions:**
- Make iframe height larger (less internal scrolling)
- Or make it full-page embed
- Consider button link instead of embed

### Oracle Looks Different

**Problem:** Colors/styling don't match Wix site
**Solutions:**
- Update `.streamlit/config.toml` with your Wix colors
- Redeploy Streamlit app
- Takes 2-3 minutes to apply

### "Refused to Connect" Error

**Problem:** Browser blocks iframe
**Solutions:**
- Ensure using `?embed=true` in URL
- Check Streamlit app allows embedding
- Try different browser
- Rarely happens with Streamlit Cloud

---

## ✅ Pre-Launch Checklist

Before making your Oracle live on Wix:

- [ ] Oracle deployed to Streamlit Cloud
- [ ] Test Streamlit URL works in browser
- [ ] iframe code configured with correct URL
- [ ] Tested on desktop browser
- [ ] Tested on mobile device
- [ ] Colors match your Wix theme (optional)
- [ ] Added to Wix navigation menu
- [ ] Page title/description set
- [ ] Published Wix site
- [ ] Tested live Wix page
- [ ] Shared with friend for feedback

---

## 📊 Comparison: Embed vs. Link

| Factor | iframe Embed | Button Link |
|--------|--------------|-------------|
| User stays on your site | ✅ Yes | ❌ No (new tab) |
| Setup complexity | Medium | Easy |
| Mobile experience | Good | Excellent |
| Loading speed | Slower | Faster |
| Looks native | ✅ Yes | ❌ No |
| Maintenance | Same URL | Same URL |
| **Recommended for** | Main offering | Secondary feature |

---

## 🎯 Recommended Approach

**For Most Users:**
1. ✅ **Deploy to Streamlit Cloud** (FREE)
2. ✅ **Create dedicated Wix page**
3. ✅ **Full-page iframe embed**
4. ✅ **Add to main navigation**

**Why this works:**
- Professional look
- Users don't leave your site
- Easy to maintain
- Works on all devices
- Completely free

---

## 💰 Cost Breakdown

**Total Cost: $0** (completely free!)

- **Wix:** Use existing site (free or paid plan works)
- **Streamlit Cloud:** FREE hosting
- **Gemini API:** FREE tier (thousands of readings/month)
- **Domain:** Use your existing Wix domain

**If traffic grows:**
- Gemini paid tier: ~$0.0005 per reading
- Still extremely cheap!

---

## 🌟 Example Integration

**Your Wix Site Structure:**
```
Home
About
Services
  → Oracle Reading ← (new page with iframe)
Blog
Contact
```

**User Experience:**
1. User visits: `yoursite.com`
2. Clicks "Oracle Reading" in menu
3. Oracle app loads within your Wix page
4. User generates reading
5. Downloads markdown report
6. Returns to your Wix site
7. Seamless experience!

---

## 📞 Need Help?

**Wix iframe Issues:**
- Wix Support: https://support.wix.com
- Search: "embed iframe in Wix"

**Streamlit Deployment:**
- See `DEPLOYMENT_GUIDE.md`
- Streamlit Docs: https://docs.streamlit.io

**This Oracle App:**
- All code is ready to deploy
- Just follow steps above!

---

## 🎉 You're Ready!

Your Oracle can be live on your Wix website in about **15 minutes:**

1. ✅ 10 min: Deploy to Streamlit Cloud
2. ✅ 5 min: Embed in Wix
3. ✅ 0 min: Publish and share!

**Result:** Professional oracle reading system fully integrated into your existing Wix website! 🔮✨

