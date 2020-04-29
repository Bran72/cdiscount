FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pwd
VOLUME /app
WORKDIR /app
ADD . /app

RUN pip3 install flask requests BeautifulSoup4 waitress /app/dist/cdiscount-1.0.0-py3-none-any.whl
ENTRYPOINT ["python3"]
CMD ["website/website.py"]