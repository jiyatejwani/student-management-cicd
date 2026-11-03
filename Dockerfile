# Small official Python base image
FROM python:3.12-slim

# Work inside /app in the container
WORKDIR /app

# Install dependencies first so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ ./app/
COPY wsgi.py .

# The port the app listens on
EXPOSE 5000

# Start the app with gunicorn (a production web server), 2 workers
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "wsgi:app"]
