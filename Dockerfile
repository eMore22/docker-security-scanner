# Use Python slim image for smaller size
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install --no-cache-dir requests

# Copy scanner script
COPY scanner.py .

# Make script executable
RUN chmod +x scanner.py

# Set entrypoint
ENTRYPOINT ["python", "scanner.py"]