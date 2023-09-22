FROM 3.11-bullseye
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]