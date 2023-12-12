from flask import Flask

app = Flask(__name__)
counter = 0

@app.route('/api/python/hello')
def hello():
    return 'Hello World!'

@app.route('/api/python/count')
def count():
    global counter
    counter += 1
    return 'Hello World! I have been seen %s times.' % counter

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)