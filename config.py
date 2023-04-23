import os
from dotenv import load_dotenv

load_dotenv('.env')


class Config(object):
    def __init__(self):
        self.vkapi = os.getenv('vkapi')
