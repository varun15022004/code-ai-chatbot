#!/bin/bash

# Production startup script for AI Furniture Platform
echo "🚀 Starting AI Furniture Platform in Production Mode..."

# Check if Docker is available
if command -v docker &> /dev/null && command -v docker-compose &> /dev/null; then
    echo "🐳 Starting with Docker Compose..."
    docker-compose up --build -d
    
    echo "✅ Services started!"
    echo "🌐 Frontend: http://localhost:3000"
    echo "🔗 Backend: http://localhost:8001"
    echo "📝 API Docs: http://localhost:8001/docs"
    
    # Show logs
    echo "📋 Showing logs (Ctrl+C to exit)..."
    docker-compose logs -f
    
else
    echo "⚠️  Docker not found. Starting with manual setup..."
    
    # Backend
    echo "🔧 Starting Backend..."
    cd backend
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python -m venv venv
    fi
    
    source venv/bin/activate
    pip install -r requirements.txt
    python start_server.py &
    BACKEND_PID=$!
    cd ..
    
    # Frontend
    echo "🎨 Starting Frontend..."
    cd frontend
    if [ ! -d "node_modules" ]; then
        echo "Installing dependencies..."
        npm install
    fi
    
    npm run build
    npx serve -s build -l 3000 &
    FRONTEND_PID=$!
    cd ..
    
    echo "✅ Services started!"
    echo "🌐 Frontend: http://localhost:3000"
    echo "🔗 Backend: http://localhost:8001"
    
    # Wait for interrupt
    trap 'echo "Stopping services..."; kill $BACKEND_PID $FRONTEND_PID; exit' INT
    wait
fi