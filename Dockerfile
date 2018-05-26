FROM python:2.7-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PROJECT_DIR /mnt
CMD ./scripts/run.sh -h
