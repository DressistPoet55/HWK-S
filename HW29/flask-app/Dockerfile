FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD ["python3", "app.py"]