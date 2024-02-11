# Miso

![Banner Image](./842269_Generate%20a%20banner%20image%20for%20a%20website%20for%20its%20bran_xl-1024-v1-0.png)

## Description

A expense tracker for real estate properties, in active development stage

## Installation

### From source

1. Install dependicies in the requirements.txt file

2. Setup the ```.env``` file with your secret key. Should look something like this:

  ```text
    SECRET_KEY="mysecretkey"
  ```

3. Start the Django server

  ```bash
  gunicorn --workers 2 miso.wsgi
  ```

4. Create a superuser to login to the admin console.

  ```python
  python manage.py createsuperuser
  ```

5. Login to the admin interface by going to [http://localhost:8000/admin](http://localhost:8000/admin).

### Docker

1. Clone the repo:

  ```bash
  git clone https://github.com/impulsive-sudor/Miso.git
  ```

2. Create a .env file in the root directory:

  ```bash
  touch .env
  ```

3. Add the environmental variables to the file. Make sure to change the password from the defaults.

  ```text
  SECRET_KEY="mysecretkey"
  POSTGRES_DB="postgres"
  POSTGRES_USER="postgres"
  POSTGRES_PASSWORD="postgres"
  ```

4. Run the command `docker-compose up` to get the application running. You might need to run this command twice to ensure the connection between the Django app and Postgres is made.

5. Create a superuser in the Django app.

  ```bash
  docker exec -it <container_id> python manage.py createsuperuser
  ```

6. Login to the admin interface by going to [http://localhost/admin](http://localhost/admin).

## Usage

This project is in very early stages, so please be mindful of the constant changes I will be doing.

Currently there is no forms built into the website. All the website does today is display the results from the DB. To submit data, I'm currently using the Django admin interface. This isn't ideal but it's a starting point for me to get up and running.

## Contributing

Guidelines for contributing to your project.

## License

Information about the license.
