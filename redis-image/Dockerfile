# Use existing docker image as base
FROM alpine

# Download and install dependencies
RUN apk add --update redis

# Configure start command
CMD [ "redis-server" ]

