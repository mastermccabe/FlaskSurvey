from flask import Flask, render_template, redirect, request, session, flash
import re


# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    return render_template("index.html")
#

# def hello_world():
#     return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name_val']


    language = request.form['language']

    location = request.form['location']

    comment = request.form['comment']
    if len(request.form['name_val']) < 1:
        flash("name cannot be blank!")
        return redirect('/')
    elif not len(request.form['comment']) <= 121:
       flash("Form cant be longer than 120 charaters")
       return redirect('/')
    else:
       flash("Success!")
    # Here's the line that changed. We're rendering a template from a post route now.
    return render_template('results.html', name =name, location = location, language= language, comment = comment)

# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
