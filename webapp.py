import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
from random import randrange

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

overAll = 0

@app.route('/', methods=['GET', 'POST'])
def renderMain():
  #session['right'] += detRight()
  session['question'] = 0
  session['allTime'] = overAll
  session['rand'] = randrange(100)
  return render_template('classQuiz.html')

@app.route('/outOf')
def renderOutOf():
  return render_template('outOfNum.html')

@app.route('/Q', methods=['GET', 'POST'])
def editCookie():
  global overAll
  
  st = request.form['question']
  num = request.form['num']
  print(st, num)
  if num == "first":
    session["question"] = 1
  elif num == "second" and st == "No":
    session["question"] = 2
  
  if int(session['question']) >= overAll:
    overAll = int(session['question'])
    session['allTime'] = overAll
  
  return "Stop"

#def detRight()
 # session['question'] += request.form['question']
  #return session['question']

if __name__=="__main__":
    app.run(debug=True)
