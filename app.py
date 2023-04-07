#!/usr/bin/python3
from flask import Flask, render_template, jsonify
from database import get_jobs

app = Flask(__name__)


@app.route('/')
def home():
    JOBS = get_jobs()
    return render_template('home.html', jobs=JOBS)

@app.route('/api')
def json():
    JOBS = get_jobs()
    return jsonify(jobs=JOBS)
