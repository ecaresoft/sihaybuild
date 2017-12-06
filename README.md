# Si Hay Build

A naive CI implementation made in django.

### Installation
1. [Install Pipenv](https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv)
```sh
sudo pip install pipenv
sudo pipenv install --two
pipenv shell
```
2. [Config database](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/) and setup `env` variables
```sh
psql# CREATE DATABASE databasename OWNER name;
pipenv run manage.py migrate
```
3. Run the app with honcho
```sh
pipenv run honcho start
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
