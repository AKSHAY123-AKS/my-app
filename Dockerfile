# Use base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 5000

# Copy source code
COPY . .

# Install dependencies
RUN pip install flask

# Run the app
CMD ["python", "app.py"]
