import jwt, bcrypt
import time, datetime
from datetime import timezone
from util.Error import Error
from reposistory.AppUserRepo import AppUserRepo
from .BaseService import BaseService

import os
from dotenv import load_dotenv

load_dotenv('util/.env')
SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class AppUserService(BaseService):
    @classmethod
    def getUserById(cls, user_id):
        user = AppUserRepo.getUserById(user_id)
        if user == None:
            raise Exception('user not found')
        return user.as_dict()
    
    @classmethod
    def checkEmailExist(cls, email):
        user = AppUserRepo.getUserByEmail(email)
        if user == None:
            return False
        return True
    
    @classmethod
    def searchUser(cls, name):
        users = []
        for item in AppUserRepo.searchUsers(name):
            users.append(item.as_dict())
        return users

    @classmethod
    def updateUser(cls, user_id, update_data):
        user = AppUserRepo.getUserById(user_id)
        if user == None:
            raise Exception('user not found')
        
        user = AppUserRepo.update(user, **update_data)
        return user.as_dict()

    @classmethod        
    def deleteUser(cls, user_id):
        AppUserRepo.delete(user_id)

class AuthService(BaseService):
    @classmethod
    def login(cls, email, password):
        user = AppUserRepo.getUserByEmail(email)
        if user == None:
            raise Exception('user not found')
        
        if not bcrypt.checkpw(password.encode('utf-8'), user.pwd.encode('utf-8')):
            raise Exception('wrong password')
        # jwt
        payload = {
            'user_id': user.user_id,
            "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    
    @classmethod
    def register(cls, user_data):
        if AppUserService.checkEmailExist(user_data['email']):
            raise Exception('email exist')
        # pop password key and hash it, replace it with hashed password
        password = user_data['password']
        del user_data['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data['pwd'] = hashed_password
        user = AppUserRepo.create(**user_data)
        # jwt
        payload = {
            'user_id': user.user_id,
            "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token