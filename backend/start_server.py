#!/usr/bin/env python3
"""
Simple server startup script
"""
import uvicorn
from main_server import app

if __name__ == "__main__":
    print("🚀 Starting AI Furniture Recommendation Platform Backend...")
    print("📊 Loading dataset...")
    
    # Import and load dataset
    from main_server import load_furniture_dataset
    dataset = load_furniture_dataset()
    print(f"✅ Dataset loaded with {len(dataset)} products")
    
    print("🌐 Starting server on http://127.0.0.1:8001")
    print("📝 API docs available at http://127.0.0.1:8001/docs")
    print("💡 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start the server
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8001, 
        log_level="info",
        reload=False
    )