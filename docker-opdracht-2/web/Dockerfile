FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
HEALTHCHECK CMD curl --fail http://localhost/ || exit 1