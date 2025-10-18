#!/bin/bash

# Build script for AI Furniture Frontend

echo "Building AI Furniture Frontend for production..."

# Install dependencies
echo "Installing dependencies..."
npm install

# Create production build
echo "Creating production build..."
npm run build

echo "Build completed! Deploy the 'build' folder to your hosting service."
echo "Make sure to update REACT_APP_API_URL in .env.production with your backend URL."