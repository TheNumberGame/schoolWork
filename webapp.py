import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

overAll = 0
correct = ["any", "Yes", "end"]

@app.route('/', methods=['GET', 'POST'])
def renderMain():
  #session['right'] += detRight()
  session['question'] = 0
  session['allTime'] = overAll
  return render_template('classQuiz.html')

@app.route('/outOf')
def renderOutOf():
  return render_template('outOfNum.html')

@app.route('/Q', methods=['GET', 'POST'])
def editCookie():
  global overAll, correct
  str = request.form['question'][0]
  num = request.form['question'][1]
  if num == 1:
    session["question"] = 1
  elif num == 2 and str == "Yes":
    session["question"] = 2
  
  if int(session['question']) >= overAll:
    overAll = int(session['question'])
    session['allTime'] = overAll
  
  return "Stop"

#def detRight()
 # session['question'] += request.form['question']
  #return session['question']

if __name__=="__main__":
    app.run(debug=False)
