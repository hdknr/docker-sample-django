FROM python:3.8.3
WORKDIR /usr/src/app/web

ENV APP_HOME=/usr/src/web
## COPY
COPY . /usr/src/app

RUN mkdir -p $APP_HOME && \
    mkdir $APP_HOME/static && \
    mkdir $APP_HOME/media

## nginx
RUN apt-get update 
RUN apt-get install nginx -y
COPY ./docker/deployment/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
RUN unlink /etc/nginx/sites-enabled/default
EXPOSE 80

## Python Django
ENV POETRY_VERSION=1.0.10 \
    PATH="/root/.poetry/bin:$PATH"

RUN pip install mysqlclient

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/${POETRY_VERSION}/get-poetry.py | python && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml /usr/src/app/pyproject.toml

RUN poetry install
RUN mkdir -p /var/run/gunicorn
RUN chmod +x /usr/src/app/docker/deployment/entrypoint.sh

# CMD /usr/src/app/docker/deployment/entrypoint.sh hello-container-1
CMD ["/usr/src/app/docker/deployment/entrypoint.sh"]
