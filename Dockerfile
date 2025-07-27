# Use slim base Python image
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY main.py .

# Create input/output folders
RUN mkdir input output

# Entry point
CMD ["python", "main.py"]
