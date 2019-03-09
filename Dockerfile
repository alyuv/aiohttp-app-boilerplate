FROM python:3.7.1-alpine3.8

ARG build_version
ENV BUILD_VERSION=${build_version}

RUN apk add --virtual build-deps gcc python3-dev musl-dev build-base linux-headers pcre-dev postgresql-dev && \
    pip3 install --upgrade pip setuptools

# add sources to the image
ADD ./ /aiohttp_app_boilerplate/
WORKDIR /aiohttp_app_boilerplate

ADD ./aiohttp_app_boilerplate/configs/ /etc/aiohttp-app-boilerplate

# python requirements
RUN pip3 install -r requirements/base.txt -r requirements/dev.txt -r requirements/test.txt
RUN pip3 install -e .

CMD aiohttp-app-boilerplate-service