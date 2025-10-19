# Root Dockerfile to build and run the FastAPI backend from /backend
FROM python:3.11-slim

# Keep backend at /app/backend so code can resolve ../data correctly
WORKDIR /app/backend

# System deps (optional: build tools and curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ curl \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source and dataset to /app/data
COPY backend/ ./
COPY data /app/data

# Env and port
ENV HOST=0.0.0.0
ENV PORT=8001
EXPOSE 8001

# Start app
CMD ["python", "main_server.py"]
