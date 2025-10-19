#!/bin/bash

echo "🔧 Setting up AI Furniture Platform..."

# Check prerequisites
echo "📋 Checking prerequisites..."

# Check Python
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.11+"
    exit 1
fi

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 18+"
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm"
    exit 1
fi

echo "✅ Prerequisites check passed!"

# Setup Backend
echo "🐍 Setting up Backend..."
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv || python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit backend/.env with your API keys"
fi

cd ..

# Setup Frontend
echo "⚛️ Setting up Frontend..."
cd frontend

# Install dependencies
echo "Installing Node.js dependencies..."
npm install

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating frontend .env file..."
    echo "REACT_APP_API_URL=http://127.0.0.1:8001" > .env
fi

cd ..

echo "🎉 Setup completed successfully!"
echo ""
echo "📚 Next steps:"
echo "1. Edit backend/.env with your API keys (optional)"
echo "2. Run the project:"
echo "   - Development: ./start_development.sh"
echo "   - Production: ./start_production.sh"
echo "   - Docker: docker-compose up --build"
echo ""
echo "🌐 URLs:"
echo "   - Frontend: http://localhost:3000"
echo "   - Backend: http://127.0.0.1:8001"
echo "   - API Docs: http://127.0.0.1:8001/docs"
echo ""
echo "📖 For deployment: See DEPLOYMENT.md"