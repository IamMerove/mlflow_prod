FROM python:3.10-slim

WORKDIR /app

# Copie et installation des dépendances en premier (cache efficace)
COPY src/front/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code
COPY src/front/app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false"]