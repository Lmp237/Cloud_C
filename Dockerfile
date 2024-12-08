FROM python:3.7-slim
RUN mkdir -p /app & \
    mkdir -p /app/templates & \
    mkdir -p /app/static
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY web/static /app/static/
COPY web/templates /app/templates/
COPY web/requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY web/app.py web/dbconnect.py /app/
ENTRYPOINT ["python","app.py"]
