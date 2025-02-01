![Badge](https://img.shields.io/badge/python-3.12.2-green.svg)
![Badge](https://img.shields.io/badge/django-5.1-green.svg)

# Installation

```bash
$ git clone https://github.com/mrthkc/bumper_task.git
$ cd bumper_task
$ python3.12 -m venv venv
$ ./venv/bin/python3.12 -m pip install -r requirements.txt
$ export ENVIRONMENT=development SECRET_KEY='oow961_))c@35gsjl_kox=npa@5k!)hg^et-$5e*_y^)ah1o(7' DB_HOST=localhost DB_NAME=guestbook DB_USER=db_user DB_PASSWORD=****
$ ./venv/bin/python3.12 manage.py migrate
$ ./venv/bin/python3.12 manage.py runserver
```

# Tests
```bash
$ ./venv/bin/python manage.py test guestbook.tests -v 2
```