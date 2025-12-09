# GitHub Pages Deployment Guide for Zealous Solutions

## Overview
Your website will be deployed to GitHub Pages for FREE and redirected to your GoDaddy domain. This is the most cost-effective solution!

## Step 1: Generate Static Files
Run the static site generator to create HTML files from your Flask app:

```bash
python generate_static.py
```

This creates a `docs/` folder with all your website pages as static HTML files.

## Step 2: Push to GitHub
1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Zealous Solutions website"
   ```

2. **Create GitHub Repository**:
   - Go to [GitHub.com](https://github.com)
   - Click "New Repository"
   - Name: `zealous-solutions-website`
   - Make it Public (required for free GitHub Pages)
   - Click "Create repository"

3. **Push Your Code**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/zealous-solutions-website.git
   git branch -M main
   git push -u origin main
   ```

## Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll to "Pages" in the left sidebar
4. Under "Source": Select "Deploy from a branch"
5. Choose "main" branch and "/docs" folder
6. Click "Save"

## Step 4: Configure Custom Domain (GoDaddy)
1. **In GitHub Repository Settings > Pages**:
   - Add your domain: `zealous-solutions.com`
   - Check "Enforce HTTPS"

2. **In GoDaddy DNS Settings**:
   ```
   Type: CNAME
   Name: www
   Value: dev778d.github.io
   
   Type: A
   Name: @
   Value: 185.199.108.153
   
   Type: A
   Name: @
   Value: 185.199.109.153
   
   Type: A
   Name: @
   Value: 185.199.110.153
   
   Type: A
   Name: @
   Value: 185.199.111.153
   ```

3. **Domain Redirection Setup**:
   - In GoDaddy, set up URL Forwarding/Redirection
   - Forward `zealous-solutions.com` → `https://dev778d.github.io/zealous-solutions-website/`
   - Forward `www.zealous-solutions.com` → `https://dev778d.github.io/zealous-solutions-website/`
   - Enable "Forward with masking" to keep your domain in the address bar

## Step 5: Automatic Deployment
The GitHub Action workflow will automatically:
- Generate static files when you push changes
- Deploy to GitHub Pages
- Update your live website at zealous-solutions.com

## Benefits of This Approach
- ✅ **FREE Hosting**: No monthly costs
- ✅ **Fast Loading**: Static files load instantly
- ✅ **Global CDN**: GitHub's worldwide content delivery
- ✅ **Automatic SSL**: HTTPS encryption included
- ✅ **Custom Domain**: Professional branding
- ✅ **Auto Deploy**: Push code → Live website

## Your Live URLs
- **GitHub Pages**: https://YOUR_USERNAME.github.io/zealous-solutions-website/
- **Custom Domain**: https://zealous-solutions.com (after DNS setup)

## Making Updates
1. Edit your Flask templates/static files
2. Run: `python generate_static.py`
3. Git commit and push
4. Website updates automatically!

## Troubleshooting
- **DNS Changes**: Take 24-48 hours to propagate
- **HTTPS Certificate**: May take up to 24 hours to generate
- **Build Errors**: Check GitHub Actions tab in your repository

## Next Steps
1. Run the static generator
2. Push to GitHub
3. Enable Pages
4. Configure your GoDaddy domain
5. Go live with professional call center website! 🚀