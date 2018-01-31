import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

overAll = 0

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
  global overAll
  session['question'] = request.form['question']
  #If statement creating errors. Causes session['question'] to not update for whatever reason.    
  if int(session['question']) >= overAll:
    overAll = int(session['question'])
    session['allTime'] = overAll
  
  return "Stop"

#def detRight()
 # session['question'] += request.form['question']
  #return session['question']

if __name__=="__main__":
    app.run(debug=False)
