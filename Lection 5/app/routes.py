from flask import render_template, request, redirect, make_response
from app import app
from app.database import register_user, login_user, add_message, Messages
from datetime import datetime


@app.route('/')
def redirect_to_register():
    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirmed_password = request.form.get('confirmed_password')
        if password == confirmed_password:
            if register_user(username, password):
                return redirect('/send')
            else:
                return render_template('register.html', error='Error: user with this nickname is already registered')
        else:
            return render_template('register.html', error='Error: Passwords do not match')
    if request.method == "GET":
        return render_template('register.html')


@app.route('/send', methods=['GET', 'POST'])
def user_login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        message = request.form.get('message')
        if login_user(username, password):
            add_message(username=username, message=message, message_date=datetime.utcnow())
            return redirect('/all')
        else:
            return render_template('send.html', error='Error: Passwords do not match')
    if request.method == 'GET':
        return render_template('send.html')


@app.route('/all')
def show_messages():
    messages = Messages.query.all()
    data = ""
    for message in messages:
        data += "{}: {} [{}]<br>".format(message.username, message.message, message.message_date)
    responce = make_response(data)
    return responce
