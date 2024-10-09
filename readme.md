# To-Do List Application

This is a simple To-Do List web application built with Django. It allows users to manage their daily tasks effectively. Users can add, complete, and delete tasks. The application also supports user registration, login, and logout functionalities.

## Features

- User registration and login
- Add tasks
- Complete tasks
- Delete tasks
- Logout


## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MacroXie04/TODO-list.git
   cd TODO-list
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
    Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv\Scripts\activate
        ```

3. **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py makemigrations index
    python manage.py migrate
   ```
   
5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Visit http://127.0.0.1:8000/ or http://localhost:8000/ in your web browser.**

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.