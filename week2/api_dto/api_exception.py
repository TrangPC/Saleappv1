import flask
from flask import Flask, Blueprint, jsonify, request
def errorhandler(e):
    return {'status':'bad request!'}, 400


