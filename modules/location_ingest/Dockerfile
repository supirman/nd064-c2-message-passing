FROM quay.io/basisai/python-alpine-grpcio:3.8.10-1.39.0

WORKDIR .

RUN apk add --no-cache libstdc++

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python", "main.py"]