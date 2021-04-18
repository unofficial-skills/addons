ARG BUILD_FROM
FROM $BUILD_FROM
WORKDIR /app
COPY run.sh run.sh
RUN chmod 777 run.sh
COPY . /app
EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP=main.py
RUN chmod 777 /app/run.sh
COPY supervisord.conf /etc/supervisor/supervisord.conf
ENTRYPOINT ["./run.sh"]
