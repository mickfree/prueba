FROM python:3.12.6

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copia y instala las dependencias
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Expone el puerto 8080
EXPOSE 8080

# Comando para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
