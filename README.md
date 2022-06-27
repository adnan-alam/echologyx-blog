# Echologyx Blog

### Requirements

- Python 3.8 or 3.8+

### Project setup

- Clone the repository:

  ```bash
  git clone git@github.com:adnan-alam/echologyx-blog.git
  ```

- Create a **.env** file inside the project directory and copy from **env_example** to **.env** and set the environment variables according to the needs.

  ```bash
  # example
  DJANGO_SECRET_KEY=a secure secret key
  SQLITE_DATABASE_NAME=example_db.sqlite3
  ```

- Create a virtual environment named **env** with Python's **venv**:

  ```bash
  python3.8 -m venv env
  ```

  - Activate the virtual environment (For Ubuntu):
    ```bash
    source env/bin/activate
    ```

- Install all required packages:

  ```bash
  pip install -r requirements.txt
  ```

- Run **migrate** command to propagate the migrations files into the db

  ```bash
  python manage.py migrate
  ```

- Create admin account

  ```
  python manage.py createsuperuser
  ```

- Run Django server

  ```bash
  python manage.py runserver ip_address:port
  ```

- Change the default Domain of Site. Go to `http://ip_address:port/admin/`, login as admin and navigate to **Sites**. Change the Domain to **ip_address:port**.

### Makefile

- Delete `.pyc` files with the command:

  ```bash
  make clean
  ```
