# Use an official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy app files
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port Flask will run on
EXPOSE 5001

# Start the app
CMD ["python", "app.py"]
