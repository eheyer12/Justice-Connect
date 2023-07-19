#!/usr/bin/env python3
import ipdb
from models import db, Client, Lawyer, Lawfirm, Case
from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

CORS(app)

api = Api(app)

class Clients(Resource):
    
    def get(self):
        clients = Client.query.all()
        response_body = [client.to_dict(rules=("-cases",)) for client in clients]
       
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            json_data=request.get_json()
            new_client = Client(
                username=json_data.get("username"),
                role=json_data.get('role')
                )
            db.session.add(new_client)
            db.session.commit()

            response_body = new_client.to_dict()

            return make_response(jsonify(response_body), 200)
        
        except ValueError:
            response_body = {"error": ["validation errors"] }

            return make_response(jsonify(response_body), 400)


api.add_resource(Clients, "/clients")

class ClientsById(Resource):

    def get(self, id):
        client = Client.query.filter(Client.id == id).first()
        response_body = client.to_dict()

        if not client:
            response_body = {
                "error": "Client not found"
            }
            return make_response(jsonify(response_body), 404)

        return make_response(jsonify(response_body), 200)

    # def patch(self, id):
    #     client = Client.query.filter(Client.id == id).first()

    #     if not client:
    #         response_body = {
    #             "error": "Client not found"
    #         }
    #         return make_response(jsonify(response_body), 404)
        
    #     else:
    #         try:
    #             json_data = request.get_json()
    #             for key in json_data:
    #                 setattr(client, key, json_data.get(key))
    #             db.session.commit()

    #             response_body = client.to_dict()
    #             return make_response(jsonify(response_body), 200)
            
    #         except ValueError as error:
                
    #             response_body = {
    #                 "error": error.args
    #             }
                
    #             return make_response(jsonify(response_body), 422)
            
    def delete(self, id):
        client = Client.query.filter(Client.id == id).first()

        if not client:
            response_body = {
                "error": "Client not found"
            }
            status = 404

        else:
            db.session.delete(client)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)    

api.add_resource(ClientsById, "/clients/<int:id>")

class Lawyers(Resource):
    def get(self):
        lawyers = Lawyer.query.all()
        response_body = [lawyer.to_dict(rules=("-cases","-lawfirm")) for lawyer in lawyers]
       
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            json_data=request.get_json()
            new_lawyer = Lawyer(
                title=json_data.get("title"),
                lawfirm_id=json_data.get('lawfirm_id')
                )
            db.session.add(new_lawyer)
            db.session.commit()

            response_body = new_lawyer.to_dict()

            return make_response(jsonify(response_body), 200)
        
        except ValueError:
            response_body = {"error": ["validation errors"] }

            return make_response(jsonify(response_body), 400)

api.add_resource(Lawyers, "/lawyers")

class LawyersById(Resource):
    def get(self, id):
        lawyer = Lawyer.query.filter(Lawyer.id == id).first()
        response_body = lawyer.to_dict()

        if not lawyer:
            response_body = {
                "error": "Lawyer not found"
            }
            return make_response(jsonify(response_body), 404)
    
    def delete(self, id):
        lawyer = Lawyer.query.filter(Lawyer.id == id).first()

        if not lawyer:
            response_body = {
                "error": "Lawyer not found"
            }
            status = 404

        else:
            db.session.delete(lawyer)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status) 

api.add_resource(LawyersById, "/lawyers/<int:id>")

class Lawfirms(Resource):
    def get(self):
        lawfirms = Lawfirm.query.all()
        response_body = [lawfirm.to_dict(rules=("-lawyers.cases",)) for lawfirm in lawfirms]
       
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            json_data=request.get_json()
            new_lawfirm = Lawfirm(
                title=json_data.get("title"),
                rank=json_data.get('rank')
                )
            db.session.add(new_lawfirm)
            db.session.commit()
            response_body = new_lawfirm.to_dict()

            return make_response(jsonify(response_body), 200)
        
        except ValueError:
            response_body = {"error": ["validation errors"] }

            return make_response(jsonify(response_body), 400)

api.add_resource(Lawfirms, "/lawfirms")

class LawfirmsById(Resource):
    def get(self, id):
        lawfirm = Lawfirm.query.filter(Lawfirm.id == id).first()
        response_body = lawfirm.to_dict()

        if not lawfirm:
            response_body = {
                "error": "Lawfirm not found"
            }
        return make_response(jsonify(response_body), 404)
            
    def delete(self, id):
        lawfirm = Lawfirm.query.filter(Lawfirm.id == id).first()

        if not lawfirm:
            response_body = {
                "error": "Lawfirm not found"
            }
            status = 404

        else:
            db.session.delete(lawfirm)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status) 

api.add_resource(LawfirmsById, "/lawfirm/<int:id>")

class Cases(Resource):

    def get(self):
        cases = Case.query.all()

        response_body = []

        for case in cases:
            response_body.append(case.to_dict())

        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            json_data=request.get_json()
            new_case = Case(
                title=json_data.get("title"),
                body=json_data.get("body"),
                client_id=1,
                lawyer_id=1
            )
            db.session.add(new_case)
            db.session.commit()

            response_body = new_case.to_dict()
            
            return make_response(jsonify(response_body), 201)
        
        except ValueError:
            response_body = {"error": ["validation errors"] }

            return make_response(jsonify(response_body), 400)

api.add_resource(Cases, '/cases')

class CasesById(Resource):
    def get(self, id):
        case = Case.query.filter(Case.id == id).first()
        response_body = case.to_dict()
        print(case)
        if not case:
            response_body = {
                "error": "Case not found"
            }
            return make_response(jsonify(response_body), 404)
    
    def patch(self, id):
        case = Case.query.filter(Case.id == id).first()

        if not case:
            response_body = {
                "error": "Case not found"
            }
            return make_response(jsonify(response_body), 404)
        
        else:
            try:
                json_data = request.get_json()
                for key in json_data:
                    setattr(case, key, json_data.get(key))
                db.session.commit()

                response_body = case.to_dict()
                return make_response(jsonify(response_body), 200)
            
            except ValueError as error:
                
                response_body = {
                    "error": error.args
                }
                
                return make_response(jsonify(response_body), 422)
    
    def delete(self, id):
        case = Case.query.filter(Case.id == id).first()

        if not case:
            response_body = {
                "error": "Case not found"
            }
            status = 404

        else:
            db.session.delete(case)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status) 

api.add_resource(CasesById, "/cases/<int:id>")

if __name__ == '__main__':
    app.run(port=7000, debug=True)