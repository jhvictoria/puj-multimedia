FROM node:7.10.1-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh gettext curl

WORKDIR /usr/src/app

COPY package.json .
COPY bower.json .

RUN npm install
RUN npm run bower
RUN npm install -g grunt

COPY Gruntfile.js .
