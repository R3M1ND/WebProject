from flask import Flask, render_template,request
app = Flask(__name__)

#---------------------------------------------------------------------
@app.route('/')
def Home():
    return render_template('web.html')
@app.route('/my-link/')
def my_link():
    return render_template('rankweb.html')
@app.route('/searchengine',methods = ['POST',"GET"])
def search():
    output = request.form.to_dict()
    search = output["search"]   
    return render_template('rankweb.html',search = search)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    #app.run()
