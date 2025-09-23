# Explanation
This project is a locally running demo of controlling Docker containers
programatically with Django.

The file test.py is simply an independent script which demos controlling
Docker containers using the python-on-whales library.

The rest of the project is a Django project with an app named "demo" which
can be run locally.

# Installation and Setup
## Docker
I can't fit a guide here but please install Docker on your platform.

## DVWA
Please get [DVWA](https://github.com/digininja/DVWA) up and running.
Use the Docker instructions for DVWA.
In principle, any Dockerized app can be used, but this prototype hardcodes
DVWA. Ensure the directory `DVWA` is in the parent directory of this repository.
It should look something like this:
```console
$ cd [PARENT-DIRECTORY]
$ ls
...
DVWA/
protowadt/
...
```

## Python
Please set up a virtual environment to install packages.
On a Unix system, you can use [venv](https://docs.python.org/3/library/venv.html)
```console
$ python -m venv .venv
$ source .venv/bin/activate
$ which pip
(should output a local folder)
$ pip install -r requirements.txt
```

Now that you have DVWA working and Django and other packages installed,
you should be able to type `python manage.py runserver` in the `protowadt/` directory (this repo)
and go to http://localhost:8000/demo to see the demo working.

# Usage
Here are the current API endpoints:
- http://localhost:8000/demo/api/start
- http://localhost:8000/demo/api/restart
- http://localhost:8000/demo/api/stop
- http://localhost:8000/demo/api/down
- http://localhost:8000/demo/api/logs

If you access these local URLs and keep an eye on Docker Desktop, you can see the API
calls changing container state.
