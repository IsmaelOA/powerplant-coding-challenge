# Base image
FROM python:3.11.6-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /usr/src/app

# Copy requirements file and install dependencies
RUN pip install flask requests

# Set PYTHONPATH
ENV PYTHONPATH=/usr/src/app

# Copy application files
COPY . .

# Expose application port
EXPOSE 8888

# Command to run the application
CMD ["python", "main.py"]
