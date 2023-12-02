from app import db
access_status = False


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
    users = Users.query.all()
    for user in users:
        if user.username == username and user.password == password:
            access_status = True
            break
        else:
            access_status = False
    return access_status


def add_message(username, message, message_date):
    try:
        new_message = Messages(username=username, message=message, message_date=message_date)
        db.session.add(new_message)
        db.session.flush()
        db.session.commit()
    except Exception as error:
        print(error)



