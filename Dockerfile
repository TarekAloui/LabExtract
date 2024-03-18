FROM downloads.unstructured.io/unstructured-io/unstructured:latest

WORKDIR /app

COPY src /app/

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0 --workers=4

