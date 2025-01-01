# To-Do List Application

## Overview

This project is a simple To-Do List web application built with **Python** and the **Flask** framework. It allows users to create, edit, and delete tasks in a web-based to-do list. The application is styled using **Bootstrap** for responsiveness and uses **Jinja2** templating for rendering dynamic HTML pages.

## Features

- **Task Management**: Users can add new tasks, edit existing ones, and delete tasks.
- **Database**: The application uses **SQLite** for storing tasks in a simple relational database.
- **Responsive UI**: The front-end is styled with **Bootstrap** for a clean and mobile-friendly user interface.
- **Template Rendering**: The application leverages **Jinja2 templates** to dynamically render task lists and forms.
  
## Technologies Used

- **Python**: The back-end of the application is written in Python using the Flask framework.
- **Flask**: A lightweight Python web framework used to handle routing, HTTP requests, and template rendering.
- **SQLite**: A simple file-based database used to store tasks.
- **Jinja2**: A templating engine used to dynamically generate HTML pages in the Flask application.
- **Bootstrap**: A popular front-end framework for responsive design and styling.
  
## Installation

To run this application locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   

2. Navigate to the project directory:
    ```bash
    cd todo-list-app

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
   
4. Activate the virtual environment:
on Windows:

    ```bash
    venv\Scripts\activate


5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

6. Initialize the database:

    ```bash
    flask shell
    >>> from app import db, Task
    >>> db.create_all()
    >>> exit()

7. Run the application:

    ```bash
    flask run
    Visit http://127.0.0.1:5000 in your browser to view the application.
