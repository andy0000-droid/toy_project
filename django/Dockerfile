FROM python:3.11.9
WORKDIR /app
copy ./django/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .