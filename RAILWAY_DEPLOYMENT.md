# 🚂 Railway Deployment Guide - Environment Variables

## Step-by-Step Railway Deployment

### Step 1: Go to Railway
1. Open [https://railway.app](https://railway.app)
2. Click "Login" and sign up with your GitHub account
3. You'll see your Railway dashboard

### Step 2: Create New Project
1. Click "New Project" button
2. Select "Deploy from GitHub repo"
3. Choose your repository: `rxxj25/AI-PROJECT-EVALUATOR`
4. Click "Deploy Now"

### Step 3: Add Environment Variables (CRITICAL!)

**Method 1: Through Railway Dashboard**
1. Once your project is deployed, click on your project name
2. Click on the **"Variables"** tab (next to "Deployments", "Settings")
3. Click **"New Variable"** button
4. Add each variable one by one:

```
Variable Name: SNOWFLAKE_ACCOUNT
Value: sfsehol-natwest_learnaix_hack4acause_zrkzae
```

```
Variable Name: SNOWFLAKE_USER
Value: USER
```

```
Variable Name: SNOWFLAKE_PASSWORD
Value: sn0wf@ll
```

```
Variable Name: GEMINI_API_KEY
Value: AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
```

```
Variable Name: FLASK_ENV
Value: production
```

**Method 2: Through Railway CLI (Alternative)**
1. Install Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Link project: `railway link`
4. Add variables:
```bash
railway variables set SNOWFLAKE_ACCOUNT=sfsehol-natwest_learnaix_hack4acause_zrkzae
railway variables set SNOWFLAKE_USER=USER
railway variables set SNOWFLAKE_PASSWORD=sn0wf@ll
railway variables set GEMINI_API_KEY=AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk
railway variables set FLASK_ENV=production
```

### Step 4: Configure Build Settings
1. Go to **"Settings"** tab
2. Under **"Build"** section:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`

### Step 5: Redeploy
1. After adding all environment variables, click **"Redeploy"**
2. Railway will rebuild your app with the new variables
3. Wait 2-3 minutes for deployment

### Step 6: Get Your Live URL
1. Go to **"Deployments"** tab
2. Click on your latest deployment
3. Your live URL will be: `https://ai-project-evaluator-blitzwizard-production.up.railway.app`

---

## 🔧 Railway Environment Variables Screenshot Guide

**In Railway Dashboard:**
1. **Project Overview** → Click your project
2. **Variables Tab** → Click "Variables" (next to Deployments)
3. **New Variable** → Click "New Variable" button
4. **Add Each Variable**:
   - Name: `SNOWFLAKE_ACCOUNT`
   - Value: `sfsehol-natwest_learnaix_hack4acause_zrkzae`
   - Click "Add"
   - Repeat for all 5 variables

---

## ✅ Verification Steps

After deployment, test these features:
1. **Visit your Railway URL**
2. **Test Dashboard** - Should load without errors
3. **Test Project Submission** - Submit a test project
4. **Test AI Evaluation** - Check if AI scoring works
5. **Test Leaderboard** - Verify rankings display

---

## 🚨 Troubleshooting

**If deployment fails:**
1. Check **"Logs"** tab for error messages
2. Verify all environment variables are set correctly
3. Ensure Python version is 3.11
4. Check that `requirements.txt` is in root directory

**If app doesn't work:**
1. Verify Snowflake credentials are correct
2. Check Gemini API key is valid
3. Ensure all environment variables are spelled correctly
4. Check Railway logs for specific errors

---

## 🎯 Your Live URL

Once deployed successfully, your AI Project Evaluator will be live at:
**`https://ai-project-evaluator-blitzwizard-production.up.railway.app`**

Railway provides:
- ✅ **Free tier** with generous limits
- ✅ **Automatic deployments** from GitHub
- ✅ **Easy environment variable management**
- ✅ **Built-in monitoring and logs**
- ✅ **Custom domain support**

Your app will be live and ready for the hackathon! 🚀
