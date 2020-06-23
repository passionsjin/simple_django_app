FROM nginx
RUN rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443

# Is this even the right command I have no idea

CMD ["nginx", "-g", "daemon off;"]