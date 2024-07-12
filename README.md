# Flask RESTful Routing

## Learning Goals (Part One)

- Using the flask_restful library

## Getting Started

```bash
pipenv install
pipenv shell

cd server

flask db init
flask db migrate -m "create sports table"
flask db upgrade

python seed.py

python app.py
```

## RESTful Routes

!["restful routes chart"](assets/restful-routes.png)

## MVC Architecture

!["model view controller chart"](assets/mvc.png)