import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  time_date = datetime.datetime.now()
  return render_template("index.html", dt=time_date)

@app.route('/mappa', methods=['GET'])
def mappa():
  return render_template('mappa.html')
@app.route('/mappa600', methods=['GET'])
def mappa600():
  return render_template('mappa600.html')
@app.route('/mappa800', methods=['GET'])
def mappa800():
  return render_template('mappa800.html')
@app.route('/mappa1000', methods=['GET'])
def mappa1000():
  return render_template('mappa1000.html')
@app.route('/template', methods=['GET'])
def template():
  return render_template('sitoTemplate/index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)