FROM python:3.12.2-alpine3.19
WORKDIR /app
RUN addgroup -g 1000 api && \ 
    adduser -u 1000 -G api -D dbuser
COPY requirements.txt .
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev libpq-dev && \
    pip3 install --no-cache-dir -r requirements.txt
COPY main.py config.py wait-for-it.sh docker-entrypoint.sh .
RUN chown -R dbuser:api /app
USER dbuser
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python3", "main.py"]
EXPOSE 5000

