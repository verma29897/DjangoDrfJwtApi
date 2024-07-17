# DjangoDrfJwtApi
Django Blog Application
# Django Blog Application

This is a simple blog application built with Django and Django REST Framework, integrating basic CRUD functionalities.

## Features

- User authentication with JWT tokens
- CRUD operations for posts and comments
- Token-based authentication for creating, updating, and deleting posts and comments
- Optional React frontend

## Installation

1. Clone the repository:
   git clone https://github.com/verma29897/DjangoDrfJwtApi.git
   cd django-blog

Create and activate a virtual environment:
pip install pipenv shell
pipenv shell

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


## API Endpoints
Authentication
POST /api/token/
## Refresh Token:
POST /api/token/refresh/

## List/Create Posts:
GET/POST /api/posts/
## Retrieve/Update/Delete Post:
GET/PUT/DELETE /api/posts/{id}/
## Comments
List/Create Comments for a Post:
GET/POST /api/posts/{post_id}/comments/


