from app import db
access_status = 0
# statuses: 1-all is fine
# 2-user is unregistered
# 3 - passwords do not match

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256))


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=False)
    message = db.Column(db.String(256))
    message_date = db.Column(db.DateTime)


def register_user(username, password):
    try:
        user = Users(username=username, password=password)
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return True
    except Exception as error:
        print(error)
        return False


def login_user(username, password):
    global access_status
    users_list = Users.query.with_entities(Users.username).all()
    username_list = [username for (username,) in users_list]
    users = Users.query.all()
    if username not in username_list:
        access_status = 2
    else:
        for user in users:
            if user.username == username and user.password == password:
                access_status = 1
                break
            else:
                access_status = 3
    return access_status


def add_message(username, message, message_date):
    try:
        new_message = Messages(username=username, message=message, message_date=message_date)
        db.session.add(new_message)
        db.session.flush()
        db.session.commit()
    except Exception as error:
        print(error)



