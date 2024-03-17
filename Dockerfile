FROM python:latest

WORKDIR /app

COPY src /app/
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    pandoc \
    cmake \
    protobuf-compiler \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0

