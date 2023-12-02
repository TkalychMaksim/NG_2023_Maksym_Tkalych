from flask import Flask, render_template, request
from images_choice import image_index, images_list
app = Flask('Gallery')
current_index = 0


@app.route('/', methods=['GET', 'POST'])
def render_homepage():
    if request.method == 'GET':
        global current_index
        image_path = f'images/{images_list[current_index]}'
        return render_template('homepage.html', path=image_path)
    if request.method == "POST":
        if request.form.get('button_clicked') == 'next':
            current_index = image_index('next')
        elif request.form.get('button_clicked') == 'previous':
            current_index = image_index('previous')
        image_path = f'images/{images_list[current_index]}'
        return render_template('homepage.html', path=image_path)


app.run(host='0.0.0.0', port=8080, debug=True)
