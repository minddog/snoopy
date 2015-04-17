FROM ubuntu:trusty
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip

# Define working directory.
WORKDIR /data

COPY . /data
RUN cd /data 
RUN sudo pip install virtualenv
RUN virtualenv /data/.venv
RUN /data/.venv/bin/pip install -r requirements.txt
RUN /data/.venv/bin/python setup.py install 
EXPOSE  5000
CMD ["/data/.venv/bin/python", "server.py"]
