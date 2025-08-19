# News Application

## Description
This is a web-based platform, built with Django framework which allows users to register as journalist and be able to create, publish, and interact with articles and newsletters register as general readers.

## Requirements
### Requirements for manual setup with virtual environments
* Python 3.10+
* MariaDB
* Twitter / X Developer accounts

### Requirements for Docker setup
* Docker 
* Docker Compose
* Twitter / X Developer accounts

## Setup and Installation

### 1. Clone the repository
* Using HTTPS:
```bash
git clone https://github.com/Lauvenia/news-app.git
```

* Using SSH:
```bash
git clone git@github.com:Lauvenia/news-app.git
```

### 2. Navigate into the repository directory

```bash
cd news-app
```

### 3. Setting up the environmental variables
1. Rename the .env.template file to .env
2. Update the values for the environmental variables

### 4. Select the setup method

* Virtual Environment
    1. Create a virtual environment
    ```bash
    python -m venv env
    ```

    2. Activate your virtual environment
        * Windows:
        ```bash
        .\env\Scripts\activate
        ```

        * Linux / MacOS:
        ```bash
        source env/bin/activate
        ```

    3. Install project dependencies
    ```bash
    pip install -r requirements.txt
    ```

    4. Configure MariaDB to align with environmental variables
    5. Apply migrations to database
    ```bash
    python manage.py migrate
    ```
    6. Run the server
    ```bash
    python manage.py runserver
    ```

* Docker & Docker Compose
1. Build and start container
```bash
docker-compose up --build
```

### 5. Visit the webpage
* Navigate to [127.0.0.1:8000/](127.0.0.1:8000/) in the browser to view the homepage.



