# Basic Django CRUD Application

## Tech Stack
- Python
- Django
- PostgreSQL
- HTML, JavaScript
- Chart.js

## Features
- REST-style CRUD APIs (no serializers, no DRF)
- PostgreSQL database integration
- Third-party API integration (CoinDesk)
- Simple HTML UI for CRUD operations
- Data visualization using Chart.js

## Run Instructions
pip install django psycopg2 requests
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## API Endpoints
POST   /api/create/
GET    /api/list/
PUT    /api/update/<id>/
DELETE /api/delete/<id>/
GET    /api/report/
GET    /api/external/
