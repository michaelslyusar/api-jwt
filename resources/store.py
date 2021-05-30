from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return{'message':'Store does not exist'},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return{'message':'Store already exists'},400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"An error occurred while creating the store"},500
        return store.json(),201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {'message': 'Store already exists'}, 400
        else:
            return {'message': 'There is no store with that name'}, 400
        return {'message': 'Store deleted successfully'}, 200


class StoreList(Resource):
    def get(self):
        return{'stores':[store.json() for store in StoreModel.find_all()]}
