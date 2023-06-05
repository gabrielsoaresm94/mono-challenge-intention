FROM python:3.9
COPY requirements.txt /
COPY run_migrations.sh /

# RUN pip install -r /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app
WORKDIR /app

EXPOSE 5000

# RUN chmod +x /run_migrations.sh
# RUN /run_migrations.sh

CMD [ "python", "./app.py" ]
