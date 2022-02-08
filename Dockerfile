FROM python:3.7
# para no tener error con la version psycopg2==2.9.1 no utilizo una imagen slim o alpine
WORKDIR /app

COPY ["requeriments.txt" ,  "/app/"]

RUN pip install -r requeriments.txt

COPY ["." ,  "/app/"]

EXPOSE 8000