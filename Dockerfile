FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose ports: FastAPI 8000, Streamlit 8501
EXPOSE 8000 8501

# Run both backend and frontend
CMD bash -c "uvicorn dpred.app:app --host 0.0.0.0 --port 8000 & streamlit run frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0"
