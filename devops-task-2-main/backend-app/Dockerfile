FROM python:3.12-alpine

WORKDIR /app

# Install dependencies
RUN apk add python3-dev gcc libc-dev libffi-dev

# Copy requirements and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the REDIS_URI environment variable
# Make sure this matches your Redis service name
ENV REDIS_URI=redis://redis-svc:6379


# Expose port 8080
EXPOSE 8080

# Start the application using FastAPI
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8080"]
