FROM python:3.10-slim

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --timeout 150 -r app/requirements.txt
RUN python app/utils/load_model.py
EXPOSE 9527
ENTRYPOINT [ "sh", "bin/entrypoint.sh"]