FROM python:3.9.7-alpine3.14

RUN apk update && apk add bash

COPY ./scripts /app/scripts
COPY ./requirements /app/requirements
COPY ./src /app/src
WORKDIR /app/src

RUN pip install --no-cache-dir --disable-pip-version-check -r /app/requirements/requirements.txt

EXPOSE 8005

CMD ["../scripts/app-command.sh"]