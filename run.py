# -*- coding: utf-8 -*-

import importlib
import sys

from app import create_app
from config import app_active_env, app_config

config = app_config[app_active_env]
config.APP = create_app(app_active_env)

if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    importlib.reload(sys)
