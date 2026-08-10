# Używamy lekkiego obrazu Pythona
FROM python:3.11-slim

# Tworzymy katalog roboczy wewnątrz kontenera
WORKDIR /app

# Kopiujemy plik z bibliotekami i instalujemy boto3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy nasz kod do kontenera
COPY app.py .

# Tworzymy folder na pliki wyjściowe
RUN mkdir -p /app/output

# Domyślna komenda uruchamiana po starcie kontenera
CMD ["python", "app.py"]