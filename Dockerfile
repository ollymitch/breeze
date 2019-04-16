FROM python:latest
RUN apt-get update -y

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 2418
ENTRYPOINT ["python"]
CMD ["app.py"]