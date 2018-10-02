FROM flashlinks/nodejs

ARG LINKS_API_HOST
ENV LINKS_API_HOST=$LINKS_API_HOST

ARG LINKS_API_PORT
ENV LINKS_API_PORT=$LINKS_API_PORT

# Create app directory
WORKDIR /usr/src/app

COPY package.json .
COPY bower.json .

# Install dependencies
RUN npm install
RUN npm run bower

# Copy app code
COPY src/ ./src
COPY app.js .

# Create env.js
RUN envsubst < ./src/js/env.js.tmpl > ./src/js/env.js

#start app
CMD [ "npm", "start" ]
