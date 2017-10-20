# Si Hay Build

A naive CI implementation made in django.

### Installation
1. Use pip to install requirements.
```
pip install -r requirements.txt
```
2. Run migrations
```
./manage.py migrate
```
3. Run server
```
./manage.py runserver
```

### Usage
*NOTE:* This version requires that you SSH into the server and install the
dependencies needed for your projects to run.

*NOTE:* You also need to clone the repos before running tests
```
./manage.py shell
>>> from webhooks import repos
>>> repos.install('GIT_URL_FOR_REPO')
```

Before starting, create an admin user
```
./manage.py createsuperuser
```

Once the server is running, enter `localhost:8000/admin/`, and configure your
repos and pipelines.

After that, enter your repo settings in github and add a webhook pointing to
`<SERVER_URL>/webhooks`.

And thats it!
