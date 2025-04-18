from flask import Flask, render_template

app = Flask(__name__)

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

def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == '__main__':
    app.run(debug=True)
