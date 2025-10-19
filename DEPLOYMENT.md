# 🚀 Deployment Guide - AI Furniture Platform

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Environment Setup](#environment-setup)
- [Deployment Options](#deployment-options)
- [Production Configuration](#production-configuration)
- [Troubleshooting](#troubleshooting)

## 🚀 Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/your-username/ai-furniture-platform.git
cd ai-furniture-platform

# Backend setup
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Run both services
# Terminal 1 (Backend)
cd backend
python start_server.py

# Terminal 2 (Frontend)
cd frontend
npm start
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access:
# Frontend: http://localhost:3000
# Backend: http://localhost:8001
```

## 🔧 Environment Setup

### Required Environment Variables

#### Backend (.env)
```env
# Basic Configuration
ENVIRONMENT=production
DEBUG=false
HOST=0.0.0.0
PORT=8001

# CORS Settings
FRONTEND_URL=https://your-frontend-domain.com
ALLOWED_ORIGINS=https://your-frontend-domain.com

# AI API Keys (Optional but recommended)
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_TOKEN=your_huggingface_token
```

#### Frontend (.env.production)
```env
GENERATE_SOURCEMAP=false
REACT_APP_API_URL=https://your-backend-api.com
REACT_APP_ENVIRONMENT=production
```

## 🌐 Deployment Options

### 1. Railway (Backend) + Vercel (Frontend)

#### Backend on Railway:
1. Connect your GitHub repository to Railway
2. Select the `backend` folder as the root directory
3. Set environment variables in Railway dashboard
4. Deploy automatically triggers on push to main branch

#### Frontend on Vercel:
1. Connect your GitHub repository to Vercel
2. Set root directory to `frontend`
3. Configure environment variables
4. Deploy automatically on push

### 2. Heroku Deployment

#### Backend:
```bash
# Install Heroku CLI
heroku create your-app-name-backend
heroku config:set ENVIRONMENT=production
heroku config:set DEBUG=false
# Set other environment variables...

# Deploy
git subtree push --prefix backend heroku main
```

#### Frontend:
```bash
heroku create your-app-name-frontend
heroku buildpacks:set mars/create-react-app
# Deploy frontend...
```

### 3. DigitalOcean App Platform

1. Create new app from GitHub
2. Configure build and run commands
3. Set environment variables
4. Deploy

### 4. AWS/GCP/Azure

Use the provided `Dockerfile` files for containerized deployment on any cloud platform.

## ⚙️ Production Configuration

### Backend Optimizations:
- **Workers**: Use `uvicorn` with multiple workers in production
- **Database**: Consider PostgreSQL for production (currently using CSV)
- **Caching**: Enable Redis for better performance
- **Monitoring**: Add application monitoring (e.g., Sentry)

### Frontend Optimizations:
- **CDN**: Use CDN for static asset delivery
- **Compression**: Enable gzip compression (included in nginx config)
- **Caching**: Configure proper cache headers
- **Bundle Analysis**: Use `npm run build` and analyze bundle size

## 🎯 Features & Capabilities

### Core Features:
- ✅ AI-powered furniture search (312 products)
- ✅ Natural language queries
- ✅ Analytics dashboard
- ✅ Responsive design
- ✅ Dark theme UI

### AI Integration:
- **Semantic Search**: Pinecone vector database (optional)
- **Text Generation**: Google Gemini AI (optional)
- **Embeddings**: Sentence transformers
- **Fallback**: Keyword search when AI services unavailable

### Performance:
- **Backend**: FastAPI with async support
- **Frontend**: React with optimized builds
- **Database**: CSV-based (easily replaceable)
- **Caching**: Built-in caching mechanisms

## 🔍 Troubleshooting

### Common Issues:

#### Backend won't start:
- Check Python version (3.11+ recommended)
- Verify all dependencies installed
- Check environment variables
- Ensure port 8001 is available

#### Frontend build fails:
- Clear node_modules and reinstall
- Check Node.js version (18+ recommended)
- Verify all environment variables set

#### CORS errors:
- Update FRONTEND_URL in backend .env
- Check ALLOWED_ORIGINS configuration
- Ensure both services are running

#### API connection issues:
- Verify REACT_APP_API_URL points to correct backend
- Check firewall settings
- Confirm backend health endpoint: `/health`

### Performance Optimization:
```bash
# Backend
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main_server:app

# Frontend
npm run build
# Serve build/ directory with nginx or similar
```

## 📊 Monitoring & Health Checks

### Health Endpoints:
- **Backend**: `GET /health`
- **API Docs**: `GET /docs`
- **Analytics**: `GET /api/analytics`

### Expected Responses:
```json
{
  "status": "healthy",
  "timestamp": "2025-10-18T...",
  "version": "2.0.0-enhanced",
  "dataset_loaded": true,
  "dataset_size": 312
}
```

## 🔐 Security Considerations

- Environment variables for sensitive data
- CORS properly configured
- Security headers in nginx config
- Non-root user in Docker containers
- Input validation and sanitization

## 📈 Scaling

- Use load balancers for multiple backend instances
- Implement Redis for session management
- Consider microservices architecture for larger scale
- Monitor performance and optimize bottlenecks

## 📞 Support

For deployment issues:
1. Check logs in your deployment platform
2. Verify environment variables
3. Test locally first
4. Check GitHub Actions for CI/CD pipeline status

---

**Ready to deploy your AI Furniture Platform! 🚀**