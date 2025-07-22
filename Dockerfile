FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# backup and restore
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy and install the requirements into the container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

RUN chmod +x run.sh

# Expose the port the app runs on
EXPOSE 8000