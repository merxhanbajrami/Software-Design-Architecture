FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]