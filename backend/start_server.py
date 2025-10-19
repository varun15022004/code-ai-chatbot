#!/usr/bin/env python3
"""
Simple server startup script (Render/containers friendly)
"""
import os
import uvicorn
from main_server import app

if __name__ == "__main__":
    print("Starting AI Furniture Recommendation Platform Backend...")
    print("Loading dataset...")

    # Import and load dataset
    from main_server import load_furniture_dataset

    dataset = load_furniture_dataset()
    print(f"Dataset loaded with {len(dataset)} products")

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "10000"))
    print(f"Starting server on http://{host}:{port}")
    print(f"API docs available at http://{host}:{port}/docs")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)

    # Start the server
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info",
        reload=False,
    )
