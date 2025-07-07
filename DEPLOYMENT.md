# Deploying Flask Blog to Render

## Prerequisites
- GitHub account with your code pushed
- Render account

## Step 1: Environment Variables Setup

You'll need to set these environment variables in Render:

### Required Environment Variables:
1. **SECRET_KEY**: A random secret key for Flask
   - Generate one: `python -c "import secrets; print(secrets.token_hex(16))"`
   - Example: `SECRET_KEY=your-generated-secret-key-here`

2. **SQLALCHEMY_DATABASE_URI**: PostgreSQL database connection string
   - Render will provide this when you create a PostgreSQL database
   - Format: `postgresql://username:password@host:port/database_name`

## Step 2: Create PostgreSQL Database on Render

1. Go to your Render dashboard
2. Click "New" → "PostgreSQL"
3. Choose a name for your database
4. Select a plan (Free tier available)
5. Click "Create Database"
6. Copy the "External Database URL" - this is your `SQLALCHEMY_DATABASE_URI`

## Step 3: Deploy the Web Service

1. In your Render dashboard, click "New" → "Web Service"
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: `flask-blog` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
4. Add Environment Variables:
   - `SECRET_KEY`: Your generated secret key
   - `SQLALCHEMY_DATABASE_URI`: The database URL from Step 2
5. Click "Create Web Service"

## Step 4: Database Initialization

After deployment, you may need to initialize your database. The app will create tables automatically when it first runs.

## Step 5: Access Your App

Your app will be available at: `https://your-app-name.onrender.com`

## Troubleshooting

- Check the logs in Render dashboard if deployment fails
- Ensure all environment variables are set correctly
- Make sure your database is running and accessible 