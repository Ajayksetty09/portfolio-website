# Portfolio Website

A personal portfolio website built with Django to showcase projects, skills, and professional information.

## Features

* Home Page
* About Me Section
* Skills Showcase
* Projects Portfolio
* Contact Form
* Admin Dashboard for Content Management
* Responsive Design
* Secure Environment Variable Configuration

## Tech Stack

* Python
* Django
* HTML
* CSS
* SQLite (Development)
* Git & GitHub

## Project Structure

```text
portfolio-website/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .env
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/
├── media/
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Ajayksetty09/portfolio-website.git
cd portfolio-website
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

## GitHub Repository

Repository Link:

https://github.com/Ajayksetty09/portfolio-website

## Future Improvements

* Blog Section
* Project Filtering
* Resume Download Feature
* Dark Mode
* Deployment on Render/AWS

## Author

Ajay Krishnamsetty

GitHub:
https://github.com/Ajayksetty09
