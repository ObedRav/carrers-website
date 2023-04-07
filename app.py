#!/usr/bin/python3
from flask import Flask, render_template, jsonify
from database import get_jobs, load_job_from_db

app = Flask(__name__)

JOBS = []

@app.before_request
def initialize_jobs():
    global JOBS
    JOBS = get_jobs()

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api')
def json():
    return jsonify(jobs=JOBS)

@app.route('/job/<int:id>')
def dinamic_job(id: int):
    job = load_job_from_db(id)
    if job is None:
        return "Not found 404"
    return render_template('jobpage.html', job=job) 

