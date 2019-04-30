FROM python:2.7-alpine
RUN apk add --no-cache bash gcc libc-dev mariadb-dev --update-cache gcc jpeg-dev zlib-dev python-dev py-pip libpng-dev

ENV PYTHONUNBUFFERED 1
ENV WEBAPP_DIR=/Sistema
WORKDIR $WEBAPP_DIR
ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt
ADD . $WEBAPP_DIR/

