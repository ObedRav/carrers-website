#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        'title': 'Software Engineer',
        'location': 'Medellin, Colombia',
        'salary': '120000'
    },
    {
        'title': 'Database Engineer',
        'location': 'Bogota, Colombia',
        'salary': '110000'
    },
    {
        'title': 'Database Engineer',
        'location': 'Bogota, Colombia'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=jobs)


