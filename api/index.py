from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contactme")
def contactme():
    return render_template("contactme.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

# Export the app as "app" for Vercel
app = app

# Optional: Uncomment this for local testing
# if __name__ == '__main__':
#     app.run(debug=True)
