FROM python:3.10-slim

WORKDIR /app

# Copy backend requirements
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/app.py .

# Copy frontend files
COPY frontend ./frontend

EXPOSE 5000

CMD ["python", "app.py"]
