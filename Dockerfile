FROM python:3.10-slim
WORKDIR /YAMLAPP
RUN pip install flask
COPY app.py .
EXPOSE 9000
CMD ["python", "app.py"]