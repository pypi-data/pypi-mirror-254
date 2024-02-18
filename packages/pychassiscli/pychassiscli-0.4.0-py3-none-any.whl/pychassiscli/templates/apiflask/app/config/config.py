import os

from pychassislib import Config as _Config


class Config(_Config):
    """
    配置
    """
    RABBITMQ_URI = os.getenv('RABBITMQ_URI')

