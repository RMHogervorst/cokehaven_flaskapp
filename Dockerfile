FROM python:3.9.4
RUN mkdir /app
RUN mkdir /app/uploads
WORKDIR /app
COPY . .
COPY templates/ ./templates
COPY static/    ./static
RUN pip install -r requirements.txt

ENV PORT 80
EXPOSE 80

#ENTRYPOINT ["gunicorn", "--timeout", "600","--worker-tmp-dir /dev/shm","--workers=2 --threads=4 --worker-class=gthread","--log-file= - ", "--access-logfile", "'-'", "--error-logfile", "'-'", "--chdir=/app", "flask_app:app"]
ENTRYPOINT ["gunicorn","flask_app:app", "--timeout", "600","--worker-tmp-dir", "/dev/shm","--workers=2", "--threads=4", "--worker-class=gthread", "--log-level=INFO"]