import os

from flask import Flask
from dotenv import load_dotenv
from redis import Redis
from rq import Queue

# Get the project root path
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")

# Load variables from .env file
DOTENV_PATH = os.path.join(APP_ROOT, ".env")
load_dotenv(DOTENV_PATH)

# Set config path env variable if not already set
VAR_CONFIG_PATH = "FLASK_CONFIG_FILE"
FLASK_ENV = os.getenv("FLASK_ENV", "production")
ENV_CONFIG_PATH = os.path.join(APP_ROOT, "config", FLASK_ENV + ".py")
os.environ.setdefault(VAR_CONFIG_PATH, ENV_CONFIG_PATH)

def create_app(config_file=None, settings_override=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Load the default config file
    app.config.from_pyfile(os.path.join(APP_ROOT, "config", "default.py"))

    if config_file:
        # Use the manually specified config file
        app.config.from_pyfile(config_file)
    else:
        # Use the default already loaded into the environment variable
        app.config.from_envvar(VAR_CONFIG_PATH)

    if settings_override:
        # Override config variables with the dictionary parm
        app.config.update(settings_override)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = Queue(os.getenv("RQ_NAME"), connection=app.redis)

    from . import index
    app.register_blueprint(index.bp)

    return app
