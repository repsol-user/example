FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3-dev python3-pip
RUN python3 -m pip install -U pip
ADD foobar/ /root/foobar
ADD requirements.txt /root/requirements.txt
ENV PYTHONPATH=/root
RUN python3 -m pip install -r /root/requirements.txt
CMD python3 -m foobar
