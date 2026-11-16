FROM python:3.12-slim

WORKDIR /app

# Instalace závislost nejdřív – vrstva se znovu použije, pokud se změní jen kód
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/

# Výchozí port uvnitř kontejneru (app.py umí číst i FLASK_PORT)
ENV FLASK_PORT=5052

EXPOSE 5052

CMD ["python", "app.py"]
