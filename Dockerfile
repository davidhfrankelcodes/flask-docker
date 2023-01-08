FROM python:3.9

WORKDIR /app
# Install the required libraries from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add the Flask app code

COPY . .

# Expose port 5000
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
