# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

COPY requirements.txt .

# Install Dependancy
RUN pip install --upgrade pip
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

# Copy code from source to destonation
COPY . .

# Expose port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]
