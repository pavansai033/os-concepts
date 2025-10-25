# 🚀 GitHub Setup Commands

## Replace YOUR_USERNAME with your actual GitHub username

```bash
# Navigate to your project directory
cd /workspace/project

# Add GitHub as remote origin
git remote add origin https://github.com/YOUR_USERNAME/operating-systems-concepts.git

# Rename master branch to main (GitHub's default)
git branch -M main

# Push your code to GitHub
git push -u origin main
```

## If you get authentication errors:

### Option 1: Use Personal Access Token
```bash
# Remove existing remote
git remote remove origin

# Add remote with token authentication
git remote add origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/operating-systems-concepts.git

# Push to GitHub
git push -u origin main
```

### Option 2: Use GitHub CLI (if installed)
```bash
# Login to GitHub
gh auth login

# Push to GitHub
git push -u origin main
```

## After successful push:

Your repository will be available at:
https://github.com/YOUR_USERNAME/operating-systems-concepts

## Share with friends:
- Repository URL: https://github.com/YOUR_USERNAME/operating-systems-concepts
- Live demo (if you enable GitHub Pages): https://YOUR_USERNAME.github.io/operating-systems-concepts