FROM python:3.7

# copy all files
RUN mkdir server
COPY ./Server.py /server
COPY ./test_server.py /server
WORKDIR /server

# install required libraries


EXPOSE 11001

CMD ["python", "Server.py"]

