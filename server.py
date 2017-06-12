from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def home_page():
    """Return homepage."""

    return render_template("index.html")


@app.route('/application-form')
def application_form():

    job_options = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", joboptions=job_options)


@app.route('/application-success', methods=["POST"])
def application_success():

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    received_salary = request.form.get('salary')
    position = request.form.get('position')

    salary = float(received_salary)

    return render_template("application-response.html", firstname=firstname, lastname=lastname, salary=salary, position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
