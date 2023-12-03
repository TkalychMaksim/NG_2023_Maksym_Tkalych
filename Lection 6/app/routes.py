import random

from app import app
from app.database import register_user, login_user, add_message, Messages
from flask import render_template, request, redirect, session
from datetime import datetime
import os
import random

@app.route('/', methods=['GET', 'POST'])
def render_homepage():
    images_list = sorted(os.listdir('client/static/images'))
    current_index = random.randint(0, (len(images_list)-1))
    image_path = f'images/{images_list[current_index]}'
    session_username = session.get('username', 'Anonym')
    if request.method == 'GET':
        return render_template('homepage.html', username=session_username, path=image_path)
    if request.method == 'POST':
        if request.form.get('button_clicked') == 'register':
            return redirect('/register')
        if request.form.get('button_clicked') == 'login':
            return redirect('/login')
        return render_template('homepage.html', username=session_username)
@app.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirmed_password = request.form.get('confirmed_password')
        if password == confirmed_password:
            if register_user(username, password):
                session['username'] = username
                return redirect('/chat')
            else:
                return render_template('register.html', error='Error: user with this nickname is already registered')
        else:
            return render_template('register.html', error='Error: Passwords do not match')
    if request.method == "GET":
        return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        access_status = login_user(username=username, password=password)
        print(access_status)
        if access_status == 1:
            session['username'] = username
            return redirect('/chat')
        elif access_status == 2:
            return render_template('login.html', error='Error: user with this username is unregistered')
        elif access_status == 3:
            return render_template('login.html', error='Error: password is incorrect')
    elif request.method == 'GET':
        return render_template('login.html')
@app.route('/chat', methods=['GET', 'POST'])
def render_chat_page():
    if request.method == "GET":
        chat_messages = get_messages()
        return render_template('chat.html', messages=chat_messages)
    elif request.method == "POST":
        message = request.form.get('input_message')
        if message is not None:
            add_messages(message)
        elif request.form.get('button_clicked') == 'log_out':
            session.clear()
            return redirect('/')
    return redirect('/chat')
def add_messages(message):
    username = session.get('username')
    add_message(username=username, message=message, message_date=datetime.now())
@app.route('/get_messages')
def get_messages():
    messages = Messages.query.order_by(Messages.message_date.asc()).all()
    messages_html = ''.join(
        f"<p><i>({message.message_date.strftime('%Y-%m-%d %H:%M:%S')})</i> <b>{message.username}</b>: {message.message}</p>"
        for message in messages
    )
    return messages_html
