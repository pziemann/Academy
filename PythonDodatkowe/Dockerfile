# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY requirements.txt web-checker.py ./

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set execute permission for the script
RUN chmod +x web-checker.py

# Specify the command to run the script
CMD ["python", "web-checker.py"]
