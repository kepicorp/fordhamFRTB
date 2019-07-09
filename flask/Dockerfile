FROM ubuntu:latest
RUN apt-get update && apt-get install -y software-properties-common && apt-add-repository universe && apt-get update && apt-get install -y python-pip
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]