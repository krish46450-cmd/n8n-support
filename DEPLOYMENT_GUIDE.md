# Support Dashboard Deployment Guide

This guide will help you deploy the Support Dashboard to Render.

## Prerequisites

- A [Render](https://render.com) account (free tier available)
- Git repository with your code (GitHub, GitLab, or Bitbucket)
- Updated environment variables

## Deployment Options

### Option 1: Deploy using Render Blueprint (Recommended)

This is the easiest method as it sets up both the web service and database automatically.

1. **Push your code to Git**
   ```bash
   cd "Support Dashboard"
   git init
   git add .
   git commit -m "Initial commit for deployment"
   git remote add origin <your-git-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New" → "Blueprint"
   - Connect your Git repository
   - Render will automatically detect the `render.yaml` file
   - Review the services (web service + PostgreSQL database)
   - Click "Apply" to deploy

3. **Initialize the database**

   After deployment completes:
   - Go to your web service in Render Dashboard
   - Click "Shell" tab to open a terminal
   - Run:
     ```bash
     python init_support_db.py
     ```

4. **Access your dashboard**
   - Your app will be available at: `https://support-dashboard-XXXXX.onrender.com`
   - Login with default credentials:
     - Manager: `admin` / `admin123`
     - Agent: `agent1` / `agent123`

   ⚠️ **Change these passwords immediately!**

### Option 2: Manual Deployment

If you prefer to set up services manually:

#### Step 1: Create PostgreSQL Database

1. In Render Dashboard, click "New" → "PostgreSQL"
2. Configure:
   - Name: `support-db`
   - Database: `support_dashboard`
   - User: `support_user`
   - Region: Choose closest to you
   - Plan: Free
3. Click "Create Database"
4. Copy the "Internal Database URL" (starts with `postgresql://`)

#### Step 2: Create Web Service

1. Click "New" → "Web Service"
2. Connect your Git repository
3. Configure:
   - **Name**: `support-dashboard`
   - **Region**: Same as your database
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: `Support Dashboard`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn support_app:app`
   - **Plan**: Free

#### Step 3: Set Environment Variables

In the web service settings, add these environment variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SUPPORT_SECRET_KEY` | (generate a random string - use a password generator) |
| `FLASK_ENV` | `production` |
| `SUPPORT_DATABASE_URL` | (paste the PostgreSQL Internal Database URL) |
| `CLIENT_API_URL` | (your client app URL, if deployed separately) |
| `SUPPORT_API_KEY` | (generate a random string for API authentication) |

4. Click "Save Changes"

#### Step 4: Deploy

1. Click "Manual Deploy" → "Deploy latest commit"
2. Wait for the build to complete (2-3 minutes)
3. Once deployed, open the Shell and run:
   ```bash
   python init_support_db.py
   ```

## Post-Deployment Configuration

### 1. Change Default Passwords

**IMPORTANT**: The default passwords are publicly known. Change them immediately:

1. Log in as admin
2. Create new admin users with strong passwords
3. Delete or update the default users

### 2. Configure Client App Integration

If you have a separate client app, update the `CLIENT_API_URL` environment variable to point to your client app's API endpoint.

### 3. Set Up Custom Domain (Optional)

1. In your web service settings, go to "Settings" → "Custom Domain"
2. Add your domain name
3. Follow Render's instructions to configure DNS

## Environment Variables Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SUPPORT_SECRET_KEY` | Flask secret key for session encryption | Yes | - |
| `FLASK_ENV` | Environment mode (`production` or `development`) | Yes | `production` |
| `SUPPORT_DATABASE_URL` | PostgreSQL connection string | Yes | - |
| `CLIENT_API_URL` | Client app API endpoint for integration | No | `http://localhost:5000/api` |
| `SUPPORT_API_KEY` | API key for secure inter-app communication | No | - |
| `PORT` | Port to run the app (Render sets this automatically) | No | `8001` |
| `PYTHON_VERSION` | Python version to use | No | `3.11.0` |

## Troubleshooting

### Build Fails

- Check that `requirements.txt` is in the root of "Support Dashboard" directory
- Verify Python version compatibility
- Check build logs for specific errors

### Database Connection Issues

- Ensure `SUPPORT_DATABASE_URL` is set correctly
- Verify the database is in the same region as your web service
- Check that the database is running (not suspended)

### App Won't Start

- Check that `gunicorn` is installed (it's in requirements.txt)
- Verify the start command: `gunicorn support_app:app`
- Check application logs for errors

### Can't Log In

- Ensure you ran `python init_support_db.py` after deployment
- Check database logs to verify tables were created
- Try accessing the Shell and running the init script again

## Monitoring and Maintenance

### View Logs

- In Render Dashboard → Your Web Service → "Logs" tab
- Real-time logs show all application activity

### Database Backups

Render Free tier:
- No automatic backups
- Export data manually if needed

Render Paid tier:
- Daily automatic backups
- Point-in-time recovery available

### Scaling

Free tier limitations:
- Service spins down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- 750 hours/month free compute time

To avoid spin-down:
- Upgrade to Starter plan ($7/month)
- Keeps service always running

## Security Best Practices

1. **Change default passwords immediately**
2. **Use strong, unique secrets** for `SUPPORT_SECRET_KEY`
3. **Enable HTTPS** (Render provides this automatically)
4. **Regularly update dependencies**
   ```bash
   pip list --outdated
   pip install --upgrade <package>
   ```
5. **Monitor access logs** for suspicious activity
6. **Keep API keys secret** - never commit them to Git

## Cost Breakdown

**Free Tier:**
- PostgreSQL Database: Free (1GB storage, shared CPU)
- Web Service: Free (750 hours/month)
- Total: $0/month

**If you need always-on service:**
- PostgreSQL Database: $7/month (256MB RAM, 1GB storage)
- Web Service: $7/month (512MB RAM, always on)
- Total: $14/month

## Next Steps

After successful deployment:

1. ✅ Change default passwords
2. ✅ Configure custom domain (optional)
3. ✅ Set up monitoring/alerts
4. ✅ Test all functionality
5. ✅ Create additional support staff accounts
6. ✅ Configure client app integration

## Support

For issues with:
- **Render Platform**: Check [Render Docs](https://render.com/docs)
- **Application Issues**: Check application logs and code

---

**Last Updated**: January 2026
