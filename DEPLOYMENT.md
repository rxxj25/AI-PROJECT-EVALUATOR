# 🚀 Deployment Guide for AI Project Evaluator

## Quick Deployment Options

### 1. 🆓 **Render (Recommended - FREE)**

**Steps:**
1. Go to [render.com](https://render.com) and sign up with GitHub
2. Click "New +" → "Web Service"
3. Connect your GitHub repository: `finos-labs/learnaix-h-2025-blitzwizard`
4. Configure:
   - **Name**: `ai-project-evaluator-blitzwizard`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
   - **Python Version**: `3.11`

5. **Environment Variables** (in Render dashboard):
   ```
   SNOWFLAKE_ACCOUNT=sfsehol-natwest_learnaix_hack4acause_zrkzae
   SNOWFLAKE_USER=USER
   SNOWFLAKE_PASSWORD=sn0wf@ll
   GEMINI_API_KEY=AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
   FLASK_ENV=production
   ```

6. Click "Create Web Service"
7. Your app will be available at: `https://ai-project-evaluator-blitzwizard.onrender.com`

---

### 2. 🆓 **Railway (Alternative - FREE)**

**Steps:**
1. Go to [railway.app](https://railway.app) and sign up with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository: `finos-labs/learnaix-h-2025-blitzwizard`
4. Railway will auto-detect Python and install dependencies
5. **Environment Variables** (in Railway dashboard):
   ```
   SNOWFLAKE_ACCOUNT=sfsehol-natwest_learnaix_hack4acause_zrkzae
   SNOWFLAKE_USER=USER
   SNOWFLAKE_PASSWORD=sn0wf@ll
   GEMINI_API_KEY=AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
   ```
6. Your app will be available at: `https://ai-project-evaluator-blitzwizard-production.up.railway.app`

---

### 3. 🆓 **Heroku (Alternative)**

**Steps:**
1. Install Heroku CLI: [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
2. Login to Heroku: `heroku login`
3. Create app: `heroku create ai-project-evaluator-blitzwizard`
4. Set environment variables:
   ```bash
   heroku config:set SNOWFLAKE_ACCOUNT=sfsehol-natwest_learnaix_hack4acause_zrkzae
   heroku config:set SNOWFLAKE_USER=USER
   heroku config:set SNOWFLAKE_PASSWORD=sn0wf@ll
   heroku config:set GEMINI_API_KEY=AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
   ```
5. Deploy: `git push heroku main`
6. Your app will be available at: `https://ai-project-evaluator-blitzwizard.herokuapp.com`

---

## 🔧 Manual Deployment Steps

### Step 1: Prepare Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Add deployment configuration"
git push origin main
```

### Step 2: Choose Platform
- **Render**: Best for beginners, automatic deployments
- **Railway**: Modern platform, great for Python apps
- **Heroku**: Traditional platform, requires CLI

### Step 3: Configure Environment Variables
All platforms need these environment variables:
```
SNOWFLAKE_ACCOUNT=sfsehol-natwest_learnaix_hack4acause_zrkzae
SNOWFLAKE_USER=USER
SNOWFLAKE_PASSWORD=sn0wf@ll
GEMINI_API_KEY=AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
FLASK_ENV=production
```

### Step 4: Test Deployment
1. Visit your deployed URL
2. Test project submission
3. Verify AI evaluation works
4. Check analytics dashboard

---

## 🎯 Recommended: Render Deployment

**Why Render?**
- ✅ **Free tier** with generous limits
- ✅ **Automatic deployments** from GitHub
- ✅ **Easy setup** - no CLI required
- ✅ **Reliable** and fast
- ✅ **Perfect for hackathons**

**Your deployed URL will be:**
`https://ai-project-evaluator-blitzwizard.onrender.com`

---

## 🔍 Troubleshooting

### Common Issues:
1. **Build fails**: Check Python version (3.11)
2. **Environment variables**: Ensure all are set correctly
3. **Port issues**: Use `$PORT` environment variable
4. **Dependencies**: Ensure `requirements.txt` is complete

### Debug Commands:
```bash
# Check logs in Render dashboard
# Or use Heroku CLI:
heroku logs --tail -a ai-project-evaluator-blitzwizard
```

---

## 📱 Update Your Template

Once deployed, update your `HACK4ACAUSE-TEMPLATE_USECASE_UPDATED.md`:

```markdown
## 🌐 Hosted App / Solution URL

- 🌍 **Deployed URL**: https://ai-project-evaluator-blitzwizard.onrender.com
```

---

## 🎉 Success!

Your AI-Powered Project Evaluator will be live and accessible to judges and participants!

**Next Steps:**
1. Deploy using Render (recommended)
2. Test all features
3. Update template with live URL
4. Commit and push changes
5. Submit to hackathon! 🏆
