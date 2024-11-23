#!/bin/bash

echo "Building Docker images for frontend and backend..."

# Build backend Docker image
docker build -t docx-to-pdf-converter-backend ./file-service

# Build frontend Docker image
docker build -t docx-to-pdf-converter-frontend ./frontend

echo "Running containers..."

# Run backend container
docker run -d -p 4003:4003 docx-to-pdf-converter-backend

# Run frontend container
docker run -d -p 3000:3000 docx-to-pdf-converter-frontend

echo "Containers are running!"
