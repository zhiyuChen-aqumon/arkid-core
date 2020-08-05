FROM python:3.6 as build_deps
EXPOSE 80
WORKDIR /var/oneid
RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list &&\
    apt-get update \
    && apt-get install -y --no-install-recommends \
        vim supervisor gettext xmlsec1 \
        python-dev default-libmysqlclient-dev
ADD devops/pip.conf /etc/pip.conf
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

FROM build_deps as run_lint
ADD requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt -i https://mirrors.aliyun.com/pypi/simple/
ADD . .
ARG base_commit_id=""
RUN pre-commit install \
    && make BASE_COMMIT_ID=${base_commit_id} lint

FROM build_deps as run_test
ADD . .
RUN make test

FROM build_deps as build
RUN pip install uwsgi mysqlclient==1.4.6 -i https://mirrors.aliyun.com/pypi/simple/
ADD . .
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
RUN python manage.py compilemessages
CMD python manage.py migrate && supervisord

