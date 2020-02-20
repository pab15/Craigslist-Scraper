import os
from app import app
from app.forms import BestResaleForm
from flask import redirect, url_for, render_template, request, session, flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Best-Cars', methods=['GET', 'POST'])
def best_cars():
    form = BestResaleForm()
    return render_template('bestcars.html', form=form)