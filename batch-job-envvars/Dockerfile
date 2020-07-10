# Python base image
FROM python:3

RUN pip install requests

# Working directory within container
WORKDIR /usr/app

# Start by copying over the python script
COPY ./ ./

# Start command
CMD python main.py
