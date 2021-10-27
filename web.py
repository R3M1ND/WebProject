from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('web.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    #app.run()
