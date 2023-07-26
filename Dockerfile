FROM python:3.10-slim

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt
RUN python app/utils/load_model.py

ENTRYPOINT [ "sh", "bin/entrypoint.sh", "--reload" ]