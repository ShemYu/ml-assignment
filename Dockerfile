FROM wallies/python-cuda:3.10-cuda11.6-runtime

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --timeout 150 -r app/requirements.txt
RUN python app/utils/load_model.py

ENTRYPOINT [ "sh", "bin/entrypoint.sh", "--reload" ]