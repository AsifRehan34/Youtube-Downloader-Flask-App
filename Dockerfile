# Use an official Python runtime as a base image
FROM python:3.10.12

# Set the working directory
WORKDIR /app/backend

# Copy the requirements file into the container
COPY requirements.txt /app/backend

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/backend

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 to allow external access
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
