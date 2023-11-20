from flask import Flask, render_template, request

app = Flask('Calculator')


@app.route("/", methods=['GET', 'POST'])
def render_homepage():
    if request.method == "GET":
        return render_template('homepage.html')
    if request.method == "POST":
        user_example = request.form.get('example')
        answer = eval(user_example)
        return render_template('result.html', data=answer)


app.run(host='0.0.0.0', port=8080)


