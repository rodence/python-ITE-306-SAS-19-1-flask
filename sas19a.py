from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/hello/<rodence>')
def hello_name(rodence):
        return 'Hello %s!' % rodence

if __name__ == '__main__':
        app.run()
