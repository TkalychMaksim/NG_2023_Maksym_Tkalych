from flask import Flask, render_template, request, redirect
from images_choice import image_index, images_list
app = Flask('Gallery')
current_index = 0


@app.route('/', methods=['GET', 'POST'])
def render_homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    if request.method == "POST":
        global current_index
        if request.form.get('button_clicked') == 'next':
            current_index = image_index('next', current_index)
        elif request.form.get('button_clicked') == 'previous':
            current_index = image_index('previous', current_index)
        return redirect('gallery')


@app.route('/gallery')
def render_image():
    image_path = f'images/{images_list[current_index]}'
    print(image_path)
    return render_template('gallery.html', path=image_path)


app.run(host='0.0.0.0', port=8080, debug=True)
