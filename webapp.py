import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(_name_)

app.secret_key=os.environ["SECRET_KEY"];

app.route('/' methods=['GET', 'POST'])
def renderMain():
  session['right'] += detRight()
  return render_tempalte('classQuiz.html')

def detRight()
  session['question'] += request.form['question']
  return session['question']

if __name__=="__main__":
    app.run(debug=False)
