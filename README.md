# Django CRUD Application

This is a simple Django-based CRUD application built to demonstrate:

- Create, Read, Update, Delete (CRUD) operations using REST-style APIs
- PostgreSQL database using Supabase
- Third-party API integration
- Data visualization using Chart.js
- HTML and JavaScript frontend served by Django

---

## Features

- Add, view, update, and delete products
- PostgreSQL database hosted on Supabase
- External API data fetched and displayed on the UI
- Chart.js bar chart showing product prices
- Clean and simple user interface

---

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: PostgreSQL (Supabase)
- Charts: Chart.js

## How to Run the Project Locally

<<<<<<< HEAD
1. Create a virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
=======
1. Create a virtual environment<br>
python -m venv venv<br>
venv\Scripts\activate

2. Install dependencies<br>
>>>>>>> 008f26853e51a00217ff5a91a1721e37e05c4f8b
pip install django psycopg2-binary requests

---

## Database Configuration (Supabase)

<<<<<<< HEAD
Update settings.py with your Supabase PostgreSQL credentials:
=======
Update settings.py with your Supabase PostgreSQL credentials:<br><br>
>>>>>>> 008f26853e51a00217ff5a91a1721e37e05c4f8b

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.dboumksfmrvhuilylrqr',
        'PASSWORD': 'YOUR_SUPABASE_PASSWORD',
        'HOST': 'aws-1-ap-southeast-1.pooler.supabase.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

---

## Run Migrations

<<<<<<< HEAD
python manage.py makemigrations
=======
python manage.py makemigrations<br>
>>>>>>> 008f26853e51a00217ff5a91a1721e37e05c4f8b
python manage.py migrate

---

## Start the Server

python manage.py runserver

Open in browser:
http://127.0.0.1:8000/api/

http://127.0.0.1:8000/api/chart/

## API Endpoints

- GET /api/list/ – List products
- POST /api/create/ – Create product
- PUT /api/update/<id>/ – Update product
- DELETE /api/delete/<id>/ – Delete product
- GET /api/report/ – Chart data
- GET /api/external/ – External API data
- GET /api/chart/ – Chart page

## Author

Rohit Tulshiramji Gujarkar
