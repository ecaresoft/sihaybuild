# Si Hay Build

A naive CI implementation made in django.

### Installation
1. Use pip to install requirements.
```sh
pip install -r requirements.txt
```
2. Run migrations
```sh
./manage.py migrate
```
3. Run server
```sh
./manage.py runserver
```

### Usage
*NOTE:* This version requires that you SSH into the server and install the
dependencies needed for your projects to run.

*NOTE:* You also need to clone the repos before running tests
```python
./manage.py shell
>>> from webhooks import repos
>>> repos.install('GIT_URL_FOR_REPO')
```

Before starting, create an admin user
```sh
./manage.py createsuperuser
```

Once the server is running, enter `localhost:8000/admin/`, and configure your
repos and pipelines.

* Setup pipeline commands using a yaml syntax, for example:

```yaml
setup:
- npm install
- bower install

test:
- ember test

deploy:
- ember deploy
```

After that, enter your repo settings in github and add a webhook pointing to
`<SERVER_URL>/webhooks/`.

And thats it!
