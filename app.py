from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Vercel!"

if __name__ == '__main__':
    # This part won't run on Vercel
    pass