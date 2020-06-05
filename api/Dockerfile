FROM alpine:latest

RUN apk add --no-cache python3-dev \
&& pip3 install --upgrade pip

WORKDIR /usr/src/api

COPY . /usr/src/api

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python3", "api.py"]

