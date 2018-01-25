import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(_name_)

app.route('/'):
def renderMain():
  return render_tempalte('classQuiz.html')
