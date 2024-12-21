from Decorators import Singleton
from dao.ConversationDAO import ConversationDAO
from dao.MessageDAO import MessageDAO
from dao.UserDAO import UserDAO
from util.Error import Error

@Singleton
class ConversationService():
    def __init__(self) -> None:
        self.conversationDAO = ConversationDAO()
        self.messageDAO = MessageDAO()
        self.userDAO = UserDAO()

    def getUserConversations(self, request):
        user_id = request.args.get('user_id')
        conversations = []
        #get conversations of user_id
        for conversation in self.conversationDAO.getUserConversations(user_id):
            user_ids = conversation.user_ids #user_ids = '_1__2__3_'
            user_ids = user_ids.replace('__', ' ') #user_ids = '_1 2 3_''
            user_ids = user_ids.replace('_', '').split() #user_ids = [1, 2, 3]
            
            #get list of user representation 
            #include user_name and image_url for display
            user_list = []
            for id in user_ids:
                if id == user_id:
                    continue
                user = self.userDAO.getUserById(id)
                user_list.append(user.__repr__())
            
            item = conversation.as_dict()
            item.__setitem__('users', user_list)
            conversations.append(item)

            umc = self.messageDAO.getUnreadCount(int(id), conversation.conversation_id)
            item.__setitem__('unread', umc)

        return conversations


    def createConversation(self, request):
        user_ids = request.form.get('user_list')
        conversation_id = self.conversationDAO.createConversation(user_ids)

        user_ids = user_ids.replace('__', ' ') #user_ids = '_1 2 3_''
        user_ids = user_ids.replace('_', '').split() #user_ids = [1, 2, 3]
        for id in user_ids:
            self.messageDAO.setupNotiForUnread(user_id=int(id), conversation_id=conversation_id)
        
        return {'status': 'create success'}

    def updateConversation(self, request):
        conversation_id = request.args.get('conversation_id')
        add_id = request.args.get('add_id')
        remove_id = request.args.get('remove_id')
        if add_id != None:
            return self.addPeopleToConversation(add_id, conversation_id)
        if remove_id != None:
            return self.removePeopleFromConversation(remove_id, conversation_id)
        
        return {'status': 'request error'}

    def deleteConversation(self, request):
        conversation_id = request.args.get('conversation_id')
        conversation = self.conversationDAO.getConversationByID(conversation_id)
        if conversation == None:
            return {'status': Error.NOT_FOUND_ERROR}
        self.conversationDAO.deleteConversation(conversation)
        return {'status': 'finish delete'}

    def leaveConversation(self, request):
        pass

    def addPeopleToConversation(self, user_id, conversation_id):
        conversation = self.conversationDAO.getConversationByID(conversation_id)
        user_ids = conversation.user_ids
        if f"_{user_id}_" in user_ids:
            return {'status': 'user already in the conversation'}
        new_user_ids = f"{user_ids}_{user_id}_"
        self.conversationDAO.updateMember(conversation, new_user_ids)
        return {'status': 'ok'}

    def removePeopleFromConversation(self, user_id, conversation_id):
        conversation = self.conversationDAO.getConversationByID(conversation_id);
        user_ids = conversation.user_ids
        new_user_ids = user_ids.replace('_' + user_id + '_', '')
        self.conversationDAO.updateMember(conversation, new_user_ids)

        return {'status': 'ok'}


    