

# Task Manager Website

A site that will allow the user to create tasks & notes


## To-Do:

    * [x] Get Django up and running
    * [x] Create a landing page
    * [ ] Create database models
        * [ ] Add auto datetime to tasks/sub/comments 
        * [ ] Add magic methods for all models ( i.e., __str__, __repr__ )






## Possible front-end frameworks:

* Bootstrap


## Database:

* SQLite for development
* PostgreSQL for deployment?

settings.py:
```python

    DATABASES = {
            'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': 'dbname',
                    'USER': os.environ.get('DB_USER'),
                    'PASSWORD': os.environ.get('DB_PASS'),
                    'HOST': os.environ.get('DB_HOST'),
                    'PORT': '1234',
                }
        }
```


## Deployment:

* Heroku 
* AWS
* linode
* Apache with mod_wsgi (docs recommended)


## Django Cmds:

    * django-admin startproject <project_name>  <- Initialize a django project
    * python manage.py runserver                <- Start live server
    * python manage.py startapp <app_name>      <- Make an app in the django project
    * python manage.py makemigrations           <- Preps database for migrations
    * python manage.py migrate                  <- Execute migrations & update database
    * python manage.py createsuperuser          <- Create user in DB with admin privs


---------------------


## Notes

### URL Paths
Make a URL by modifying urls.py, adding to the `urlpatterns` list.

    ```python 
    from django.urls import path
    from . import views

    urlpatterns = [
        path('home/', views.profileView)  # Set URL route and assign associated view.
    ]
    ```

### DB and ORM

Models: class-based representations of DB objects.

#### Defining a model

    ```python
    class Project(models.Model):
        title = models.charField()
        description = models.TextField()
        id = models.UUIDField()
    ```

#### Model Object Creation

    ```python
    class UserForm(ModelForm):
        class Meta:
            model = User
            fields = '__all__'

    class UserCreate(CreateView):
        model = User
        fields = ['username', 'email', 'password']
    ```


#### Querying

Querying Django's ORM DB:

    ```python
    item = ModelName.objects.get(id=1)
    queryset = ModelName.objects.all()
    queryset = ModelNale.objects.filter()
    ```

##### Django DB queries with the django shell (python interpreter within the django project)

```shell     
    `python manage.py shell`
    # Import the models
    >>> from users.models import (model)
    >>> from django.contrib.auth.models import User
    # Make some queries
    >>> User.objects.all()
    <QuerySet [<User: admin>, etc]>
    >>> User.objects.first()/.last()
    >>> User.objects.filter(username='admin')
    <QuerySet [<User: admin>]>
    >>> User.objects.filter(username='admin').first()
    <User: admin>
    >>> user = User.objects.filter(username='admin').first()
    >>> # That user object is now stored in the `user` variable.
    >>> user.id; user.pk # primary key; 

##### Create a task within the django shell
    `python manage.py shell`
    >>> user = User.objects.get(id=1)
    # Create a task (owned by the user) and add it to DB with .save()
    >>> task_1 = Task(title='Do a Thing', subtitle='', body='Do a thing, in a certain way', user=user)
    >>> task_1.save()

##### Get the Many from "One to Many" relationships:
    >>> user.task_set
    >>> user.subtask_set
    >>> user.comment_set
```



Update DB Models:
    `python manage.py makemigrations`
    (optional) check SQL code, using the method below
    `python manage.py migrate`

To view SQL code when migrations are being made: 
    * get migration file (users/migrations/0001_initial.py or smth similar, should be shown after `makemigrations`)
    * python manage.py sqlmigrate blog 0001     Will stdout the SQL query that will be made


#### Create Senders & Receivers (Signals) to response to events

Add event listener for every time a new user registers an account

User Registers -> send() -> Email User
    ^ Sender                    ^ Receiver



#### Django Rest Framework (For backend-only)

terminal
```sh
pip install djangorestframework
```

settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

serializers.py
```python
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
```






# App Filetree Structure

root
│
│─── project_dir/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│
├── users/
│   │
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   │
│   │   ├── registration/  ← Templates used by Django user management
│   │   │
│   │   ├── users/  ← Other templates of your application
│   │   │
│   │   └── base.html  ← The base template of your application
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── db.sqlite3
└── manage.py










DB Schema:

     User
      |
     Tasks, Sub-tasks, comments
      |         |
      |         comments
      |
      Sub-tasks, comments




> Add `Date/time added` fields
> Add `Last Updated`/`Edited` time fields? 

from django.utils import timezone

date_created = models.DateTimeField(default=timezone.now)


once DB tables updated, run `python manage.py makemigrations; python manage.py migrate`
To view SQL code when migrations are being made: 
    * get migration file (users/migrations/0001_initial.py or smth similar)
    * python manage.py sqlmigrate blog 0001     Will stdout the SQL query that will be made



p5=db.ops
















