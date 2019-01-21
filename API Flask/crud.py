from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
from SegmentationTranslation import *
import _thread

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to create new user
@app.route("/post/", methods=["POST"])
def add_user():
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join('Augustus_IA', filename))

    _thread.start_new_thread(segmentation_and_translation(filename, findPostId()))

    return Response(status=200, mimetype='application/json')


# endpoint to show all users
@app.route("/get/<id>", methods=["GET"])
def get_user(id):
    try:
        file = open('Augustus_IA/AugustusOutputPrelucrat' + str(id) + '.json', 'r')
        json_data = json.load(file)
        return json_data
    except Exception as e:
        print("Json reading error:", e)
        return Response(status=503)


@app.route("/get/", methods=["GET"])
def get__default_user():
    try:
        file = open('Augustus_IA/AugustusOutputPrelucrat' + str(findPostId() - 1) + '.json', 'r')
        json_data = json.load(file)
        return json_data
    except Exception as e:
        print("Json reading error:", e)
        return Response(status=503)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)

