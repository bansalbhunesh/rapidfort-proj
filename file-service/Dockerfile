FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y libjpeg-dev zlib1g-dev wkhtmltopdf && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the application
COPY . .

# Create uploads directory
RUN mkdir -p uploads

EXPOSE 4003

CMD ["python", "server.py"]