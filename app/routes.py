from app import app
# from app.models import Employee, Department, Link 
from flask import render_template, redirect, request
# from sqlalchemy import update

@app.route('/')
def index():
    # return "Welcome to the HR department's website."
    return render_template('index.html', title="Home")