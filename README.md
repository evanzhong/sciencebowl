# sciencebowl

A question bank application for Science Bowl created by Albany High School students and alums.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/andimus/sciencebowl
$ cd sciencebowl

$ pip install -r requirements.txt

$ createdb sciencebowl

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Admin Functionality
Python has some nice built in admin functionality we can use to edit the DB.

Create a superuser
```
$ python manage.py createsuperuser
```

You should be able to use the admin page at: [http://localhost:5000/admin](http://localhost:5000/admin)

Note: don't forget to add new tables to `admin.py` to be able to edit them.

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
