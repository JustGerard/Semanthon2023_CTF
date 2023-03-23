FROM debian:buster

WORKDIR /opt/app
RUN mkdir -p /opt/app

COPY src/a.out /opt/app/a.out
RUN chmod +x /opt/app/a.out

ENTRYPOINT ["/opt/app/a.out"]