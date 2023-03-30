FROM nginx:stable-alpine-slim
COPY src/default.conf /etc/nginx/conf.d/
RUN mkdir -p /opt/nginx/images
COPY src/images /opt/nginx/images
COPY src/flag.txt /opt/nginx/flag.txt
CMD ["nginx", "-g", "daemon off;"]