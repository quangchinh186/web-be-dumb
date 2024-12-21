from reposistory.BaseReposistory import Reposistory
from model.AppUser import AppUser
from sqlalchemy import select, desc

class AppUserRepo(Reposistory):
    # GET
    @classmethod
    def searchUsers(cls, name):
        cls.session.commit()
        users = cls.session.query(AppUser).filter(AppUser.name.like(f"%{name}%")).all()
        return users

    @classmethod
    def getUserById(cls, user_id) -> AppUser:
        cls.session.commit()
        user = cls.session.get(AppUser, user_id)
        if user == None:
            return None
        return user
    
    @classmethod
    def getUserByEmail(cls, email) -> AppUser:
        cls.session.commit()
        user = cls.session.query(AppUser).filter(AppUser.email == email).first()
        if user == None:
            return None
        return user
    
    # POST
    @classmethod
    def create(cls, **kwargs):
        newUser = AppUser(**kwargs)
        cls.session.add(newUser)
        cls.session.commit()

        return newUser
    
    # PUT
    @classmethod
    def update(cls, user: AppUser, **kwargs):
        user.update(**kwargs)
        cls.session.commit()
        
        return user

    # DELETE
    @classmethod
    def delete(cls, user_id):
        user = cls.getUserById(user_id)
        cls.session.delete(user)
        cls.session.commit()