# GitHub Repository & Website Setup Guide

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Fill in the details:
   - **Repository name**: `capacitor-calculator` (or your preferred name)
   - **Description**: "Nominal Test Capacitance Calculator for Power Systems"
   - **Visibility**: Choose Public (for GitHub Pages) or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

## Step 2: Initialize Local Git Repository

Open PowerShell in your project directory and run:

```powershell
cd "c:\Users\lmaskell\PACE TECHNOLOGIES INC\Main - TechRef\Capacitors\Pace Capacitor Calculator"

# Initialize git repository
git init

# Add all files
git add index.html README.md .gitignore

# Create first commit
git commit -m "Initial commit: Nominal Test Capacitance Calculator"

# Add your GitHub repository as remote (replace USERNAME and REPO_NAME)
git remote add origin https://github.com/USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** (top menu)
3. In the left sidebar, click **Pages**
4. Under "Source", select:
   - **Branch**: `main`
   - **Folder**: `/ (root)`
5. Click **Save**
6. Wait a few minutes for deployment

## Step 4: Access Your Website

After deployment (usually 1-5 minutes), your calculator will be available at:

```
https://USERNAME.github.io/REPO_NAME/
```

For example, if your username is `pacetechnologies` and repo is `capacitor-calculator`:
```
https://pacetechnologies.github.io/capacitor-calculator/
```

## Step 5: Custom Domain (Optional)

If you want to use a custom domain like `calculator.pacetechnologies.com`:

1. In GitHub Pages settings, enter your custom domain
2. Add a CNAME record in your DNS provider pointing to:
   ```
   USERNAME.github.io
   ```
3. Wait for DNS propagation (can take up to 48 hours)

## Updating the Website

Whenever you make changes:

```powershell
# Navigate to your project directory
cd "c:\Users\lmaskell\PACE TECHNOLOGIES INC\Main - TechRef\Capacitors\Pace Capacitor Calculator"

# Add changes
git add .

# Commit with a message
git commit -m "Description of your changes"

# Push to GitHub
git push
```

GitHub Pages will automatically update your website within a few minutes.

## Files Included

- `index.html` - The main calculator (GitHub Pages looks for this file)
- `README.md` - Documentation for the repository
- `.gitignore` - Files to exclude from git

## Troubleshooting

**Issue**: Repository creation fails
- **Solution**: Make sure you're logged into GitHub and have permission to create repos

**Issue**: Git push fails
- **Solution**: You may need to authenticate. Use GitHub's personal access token or SSH keys

**Issue**: Website not showing up
- **Solution**: Wait 5-10 minutes after enabling Pages. Check the Actions tab for deployment status

**Issue**: Changes not appearing on website
- **Solution**: Clear your browser cache or try incognito mode. Changes can take 1-5 minutes to deploy

## Alternative: Quick Setup with GitHub Desktop

If you prefer a GUI:

1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Create new repository in GitHub Desktop
3. Choose the folder: `c:\Users\lmaskell\PACE TECHNOLOGIES INC\Main - TechRef\Capacitors\Pace Capacitor Calculator`
4. Publish to GitHub
5. Follow Step 3 above to enable GitHub Pages

## Security Note

Since this will be public, the calculator is client-side only (no server, no data collection). All calculations happen in the user's browser.
