FROM python:alpine as base
WORKDIR /tmp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /src
WORKDIR /src
COPY . /src/.
CMD ["python", "-u", "main.py"]