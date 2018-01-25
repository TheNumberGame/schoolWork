import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(_name_)

app.secret_key=os.environ["SECRET_KEY"];

app.route('/' methods=['GET', 'POST'])
def renderMain():
  session['right'] = request.forms['right']
  return render_tempalte('classQuiz.html')
