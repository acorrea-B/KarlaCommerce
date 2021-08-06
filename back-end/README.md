Django requires postgres to run correctly in case you don't have postgres installed, change the database in the settings.py comment out the default database and talk about the sqllite database.

Virtual env

```
pipenv install
```

````
pipenv shell
```


 Migrate BD
```
python manage.py makemigrations
```

````

python manage.py migrate

````


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
````
