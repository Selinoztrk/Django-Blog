# Django Blog Application

A feature-rich blog application built with Django that allows users to create, edit, and manage blog posts with user authentication and profile management.

---

## Features

- User Authentication (Register, Login, Logout)
- User Profile Management
- Blog Post Creation and Management
- Article Commenting System
- Rich Text Editor for Blog Posts
- Password Change Functionality
- Responsive Design with Bootstrap 5
- Profile Page Customization

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

---

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd BlogApp
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

---

## Project Structure

- `blog/` - Main application directory
  - `members/` - User authentication and profile management
  - `blog_app/` - Core blog functionality and models
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
  - `media/` - User-uploaded media files

---

## Usage

1. Register a new account or login with existing credentials
2. Create and customize your profile
3. Start creating blog posts
4. Manage your posts and profile settings

---

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
