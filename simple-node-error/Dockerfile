# Base image
FROM node:alpine

# Working directory within container
WORKDIR /usr/app

# Start by copying over the package.json file
COPY ./package.json ./

# Install node dependencies listed in package.json
RUN npm install

# Copy all files from local machine (build context, supplied at docker build)
# to container inside working directory
COPY ./ ./

# Start command
CMD npm start
