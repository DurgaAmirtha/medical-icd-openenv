FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set default environment variables
ENV API_BASE_URL="https://api.openai.com/v1"
ENV MODEL_NAME="gpt-3.5-turbo"
ENV HF_TOKEN="dummy"

# Run inference by default
CMD ["python", "inference.py"]
