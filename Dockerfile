FROM python:3.7

# copy all files
RUN mkdir server
COPY . /server
WORKDIR /server

# install required libraries


EXPOSE 11001

CMD ["python", "Server.py"]

