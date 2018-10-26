FROM flashlinks/nodejs

# Create app directory
WORKDIR /usr/src/app

# Copy app code
COPY package.json .
COPY app.js .

# Install dependencies
RUN npm install

#start app
CMD [ "npm", "start" ]
