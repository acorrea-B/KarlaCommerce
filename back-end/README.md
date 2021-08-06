```
 Virtual env
```

pipenv install
pipenv shell

```
 Migrate BD
```

python manage.py makemigrations
python manage.py migrate

```
 Create Super User
```

python manage.py createsuperuser --identification 1234 --user_type 1

```
 Load Product Data
```

python manage.py loaddata db.json

```
 Run serve
```

python manage.py runserver
