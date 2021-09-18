from flask import Flask, render_template
# import functions

app = Flask(__name__)

# ROUTES #
@app.route('/')
def home_redirect():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("home.html")

# @app.route("/about")
# def about():
# return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)



