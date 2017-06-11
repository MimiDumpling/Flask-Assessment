from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def home():
    """This is the home page"""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """This is the application_form"""

    jobs = ["Software Engineer", "QA Engineer", "Product Manager"]
    
    return render_template("application-form.html", jobs=jobs)


@app.route("/application-success", methods=['POST'])
def application_success():
    """This is the confirmation page."""

    value = request.form['salary']

    session['name'] = (request.form['firstname'] + " " + request.form['lastname'])
    session['job'] = request.form['job']
    session['salary'] = "${:,.2f}".format(float(value))
    
    return render_template("application-response.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
