ARG BUILD_FROM
FROM $BUILD_FROM
RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3 python3-dev git nodejs npm nano wget curl net-tools unzip supervisor screen
WORKDIR /app
RUN pip install -r requirements.txt
COPY run.sh run.sh
RUN chmod 777 run.sh
COPY . /app
EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP=main.py
RUN chmod 777 /app/run.sh
COPY supervisord.conf /etc/supervisor/supervisord.conf
ENTRYPOINT ["./run.sh"]
