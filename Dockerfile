FROM python:3.6-alpine
LABEL AUTHOR=avneesh.srivastava@gmail.com
ENV http_proxy=$http_proxy
ENV https_proxy=$http_proxy
ENV HTTPS_PROXY=$http_proxy
ENV HTTP_PROXY=$http_proxy
COPY . /usr/app
WORKDIR /usr/app
RUN ["pip","install","-r","/requirements.txt"]
ENTRYPOINT ["/bin/sh","/start-api.sh"]