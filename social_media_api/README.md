# Social Media API

This project is a Django-based Social Media API that includes user authentication and initial user models. It is designed to provide a platform for user registration, login, and profile management.

## Project Structure

```
social_media_api/
├── social_media_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd social_media_api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install django djangorestframework
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

## User Authentication

The API supports user registration and authentication. Users can register by providing their username, email, and password. After registration, they can log in to obtain an authentication token.

## User Model

The custom user model extends Django’s `AbstractUser` and includes additional fields such as:
- `bio`: A short biography of the user.
- `profile_picture`: A URL or path to the user's profile picture.
- `followers`: A list of users that follow this user.

## API Endpoints

- **Registration:** `/api/users/register/`
- **Login:** `/api/users/login/`
- **User Profile:** `/api/users/profile/`

## Testing

To run tests for the users app, use the following command:
```
python manage.py test users
```

## License

This project is licensed under the MIT License.