#this safely compares two string regardless of their encodings
from werkzeug.security import safe_str_cmp
from user import User

#users = [
#    User(1, 'sagarnildass', 'sagar')
#]

#these help us to find a user quickly e.g. username_mapping['sagar'] or userid_mapping[1]
'''
username_mapping = {'sagar':{
                        'id':1,
                        'username':'sagarnildass',
                        'password':'sagar'
                        }
                    }

userid_mapping = {1:{
                    'id':1,
                    'username':'sagarnildass',
                    'password':'sagar'
                    }
                  }
'''


#alternative way now
#username_mapping = {u.username:u for u in users}
#userid_mapping = {u.id:u for u in users}

def authenticate(username, password):

    #now using the new method which we created in the User class.
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

#the payload is the content of the JWT(json web token) token. Then we are going to extract the
#userid from that payload
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
