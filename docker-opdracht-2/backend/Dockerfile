FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
HEALTHCHECK CMD curl --fail http://localhost:5000/api/health || exit 1

CMD ["python", "app.py"]