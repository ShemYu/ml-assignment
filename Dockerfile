FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --timeout 150 -r app/requirements.txt
EXPOSE 9527
ENTRYPOINT [ "sh", "bin/entrypoint.sh"]