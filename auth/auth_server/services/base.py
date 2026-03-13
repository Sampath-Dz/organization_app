class BaseService:

    def create(self,db,obj):

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj


    def delete(self,db,obj):

        db.delete(obj)

        db.commit()
