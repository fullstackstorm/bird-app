import os

from flask import Flask, jsonify, make_response, Blueprint
from flask_migrate import Migrate
from flask_restful import Api, Resource
from .config import app, db, api
from .models import Bird

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

api.add_resource(Birds, '/birds')
