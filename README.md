# 🎁 Melu's 33 Birthday Wishes

A special birthday gift for Alamelu's 33rd birthday - a beautiful wish book with 33 QR codes, each unlocking a special wish.

## 🌐 Live Website

Once deployed to GitHub Pages, the wishes will be accessible at:
`https://krrulz.github.io/wish-book/`

Each wish page will be at:
`https://krrulz.github.io/wish-book/wishes/[wish-number]-[codename].html`

## 📁 Project Structure

```
wish-book/
├── index.html              # Landing page
├── assets/
│   └── style.css          # Styles for all pages
└── wishes/
    ├── 01-slow-sunday.html
    ├── 02-butter-toast.html
    └── ... (33 total wish pages)
```

## 🚀 How to Deploy to GitHub Pages

### Step 1: Create Repository
1. Go to https://github.com/krrulz
2. Click "New repository"
3. Name it: `wish-book`
4. Make it **Public** (required for GitHub Pages)
5. Click "Create repository"

### Step 2: Upload Files
You have two options:

**Option A: Using Git (Command Line)**
```bash
cd wish-book
git init
git add .
git commit -m "Initial commit: Melu's 33 birthday wishes"
git branch -M main
git remote add origin https://github.com/krrulz/wish-book.git
git push -u origin main
```

**Option B: Using GitHub Web Interface**
1. On your new repository page, click "uploading an existing file"
2. Drag and drop the entire `wish-book` folder contents
3. Click "Commit changes"

### Step 3: Enable GitHub Pages
1. Go to your repository Settings
2. Click "Pages" in the left sidebar
3. Under "Source", select "main" branch
4. Click "Save"
5. Wait 2-3 minutes for deployment

Your site will be live at: `https://krrulz.github.io/wish-book/`

## 🎨 Wish Book URLs

Each wish will have a unique URL for the QR codes:

| # | Codename | URL |
|---|----------|-----|
| 01 | Slow Sunday | https://krrulz.github.io/wish-book/wishes/01-slow-sunday.html |
| 02 | Butter Toast | https://krrulz.github.io/wish-book/wishes/02-butter-toast.html |
| 03 | Afterglow | https://krrulz.github.io/wish-book/wishes/03-afterglow.html |
| ... | ... | ... |
| 33 | Stardust | https://krrulz.github.io/wish-book/wishes/33-stardust.html |

## 📱 How It Works

1. **In the printed wish book**: Melu connects the dots to reveal a QR code
2. **Scan the QR code**: Opens the corresponding wish page
3. **Discover the wish**: Reads the beautiful description and rules
4. **Activate**: Clicks the button to send you a WhatsApp message

## 💝 Features

- ✨ Beautiful romantic design
- 📱 Mobile-responsive
- 💌 Direct WhatsApp integration
- 🎨 Themed descriptions for each wish
- ❤️ Animated elements and smooth transitions

## 🛠️ Customization

To update any wish:
1. Edit the corresponding HTML file in `wishes/` folder
2. Commit and push changes
3. GitHub Pages will auto-update in 1-2 minutes

---

Made with ❤️ for Alamelu's 33rd Birthday
