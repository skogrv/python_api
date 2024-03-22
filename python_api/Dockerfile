FROM python:3.12.2-alpine3.19
WORKDIR /app
# RUN addgroup -g 1000 dbuser && \ 
#     adduser -u 1000 -G dbuser -D dbuser
COPY requirements.txt .
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libpq-dev
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY main.py config.py wait-for-it.sh docker-entrypoint.sh .
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python3", "main.py"]
EXPOSE 5000

