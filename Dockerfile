# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables for OpenAI API key
ENV OPENAI_API_KEY "YOUR_API_KEY"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "streamlit_document_generator.py"]
