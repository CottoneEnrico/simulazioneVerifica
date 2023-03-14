import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  time_date = datetime.datetime.now()
  return render_template("index.html", dt=time_date)

@app.route('/mappa', methods=['GET'])
def mappa():
  width = request.args.get("width")
  height = request.args.get("heigh")
  return render_template('mappa.html', width=width, height=height)

@app.route('/template', methods=['GET'])
def template():
  return render_template('sitoTemplate/index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)