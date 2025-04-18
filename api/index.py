from flask import Flask, render_template
import os

# Point Flask to the correct templates folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contactme')
def contactme():
    return render_template('contactme.html')

# This is the key line Vercel needs
def handler(environ, start_response):
    return handle_request(app, environ, start_response)

# Optional: Uncomment this for local testing
if __name__ == '__main__':
    app.run(debug=True)
