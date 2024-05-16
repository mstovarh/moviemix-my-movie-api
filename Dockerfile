FROM python:3.12.3
WORKDIR /my-movie-api
COPY requirements.txt /my-movie-api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /my-movie-api/requirements.txt
COPY . /my-movie-api
CMD bash -c "while true; do sleep 1; done"