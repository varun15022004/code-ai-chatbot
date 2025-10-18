# AI Furniture Discovery Platform - Deployment Guide

## Overview
This guide will help you deploy the AI-Powered Furniture Recommendation Platform to production. The application consists of:
- **Backend**: FastAPI server with Gemini AI integration
- **Frontend**: React application with modern UI

## Prerequisites
- Git account (GitHub, GitLab, etc.)
- Backend deployment platform account (Render, Railway, or Heroku)
- Frontend deployment platform account (Vercel, Netlify, or similar)
- API Keys: Gemini AI, Pinecone (optional)

## Quick Deployment Steps

### Option 1: Using Render (Recommended)

#### Backend Deployment on Render:

1. **Prepare Your Repository**:
   - Push your code to GitHub
   - Ensure all files are committed, including the `data` folder

2. **Deploy Backend on Render**:
   - Go to [render.com](https://render.com) and create account
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure service:
     - **Name**: `ai-furniture-backend`
     - **Root Directory**: `backend`
     - **Runtime**: `Python`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn main_server:app --host 0.0.0.0 --port $PORT`

3. **Set Environment Variables** in Render dashboard:
   ```
   GEMINI_API_KEY=your_actual_gemini_key
   PINECONE_API_KEY=your_pinecone_key (optional)
   ENVIRONMENT=production
   ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app
   ```

4. **Deploy**: Click "Deploy Web Service"

#### Frontend Deployment on Vercel:

1. **Update Frontend Configuration**:
   - Update `frontend/.env.production` with your backend URL:
   ```
   REACT_APP_API_URL=https://your-backend-name.onrender.com
   ```

2. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com) and create account
   - Import your GitHub repository
   - Configure build settings:
     - **Root Directory**: `frontend`
     - **Build Command**: `npm run build`
     - **Output Directory**: `build`

3. **Set Environment Variables** in Vercel dashboard:
   ```
   REACT_APP_API_URL=https://your-backend-name.onrender.com
   REACT_APP_ENVIRONMENT=production
   ```

### Option 2: Using Railway

#### Backend on Railway:
1. Go to [railway.app](https://railway.app)
2. Create new project from GitHub repo
3. Set root directory to `backend`
4. Add environment variables
5. Railway auto-detects Python and deploys

#### Frontend on Netlify:
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop your `frontend/build` folder (after running `npm run build`)
3. Update API URL in settings

## Environment Variables

### Backend (.env):
```bash
# Required
GEMINI_API_KEY=your_gemini_api_key

# Optional but recommended
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX_NAME=furniture-search
ENVIRONMENT=production
ALLOWED_ORIGINS=https://your-frontend-domain.com

# Auto-configured by platform
PORT=8000
HOST=0.0.0.0
```

### Frontend (.env.production):
```bash
REACT_APP_API_URL=https://your-backend-domain.com
REACT_APP_ENVIRONMENT=production
```

## Testing Deployment

1. **Test Backend**: Visit `https://your-backend-url/docs` to see API documentation
2. **Test Health**: Visit `https://your-backend-url/health`
3. **Test Frontend**: Visit your frontend URL and try searching for furniture

## Troubleshooting

### Common Issues:

1. **CORS Errors**:
   - Make sure `ALLOWED_ORIGINS` includes your frontend URL
   - For testing, temporarily set `ENVIRONMENT=production` to allow all origins

2. **API Connection Issues**:
   - Verify `REACT_APP_API_URL` points to your backend
   - Check backend logs for errors

3. **Build Failures**:
   - Ensure all dependencies are in requirements.txt
   - Check Python version compatibility (recommended: 3.11)

4. **Data Loading Issues**:
   - Ensure the `data/intern_data_ikarus.csv` file is included in your repository
   - Check file permissions and path settings

### Logs and Debugging:

- **Render**: View logs in dashboard under your service
- **Vercel**: Check Function Logs in dashboard
- **Railway**: Built-in logging in project dashboard

## Scaling Considerations

- **Backend**: Consider using multiple workers: `--workers 2`
- **Database**: For production, consider moving data to a database (PostgreSQL, MongoDB)
- **Caching**: Implement Redis for search result caching
- **CDN**: Use a CDN for static assets and images

## Security Notes

- Never commit API keys to repository
- Use environment variables for all sensitive configuration
- Enable HTTPS for both frontend and backend
- Consider implementing rate limiting for production

## Cost Estimation

- **Render**: Free tier available, paid plans start at $7/month
- **Vercel**: Free tier with good limits, pro at $20/month
- **Railway**: $5/month for backend services
- **Gemini API**: Pay per API call (very affordable for moderate usage)

## Support

If you encounter issues:
1. Check the logs in your deployment platform
2. Verify all environment variables are set correctly
3. Test API endpoints directly using the `/docs` interface
4. Ensure the CSV data file is accessible to the backend

Happy deploying! 🚀