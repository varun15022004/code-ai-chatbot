#!/bin/bash

# Start script for AI Furniture Backend

echo "Starting AI Furniture Recommendation Backend..."

# Load environment variables
if [ -f .env ]; then
    echo "Loading environment variables..."
    source .env
fi

# Set default port if not specified
export PORT=${PORT:-8000}

# Start the server
echo "Starting server on port $PORT..."
uvicorn main_server:app --host 0.0.0.0 --port $PORT --workers 1