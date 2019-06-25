FROM python:slim-stretch

LABEL maintainer="Pablo Vargas <pablovargasjr@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./application.py" ]