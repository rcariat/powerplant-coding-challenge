# Robin Cariat's powerplant coding challenge


## Preconditions:

- Python 3
- Docker

## Clone the project

```
git clone https://github.com/rcariat/powerplant-coding-challenge.git
```

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload --port 8888
```

### Run test

```
pytest tests/test.py
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest tests/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8888/docs
```
