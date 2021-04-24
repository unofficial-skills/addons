FROM andrewstech/alpha-video-baseplate:latest
RUN apk add --no-cache \
        jq=1.6-r1 \
    && curl -J -L -o /tmp/bashio.tar.gz \
        "https://github.com/hassio-addons/bashio/archive/v0.7.1.tar.gz" \
    && mkdir /tmp/bashio \
    && tar zxvf \
        /tmp/bashio.tar.gz \
        --strip 1 -C /tmp/bashio \
    \
    && mv /tmp/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio \
    && rm -fr /tmp/* 
    
RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3 python3-dev git nodejs npm nano wget curl net-tools unzip supervisor jq screen
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
