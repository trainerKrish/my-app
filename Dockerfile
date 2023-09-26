FROM alpine:latest

# install python
RUN apk add --update --no-cache python3

# install pip
RUN apk add --update --no-cache py3-pip

# copy the requirements
COPY ./requirements.txt ./

# intsalling module
RUN pip3 install -r requirements.txt

# copy remaining file
COPY ./ ./

# run the script
CMD ["python3", "app.py"]


