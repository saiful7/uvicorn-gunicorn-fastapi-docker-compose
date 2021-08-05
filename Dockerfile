FROM tiangolo/uvicorn-gunicorn-fastapi

#COPY requirements.txt /app/requirements.txt
COPY ./app /app

WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app
#CMD ["uvicorn","app-test:app","--host","167.86.83.81","--port","80"]
