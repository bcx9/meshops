import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'meshops-dev')
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://meshops:meshops@postgres:5432/meshops')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
