FROM downloads.unstructured.io/unstructured-io/unstructured:latest

WORKDIR /app

COPY src /app/
# RUN apt-get update && apt-get install -y \
#     libmagic-dev \
#     poppler-utils \
#     tesseract-ocr \
#     tesseract-ocr-eng \
#     libreoffice \
#     pandoc \
#     cmake \
#     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0

