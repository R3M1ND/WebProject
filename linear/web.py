from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<string:name>')
def Home(name):
    return render_template('web.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)