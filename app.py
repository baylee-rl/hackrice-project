from flask import Flask, render_template, redirect, url_for, Response, request, session
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import os
from functions import *
app = Flask(__name__)


SECRET_KEY = os.environ.get('SECRET_KEY')

# ROUTES #
@app.route('/')
def home_redirect():
    return redirect(url_for('home'))

@app.route("/home", methods=["GET", "POST"])
def home():
    state_names = ["Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    session['state'] = 'Oregon'

    if request.method == 'POST':
        session['state'] = request.form.get('state')

        return render_template("home.html", states=state_names)    

    return render_template("home.html", states=state_names)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/plot.png")
def plot_png():
    fig = create_figure(session['state'])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)



