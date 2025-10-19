# Root Dockerfile to build and run the FastAPI backend from /backend
FROM python:3.11-slim

WORKDIR /app

# System deps (optional: build tools for some wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source and data
COPY backend/ ./
COPY data ./data

# Env and port
ENV HOST=0.0.0.0
ENV PORT=8001
EXPOSE 8001

# Start app
CMD ["python", "main_server.py"]
