

# dj-blog - Django Blog Website (MyBlog)

---

## About

MyBlog is a simple blog website built with Django and Bootstrap 5.  
It features user registration, login/logout, post creation.

---

---

## Features

- User registration and login with authentication
- Create, view blog posts with slug-based URLs
- Responsive Bootstrap 5 design with navbar, search
- Post detail page requires login
- Secure logout with POST method

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/hasdajustin/dj-blog.git
cd blogProject
```

2. **Setting Up the SECRET_KEY in `.env` File**
**Run this command in your terminal:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
- paste the secret_key in .env file

3. **Create and activate virtual environment:**
```bash
python -m venv env
env\Scripts\activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Apply migrations:**
```bash
python manage.py migrate
```

6. **Create superuser:**
```bash
python manage.py createsuperuser
```

7. **Run the development server:**
```bash
python manage.py runserver
```
