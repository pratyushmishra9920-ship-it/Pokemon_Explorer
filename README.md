# Pokémon Explorer

Pokémon Explorer is a Flask-based web application that allows users to search for Pokémon and view information fetched from a Pokémon REST API.

This project was built to practice and demonstrate **Python, Flask, REST API consumption, HTTP requests, query parameters, input validation, error handling, HTML templates, and deployment**.

## Features

* Search for Pokémon by name
* Fetch Pokémon information from an external REST API
* Display API data through a web interface
* Use query parameters for user searches
* Input validation
* Error handling for invalid Pokémon
* Dynamic HTML pages using Flask templates
* Static files including images and CSS
* Clean Flask project structure
* Production deployment using Gunicorn

## Tech Stack

* **Python**
* **Flask**
* **Requests**
* **HTML/CSS**
* **Gunicorn**
* **Render**

## Project Structure

```text
Pokemon_Explorer/
│
├── application/
│   ├── static/
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── forms.html
│   │   └── home_page.html
│   ├── __init__.py
│   ├── helper_func.py
│   └── routes.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. The user enters a Pokémon name through the web interface.
2. Flask receives the request.
3. The application sends an HTTP request to the Pokémon REST API using the `requests` library.
4. The API response is processed by the Flask application.
5. The required Pokémon information is passed to the HTML template.
6. The information is displayed to the user.
7. Invalid input and API errors are handled appropriately.

## Run Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd Pokemon_Explorer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

The application will start on the local Flask development server.

## Deployment

The application can be deployed as a production web service using **Gunicorn** and **Render**.

The production start command is:

```bash
gunicorn application:app
```

Here, `application` refers to the Flask package containing `__init__.py`, while `app` refers to the Flask application object created inside it.

## Learning Objectives

This project helped me practice:

* Flask application structure
* REST API consumption
* HTTP requests and responses
* Query parameters
* JSON data handling
* Input validation
* Error handling
* Template rendering
* Static files
* Virtual environments
* Production WSGI servers
* Web application deployment

## Future Improvements

* Add more Pokémon information
* Add additional search and filtering options
* Improve API error responses
* Add caching
* Add automated tests
* Improve the user interface
* Add more API endpoints


