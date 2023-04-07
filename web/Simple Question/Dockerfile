FROM node:16-alpine
WORKDIR /usr/src/app
COPY src/ ./

RUN npm install

EXPOSE 8000
ENTRYPOINT ["/usr/src/app/serve.sh"]