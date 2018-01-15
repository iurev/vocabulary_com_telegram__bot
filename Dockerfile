FROM python:alpine as base
WORKDIR /tmp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:alpine
RUN mkdir /src
WORKDIR /src
COPY --from=base /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages # copies python packages
