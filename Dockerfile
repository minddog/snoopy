FROM ubuntu:trusty
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip

# Define working directory.
WORKDIR /data

COPY . /data
RUN cd /data 
RUN sudo pip install virtualenv
RUN virtualenv /data/.venv
RUN source venv/bin/activate; python setup.py install
EXPOSE  8080
CMD ["python", "server.py"]
