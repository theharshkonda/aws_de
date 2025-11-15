# GitHub Pages Deployment Guide

## Overview
This guide will help you deploy your AWS Data Engineer Bootcamp website to GitHub Pages while keeping your main repository private.

## Strategy: Separate Repositories

### Option 1: Two Separate Repositories (Recommended)
1. **Private Repo**: Contains all bootcamp materials (code, notes, exercises)
2. **Public Repo**: Contains only the `docs/` folder (the website)

### Option 2: Single Repository with GitHub Actions
Keep everything in one private repo and use GitHub Actions to deploy only the `docs/` folder publicly.

---

## 🚀 Quick Setup (Option 1 - Recommended)

### Step 1: Create Private Repository for Bootcamp Materials

```bash
cd "d:\Data Engineering\AWS-Data-Engineer-2-Month-Bootcamp"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AWS Data Engineer Bootcamp materials"

# Create private repository on GitHub
# Go to: https://github.com/new
# Name: aws-data-engineer-bootcamp-private
# Visibility: Private
# Click "Create repository"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/aws-data-engineer-bootcamp-private.git
git branch -M main
git push -u origin main
```

### Step 2: Create Public Repository for Website

```bash
# Create a new folder for public website
cd "d:\Data Engineering"
mkdir aws-bootcamp-website
cd aws-bootcamp-website

# Copy only docs folder
xcopy "..\AWS-Data-Engineer-2-Month-Bootcamp\docs\*" "." /E /I

# Initialize git
git init

# Add README
echo "# AWS Data Engineer Bootcamp - Learning Dashboard" > README.md
echo "" >> README.md
echo "Visit the website: https://YOUR_USERNAME.github.io/aws-bootcamp-website" >> README.md
echo "" >> README.md
echo "A comprehensive 8-week bootcamp to become an interview-ready AWS Data Engineer." >> README.md

# Add all files
git add .

# Commit
git commit -m "Initial deployment of bootcamp website"

# Create public repository on GitHub
# Go to: https://github.com/new
# Name: aws-bootcamp-website
# Visibility: Public
# Click "Create repository"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/aws-bootcamp-website.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your public repository: `https://github.com/YOUR_USERNAME/aws-bootcamp-website`
2. Click **Settings**
3. Scroll to **Pages** (in left sidebar)
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes for deployment
7. Visit: `https://YOUR_USERNAME.github.io/aws-bootcamp-website`

---

## 🔄 Updating Your Website

### When You Make Changes

```bash
# Option 1: Manual Update
cd "d:\Data Engineering\aws-bootcamp-website"

# Copy updated files from docs folder
xcopy "..\AWS-Data-Engineer-2-Month-Bootcamp\docs\*" "." /E /I /Y

# Commit and push
git add .
git commit -m "Update website content"
git push
```

### Option 2: Automated Script

Create `update-website.bat`:

```batch
@echo off
echo Updating website from docs folder...

cd "d:\Data Engineering\aws-bootcamp-website"

echo Copying files...
xcopy "..\AWS-Data-Engineer-2-Month-Bootcamp\docs\*" "." /E /I /Y

echo Committing changes...
git add .
git commit -m "Auto-update website - %date% %time%"

echo Pushing to GitHub...
git push

echo Done! Website updated.
pause
```

Save and run this script whenever you update the docs folder.

---

## 🔒 Alternative: Single Repository with Separate Branch

### Setup

```bash
cd "d:\Data Engineering\AWS-Data-Engineer-2-Month-Bootcamp"

# Create gh-pages branch for website
git checkout --orphan gh-pages

# Remove all files
git rm -rf .

# Copy docs content to root
xcopy "docs\*" "." /E /I

# Commit
git add .
git commit -m "GitHub Pages: Initial website deployment"

# Push
git push origin gh-pages

# Switch back to main
git checkout main
```

### Enable GitHub Pages

1. Go to repository **Settings**
2. Click **Pages**
3. Select:
   - Branch: `gh-pages`
   - Folder: `/ (root)`
4. Save

**Note**: Your main repository will still be private, but the `gh-pages` branch will be publicly accessible.

---

## 📝 Folder Structure for Deployment

Your `docs/` folder already has the correct structure:

```
docs/
├── index.html                 ← Main page
├── _config.yml               ← GitHub Pages config
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── pages/
    ├── week1-2.html
    ├── week3.html
    ├── week4.html
    └── ... (more pages)
```

---
