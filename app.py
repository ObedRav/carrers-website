#!/usr/bin/python3
from flask import Flask, render_template, request
from database import get_jobs, load_job_from_db

app = Flask(__name__)


@app.route('/')
def home():
    JOBS = get_jobs()
    return render_template('home.html', jobs=JOBS)

@app.route('/job/<int:id>')
def dinamic_job(id: int):
    job = load_job_from_db(id)
    if job is None:
        return "Not found 404"
    return render_template('jobpage.html', job=job) 

@app.route('/job/<int:id>/apply', methods=['POST'])
def apply_to_job(id: int):
    data = request.form
    job = load_job_from_db(id)
    return render_template('application_submitted.html', application=data, job=job)
