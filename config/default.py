import os

# Configuration for all environments
REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
