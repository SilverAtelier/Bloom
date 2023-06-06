import sys
from api import app

sys.path.append('./api')

link = app.db_con()


# registration
# user existence
def check_name(name):
    doc_ref = link.collection(u'users').document(u'{}'.format(name))
    doc = doc_ref.get()
    if doc.exists:
        # if username is not available
        return False
    else:
        # if username is available
        return True


def register_user(username, password):
    try:
        if check_name(username):
            new_pwd = str(hash(password))
            doc = link.collection(u'users').document(username)
            doc.set({
                u'name': u"{}".format(username),
                u'pwd': u"{}".format(new_pwd)
            })
        else:
            return True
    except:
        print("something went wrong")


"""login
Authentication
"""


def login_user(username, password):
    try:
        if not check_name(username):
            new_pwd = str(hash(password))
            doc_ref = link.collection(u'users').document(u'{}'.format(username))
            doc = doc_ref.get()
            if doc.exists:
                details = doc.to_dict()
                if 'pwd' in details == new_pwd:
                    return True
                else:
                    return "wrong password"
            else:
                return "wrong username"
        return True
    except:
        return "error"


"""Reading message"""

"""sending message"""
