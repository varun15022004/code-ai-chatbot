FROM python:3.11-slim

# Set working directory inside container to mirror repo layout
WORKDIR /app/backend

# Install system dependencies (include curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ curl \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (backend) and data directory at /app/data
COPY . ./
COPY ../data /app/data

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8001

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8001/health || exit 1

# Run the application
CMD ["python", "main_server.py"]
