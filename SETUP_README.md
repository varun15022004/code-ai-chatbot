# AI-Powered Furniture Recommendation Platform - Complete Setup Guide

A comprehensive furniture discovery and recommendation system with AI-powered semantic search, conversational interfaces, and detailed analytics dashboards.

## 🚀 Features

- **AI-Powered Semantic Search**: Enhanced with Pinecone vector database for intelligent furniture discovery
- **Conversational Interface**: Natural language queries for furniture recommendations
- **Advanced Analytics**: Comprehensive dashboards showing product categories, price distributions, and search patterns
- **Smart Filtering**: Price-based filtering with natural language support
- **Real-time Search**: Fast, responsive search across all furniture attributes
- **Mobile-Responsive Design**: Modern, clean UI built with React and Tailwind CSS

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

### Required Software
- **Python 3.8 or higher** - [Download Python](https://python.org/downloads/)
- **Node.js 16.0 or higher** - [Download Node.js](https://nodejs.org/)
- **npm** (comes with Node.js) or **yarn**
- **Git** - [Download Git](https://git-scm.com/downloads)

### Optional Services
- **Pinecone Account** - For enhanced semantic search (free tier available)
- **OpenAI API Key** - For advanced AI features (optional)
- **Hugging Face Token** - For accessing certain AI models (optional)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "aarushi project final"
```

### 2. Backend Setup (Python FastAPI)

#### Navigate to Backend Directory
```bash
cd backend
```

#### Create Python Virtual Environment
```bash
# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Required Python Packages:**
- fastapi==0.104.1
- uvicorn[standard]==0.24.0
- fastapi==0.104.1
- uvicorn[standard]==0.24.0
- pandas==2.1.3
- numpy==1.25.2
- python-dotenv==1.0.0
- transformers==4.35.2
- torch==2.1.1
- sentence-transformers==2.2.2
- pinecone-client==2.2.4
- Pillow==10.1.0
- scikit-learn==1.3.2
- requests==2.31.0

#### Environment Configuration
1. Copy the environment template:
```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

2. Edit `.env` file with your configuration:
```env
# Pinecone Configuration (Optional but recommended)
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=us-east-1-aws
PINECONE_INDEX_NAME=furniture-recommendations

# Application Settings
ENVIRONMENT=development
DEBUG=true
HOST=0.0.0.0
PORT=8001

# CORS Settings
FRONTEND_URL=http://localhost:3000

# Data Settings
DATA_PATH=../data/intern_data_ikarus.csv
CLEANED_DATA_PATH=../data/cleaned_furniture_data.csv

# Model Settings
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
GENAI_MODEL=google/flan-t5-small
MAX_RESULTS=20
EMBEDDING_DIMENSION=384

# Cache Settings
ENABLE_CACHE=true
CACHE_TTL=3600
```

### 3. Frontend Setup (React)

#### Navigate to Frontend Directory
```bash
cd ../frontend
```

#### Install Node.js Dependencies
```bash
npm install
```

**Required Node.js Packages:**
- react ^18.2.0
- react-dom ^18.2.0
- react-router-dom ^6.8.0
- react-scripts 5.0.1
- axios ^1.6.2
- framer-motion ^10.16.16
- lucide-react ^0.292.0
- recharts ^2.8.0
- tailwindcss ^3.3.6

#### Frontend Environment Configuration
Create a `.env` file in the frontend directory:
```env
REACT_APP_API_URL=http://localhost:8001
REACT_APP_ENV=development
```

### 4. Data Setup

Ensure your furniture dataset (`intern_data_ikarus.csv`) is placed in the `data/` directory at the project root.

## 🚀 Running the Application

### Method 1: Run Both Services Manually

#### Terminal 1 - Start Backend Server
```bash
cd backend
# Activate virtual environment if not already active
# Windows Command Prompt
venv\Scripts\activate
# Windows PowerShell
venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

python main_server.py
```

The backend will start on: `http://localhost:8001`

You should see output like:
```
INFO:__main__:Loading furniture dataset...
INFO:__main__:Successfully loaded 312 furniture products from CSV
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8001
```

#### Terminal 2 - Start Frontend Server
```bash
cd frontend
npm start
```

The frontend will start on: `http://localhost:3000`

You should see output like:
```
Starting the development server...
webpack compiled with warnings
```

### Method 2: Quick Start Scripts

#### For Windows - Create `start.bat`
```batch
@echo off
echo Starting AI Furniture Recommendation Platform...

echo Starting Backend Server...
start "Backend" cmd /k "cd backend && venv\Scripts\activate && python main_server.py"

echo Waiting for backend to initialize...
timeout /t 5 /nobreak > nul

echo Starting Frontend Server...
start "Frontend" cmd /k "cd frontend && npm start"

echo Both servers are starting...
echo Backend: http://localhost:8001
echo Frontend: http://localhost:3000
echo API Documentation: http://localhost:8001/docs
pause
```

#### For macOS/Linux - Create `start.sh`
```bash
#!/bin/bash
echo "Starting AI Furniture Recommendation Platform..."

echo "Starting Backend Server..."
cd backend
source venv/bin/activate
python main_server.py &
BACKEND_PID=$!

echo "Waiting for backend to initialize..."
sleep 5

echo "Starting Frontend Server..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo "Both servers are running..."
echo "Backend: http://localhost:8001 (PID: $BACKEND_PID)"
echo "Frontend: http://localhost:3000 (PID: $FRONTEND_PID)"
echo "API Documentation: http://localhost:8001/docs"

# Keep script running
wait
```

Run the script:
```bash
# Windows
start.bat

# macOS/Linux
chmod +x start.sh
./start.sh
```

## 🌐 Application URLs

Once both servers are running, you can access:

- **Main Application**: `http://localhost:3000`
- **Analytics Dashboard**: `http://localhost:3000/analytics`
- **Backend API**: `http://localhost:8001`
- **API Documentation**: `http://localhost:8001/docs`
- **Health Check**: `http://localhost:8001/health`

## 🧪 Testing the Setup

### 1. Backend Health Check
Open a new terminal and run:
```bash
curl http://localhost:8001/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-10-18T10:00:00Z",
  "version": "2.0.0-enhanced",
  "dataset_loaded": true,
  "dataset_size": 312
}
```

### 2. Search API Test
```bash
curl -X POST "http://localhost:8001/search" \
-H "Content-Type: application/json" \
-d '{"query": "modern sofa under $500", "max_results": 5}'
```

### 3. Analytics API Test
```bash
curl http://localhost:8001/analytics
```

## 🐛 Troubleshooting

### Common Backend Issues

#### 1. Port 8001 Already in Use
**Error**: `[Errno 10048] error while attempting to bind on address`

**Solutions**:
```bash
# Windows - Find and kill process using port 8001
netstat -ano | findstr :8001
taskkill /PID <process_id> /F

# macOS/Linux - Find and kill process
lsof -ti:8001 | xargs kill -9
```

#### 2. Python Dependencies Installation Fails
**Error**: Package installation errors

**Solutions**:
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Clear pip cache and reinstall
pip cache purge
pip install -r requirements.txt --no-cache-dir

# If torch installation fails on Windows
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

#### 3. Virtual Environment Issues
**Error**: `venv\Scripts\activate` not working

**Solutions**:
```bash
# Windows - Enable script execution in PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Alternative activation methods
# Command Prompt
venv\Scripts\activate.bat
# PowerShell
venv\Scripts\Activate.ps1
```

#### 4. Dataset Not Found
**Error**: CSV file not found

**Solutions**:
- Ensure `intern_data_ikarus.csv` exists in `data/` directory
- Check file path in `.env` file
- Verify file permissions

### Common Frontend Issues

#### 1. Port 3000 Already in Use
**Error**: Port 3000 is already in use

**Solutions**:
- Choose alternative port when prompted
- Or manually specify: `PORT=3001 npm start`

#### 2. npm install Fails
**Error**: Package installation errors

**Solutions**:
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json  # macOS/Linux
rmdir /s node_modules & del package-lock.json  # Windows
npm install
```

#### 3. CORS Errors
**Error**: Network request blocked by CORS policy

**Solutions**:
- Verify backend is running on port 8001
- Check proxy settings in `package.json`
- Ensure backend CORS settings include frontend URL

#### 4. Build Warnings
**Error**: ESLint warnings during compilation

**Solutions**:
```bash
# Fix common ESLint issues
npm run lint --fix

# Ignore specific warnings (add to file)
// eslint-disable-next-line no-unused-vars
```

### Environment-Specific Issues

#### Windows Users
- Use **Command Prompt** or **PowerShell** (not Git Bash for Python)
- Ensure Python is added to PATH during installation
- May need to install **Microsoft Visual C++ Build Tools** for some packages

#### macOS Users
- May need to install **Xcode Command Line Tools**: `xcode-select --install`
- Use `python3` instead of `python` if both versions are installed

#### Linux Users
- May need to install additional system packages:
```bash
sudo apt-get update
sudo apt-get install python3-venv python3-pip nodejs npm
```

## 🔑 Optional Enhancements

### Setting up Pinecone (Recommended)
1. Sign up at [Pinecone](https://pinecone.io) (free tier available)
2. Create a new index:
   - **Index name**: `furniture-recommendations`
   - **Dimensions**: `384`
   - **Metric**: `cosine`
3. Get your API key and environment from dashboard
4. Update `.env` file with your credentials
5. Run initialization script: `python setup_pinecone.py`

### Adding OpenAI Integration (Optional)
1. Get API key from [OpenAI](https://openai.com/api/)
2. Add to `.env`: `OPENAI_API_KEY=your_key_here`
3. Restart backend server

## 📚 Project Structure

```
aarushi project final/
├── backend/                    # Python FastAPI server
│   ├── main_server.py         # Main server file
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example          # Environment template
│   ├── models/               # AI models
│   ├── routes/               # API endpoints
│   ├── services/             # Business logic
│   └── utils/                # Helper functions
├── frontend/                   # React application
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/           # Page components
│   │   └── utils/           # Utilities
│   ├── public/              # Static assets
│   ├── package.json         # Node.js dependencies
│   └── tailwind.config.js   # Tailwind configuration
├── data/                      # Dataset files
│   └── intern_data_ikarus.csv # Furniture dataset
├── .env                       # Global environment variables
├── README.md                  # Original documentation
└── SETUP_README.md           # This setup guide
```

## 🔍 API Documentation

Once running, visit `http://localhost:8001/docs` for interactive API documentation.

### Key Endpoints:
- **POST /search** - Search furniture items
- **GET /analytics** - Get analytics data
- **GET /health** - Health check
- **GET /greetings** - Conversational greetings

## 🎯 Usage Examples

### Search Query Examples:
- "Show me modern sofas under $500"
- "I need a wooden dining table for 6 people"
- "Find blue chairs for my office"
- "Recommend storage solutions for small spaces"

### Analytics Features:
- Product category distribution charts
- Price range analysis
- Material and color insights
- Search pattern analytics

## 📞 Support

If you encounter issues:

1. **Check this guide** for troubleshooting steps
2. **Verify installation** of all prerequisites
3. **Check logs** in terminal for specific error messages
4. **Restart services** if configuration changes were made
5. **Clear caches** (pip, npm) if dependency issues persist

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

**Happy furniture hunting! 🪑✨**

*For additional help, refer to the original README.md or create an issue in the repository.*