from flask import Flask, Blueprint

import week2.bootstrap
from week2 import app, bootstrap
from week2.api_dto.request import request


class Response:
    def __init__(self, name):
        self.name = name

    def res_name(name):
        name = request.form['name']
        data = bootstrap.get_data_profile(name=name)
        return data


@app.route('/data/profile', methods=['POST'])
def process():
    name = request.json.get('name')
    res_name = Response(name=name)
    process_name = process(res_name.name)
    response_data = process_name
    return (process_name)
