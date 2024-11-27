FROM python:3

WORKDIR /src

COPY . /src

EXPOSE 8080

CMD ["python","src/main.py"]