# pull official base image
FROM python:3.10

# set work directory
WORKDIR /src

# copy requirements file
COPY ./requirements.txt /src/requirements.txt

# install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /src/requirements.txt

# copy project
COPY . /src/

# Run the uvicorn command, telling it to use the app object imported from app.main
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888"]