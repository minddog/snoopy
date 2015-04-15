FROM spotify/kafka

RUN apt-get install python -y

# Define working directory.
WORKDIR /data

COPY . /data
RUN cd /data; python setup.py install
EXPOSE  8080
CMD ["python", "server.py"]
