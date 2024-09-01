## Chat App

This django app provides a set of HTTP and WS APIs for a chat server that supports both group and personal messages.

### Setup and run

#### pre-requisites
You need python and a virtualenv setup to install packages.
This project uses `django-channels` for websockets and it requires redis as a backend. The recommended way to get a redis server up and running fast is to use docker.
Since this is a development project, we will be using a sqlite database.

#### Run redis
use docker to run redis. Keep this running in a separate terminal
```
docker run --rm -p 6379:6379 redis:7
```

#### Setup virtualenv and install dependencies
Create and activate a virtualenv for this project and use pip to install the required libraries
```
pip install -r requirements.txt
```

#### Setup database
If running for the first time, you will need to create the tables in the database. Run
```
python manage.py migrate
```

In addition to this I would recommend that you create a superuser so that you can use the django admin to explore the models and data.
```
python manage.py createsuperuser
```
and follow the prompts

#### Run the server
Run the server using
```
python manage.py runserver
```
#### Docs
You can see the API docs here
```
http://localhost:8000/swagger/
```

### Caveats and missing functionalities
- [ ] No tests: This project does not have any unit tests or integration tests
- [ ] Edit message for 5 minutes after sending
- [ ] There should be indication of unread messages along with the count of unread messages for each conversation.
- [ ] Users should be able to see the typing status.
- [ ] Users should be able to search for other users using their username to initiate a conversation.
- [ ] Include an easy way to run a linter.
- [ ] Include some form of perfomance testing (may be using locust and faker?)