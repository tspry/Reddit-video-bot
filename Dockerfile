FROM python:3.10.14-slim

RUN apt update
RUN apt-get install -y ffmpeg
RUN apt install python3-pip -y

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN playwright install --with-deps chromium

CMD ["python3", "main.py"]
