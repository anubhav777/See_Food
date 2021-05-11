from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:12345@localhost/seefood"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)
ma=Marshmallow(app)

class Foood(db.Model):
    __tablename__="food"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    ingredients=db.Column(db.String(100))

    def __init__(self,name,ingredients):
        self.name=name
        self.ingredients=ingredients

class FoodSchema(ma.Schema):
    class Meta:
        fields=('id','name','ingredients')

food_schema=FoodSchema()
food_schemas=FoodSchema(many=True)

@app.route("/uploadfood",methods=['POST'])
def uploadfile():
    name=request.json['name']
    ingredients=request.json['ingredients']
    result = Foood(name,ingredients)
    db.session.add(result)
    db.session.commit()
    return jsonify({'satus':'added succesfully'})

@app.route('/getfood/<id>',methods=['GET'])
def getallalbum(id):
    result=Foood.query.get(id)
    return food_schema.jsonify(result)

from app import views