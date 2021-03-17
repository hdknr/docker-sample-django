FROM python:3.8.3
WORKDIR /usr/src/app/web

## COPY
COPY . /usr/src/app

## SSH
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

## --- SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN mkdir ~/.ssh
RUN echo $SSH_PUBLIC_KEY > ~/.ssh/authorized_keys
#RUN cat ./keys/*.pub >> ~/.ssh/authorized_keys
RUN chmod 0600 ~/.ssh/authorized_keys

EXPOSE 22

## nginx
RUN apt-get install nginx -y
COPY ./docker/deployment/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

## Python Django
ENV POETRY_VERSION=1.0.10 \
    PATH="/root/.poetry/bin:$PATH"

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/${POETRY_VERSION}/get-poetry.py | python && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml /usr/src/app/pyproject.toml

RUN poetry install
RUN mkdir -p /var/run/gunicorn
RUN chmod +x /usr/src/app/docker/deployment/entrypoint.sh

# ENTRYPOINT ["sh", "/usr/src/app/docker/deployment/entrypoint.sh"]
CMD /usr/src/app/docker/deployment/entrypoint.sh hello-container-1
