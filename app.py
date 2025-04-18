from flask import Flask, render_template

# Initialize Flask app with an explicit template folder path
app = Flask(__name__, template_folder='templates')

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

# Vercel's serverless entry point
def handler(environ, start_response):
    return app(environ, start_response)

# This part is not needed for Vercel, but useful locally
if __name__ == '__main__':
    app.run(debug=True)
