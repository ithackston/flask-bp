Yet Another Flask Boilerplate
-----------------------------

Features
========

* Python 3.7.6
* Flask 1.1.1
* Job handling with Redis 3.3.11 and rq 1.2.0
* Templates with Bootstrap 4.3.1
* Production and development config handling
* Editor config for Atom (better whitespacing for templates)

Getting Started
---------------

Install the prerequisites ([Homebrew](https://docs.brew.sh/Installation) makes
this very easy):
* [Python 3.8.0](https://www.python.org/downloads/release/python-380/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
* [Redis](https://formulae.brew.sh/formula/redis)

Create an new virtual environment and activate it.

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Use pip to install the requirements.

```bash
$ pip install -R requirements.txt
```

Running Web App Locally
-----------------------

Copy the `example.env.txt` file to a new file called `.env`.

Start the Redis server. You don't need to interact with Redis once it's started.

```bash
$ redis-server
```

Hit CMD+D to split the terminal into two panes. Activate the virtual environment
in the second pane (`source venv/bin/activate`). Start a new Redis worker called
"app-tasks".

```bash
$ rq worker app-tasks
```

Back in the first pane, run the server in development mode:

```bash
$ flask run
```

Open the app in your browser as instructed (http://127.0.0.1:5000/).

