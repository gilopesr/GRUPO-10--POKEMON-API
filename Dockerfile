FROM python:3.10-slim

WORKDIR /GRUPO-10--POKEMON-API

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "/GRUPO-10--POKEMON-API/app.py"]

