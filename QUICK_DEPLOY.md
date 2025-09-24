# 🚀 QUICK DEPLOYMENT - Get Live in 5 Minutes!

## Step 1: Go to Render.com
1. Open [https://render.com](https://render.com) in your browser
2. Click "Get Started for Free"
3. Sign up with your GitHub account (rxxj25)

## Step 2: Create New Web Service
1. Click "New +" → "Web Service"
2. Connect GitHub repository: `rxxj25/AI-PROJECT-EVALUATOR`
3. Click "Connect"

## Step 3: Configure Service
**Service Settings:**
- **Name**: `ai-project-evaluator-blitzwizard`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
- **Python Version**: `3.11`

## Step 4: Set Environment Variables
Click "Advanced" → "Environment Variables" and add:

```
SNOWFLAKE_ACCOUNT = sfsehol-natwest_learnaix_hack4acause_zrkzae
SNOWFLAKE_USER = USER
SNOWFLAKE_PASSWORD = sn0wf@ll
GEMINI_API_KEY = AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
FLASK_ENV = production
```

## Step 5: Deploy!
1. Click "Create Web Service"
2. Wait 2-3 minutes for deployment
3. Your app will be live at: `https://ai-project-evaluator-blitzwizard.onrender.com`

## 🎉 SUCCESS!
Your AI Project Evaluator will be live and accessible to everyone!

---

## Alternative: Railway (Even Faster)
1. Go to [https://railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `rxxj25/AI-PROJECT-EVALUATOR`
5. Add environment variables (same as above)
6. Deploy automatically!

**Railway URL**: `https://ai-project-evaluator-blitzwizard-production.up.railway.app`

---

## Test Your Live App
Once deployed, test these features:
- ✅ Main dashboard loads
- ✅ Project submission form works
- ✅ AI evaluation processes projects
- ✅ Leaderboard displays results
- ✅ Analytics dashboard shows data

Your app will be live and ready for the hackathon! 🏆
