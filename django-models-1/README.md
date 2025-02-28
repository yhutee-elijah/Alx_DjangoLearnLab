# django-models

This project demonstrates advanced model relationships in Django using ForeignKey, ManyToMany, and OneToOne fields. 

## Project Structure

```
django-models
├── relationship_app
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── django_models
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd django-models
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install django
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

7. **Access the admin panel:**
   Navigate to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

## Overview

The `relationship_app` contains models that illustrate various relationships:

- **Author**: Represents an author with a name.
- **Book**: Represents a book with a title and a foreign key to the Author.
- **Library**: Represents a library with a name and a many-to-many relationship with Books.
- **Librarian**: Represents a librarian with a name and a one-to-one relationship with a Library.

This project serves as a practical example of how to implement and manage complex relationships in Django models.