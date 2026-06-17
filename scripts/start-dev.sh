#!/bin/bash
# JARVIS OS - Local Development Startup (WSL/Linux)
# Run this from the repository root.

echo "========================================"
echo " JARVIS OS - Development Environment"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "[WARN] .env file not found. Copying from .env.example..."
    cp .env.example .env
    echo "[INFO] Edit .env to add your API keys."
    echo ""
fi

# Start Docker services
echo "[1/3] Starting Docker services (PostgreSQL, Redis, Qdrant)..."
docker compose up -d postgres redis qdrant
echo ""

# Wait for services
echo "[2/3] Waiting for services to be ready..."
sleep 5

# Start backend
echo "[3/3] Starting JARVIS API..."
echo ""
echo "Backend will be available at: http://localhost:8000"
echo "Health check: http://localhost:8000/health"
echo ""
cd apps/api
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
