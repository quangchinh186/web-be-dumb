import bcrypt
from dao.AuthenticateDAO import AuthenticateDAO
from dao.UserDAO import UserDAO
from flask import current_app
from Decorators import Singleton

@Singleton
class AuthenticateService():
    def __init__(self) -> None:
        self.authenicateDao = AuthenticateDAO()
        self.userDAO = UserDAO()

    def checkExist(self, email):
        if self.authenicateDao.mailCheck(email) != None:
            return True
        return False
        
    # def login(self, request):
    #     formData = request.form
    #     email = formData.get('email')
    #     pwd = formData.get('pwd')

    #     account = self.authenicateDao.getAccount(email)
    #     if account == None:
    #         return {'status': 'account does not exist'}

    #     check_password = bcrypt.checkpw(password=str.encode(pwd), hashed_password=str.encode(account.pwd))
    #     if not check_password:
    #         return {'status': 'wrong password'}

    #     user = self.userDAO.getUserById(account.user_id).as_dict()
    #     join_date_str = user['join_date'].strftime("%Y-%m-%d %H:%M:%S")
    #     user['join_date'] = join_date_str

    #     token = jwt.encode(user, current_app.config['SECRET_KEY'])
    #     return {'token': token}

    def signup(self, request):
        formdata = request.form.to_dict()
        #check exist
        email = formdata.get('email')
        if self.checkExist(email):
            return {'status': 'mail exist'}
        
        pwd = str.encode(formdata['pwd'])
        salt = bcrypt.gensalt()
        hash_pwd = bcrypt.hashpw(password=pwd, salt=salt)
        formdata['pwd'] = hash_pwd

        #create account
        self.authenicateDao.createAccount(**formdata)
        
        return "done"
        
    def resetPassword(self, request):
        email = request.form['email']
        if not self.checkExist(email):
            return {'error': 'account does not exist'}

        pwd = request.form['pwd']
        account = self.authenicateDao.getAccount(email)
        salt = bcrypt.gensalt()
        hash_pwd = bcrypt.hashpw(password=str.encode(pwd), salt=salt)
        self.authenicateDao.resetPassword(account, hash_pwd)

        return {'status': 'success'}
        
    # def verify(self, email):
    #     if not self.checkExist(email):
    #         return {'error': 'account does not exist'}
    #     user_id = self.authenicateDao.getAccount(email).user_id
    #     #creat profile
    #     user = self.userDAO.createUser(user_id=user_id, user_name=f"USER {user_id}").as_dict()
    #     join_date_str = user['join_date'].strftime("%Y-%m-%d %H:%M:%S")
    #     user['join_date'] = join_date_str

    #     token = jwt.encode(user, current_app.config['SECRET_KEY'])
    #     return {'token': token}