FROM alpine:latest
RUN apk upgrade --no-cache \ 
    && apk add --no-cache \ 
    openssh-client \
    busybox-extras \
    && rm -rf /var/cache/apk/*

ENV TZ JST-9
RUN apk add --update python2 py-pip python2-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pexpect

WORKDIR /work
