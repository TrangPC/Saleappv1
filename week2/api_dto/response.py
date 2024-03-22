from flask import Flask, Blueprint

import week2.bootstrap
from week2 import app
from week2.api_dto.request import request
from week2.api_dto.request import get_name
def response():
    data = week2.bootstrap.get_data_profile(name=get_name())
    return data