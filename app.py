#!/usr/bin/python3
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request
from database import get_jobs, load_job_from_db
from os import getenv
import smtplib, ssl
from email.message import EmailMessage


app = Flask(__name__)

MAIL_SERVER = getenv('MAIL_SERVER')
MAIL_PORT = getenv('MAIL_PORT')
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD')

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
    data_email = list(map(lambda pair: f"{pair[0]}: {pair[1]}", data.items()))
    # Sending an email
    receiver_email = request.form.get('email')
    msg = EmailMessage()
    msg['Subject'] = 'Application Jovian'
    msg.set_content(f"""\
We confirm your application to {job['title']} at Jovian.

This is your application data:

- Name: {data.get('full_name')}
- Email: {data.get('email')}
- LinkedIn URL: {data.get('linkedin_url')}
- Resume URL: {data.get('resume_url')}

Thank you for your interest in Jovian!
""")
    msg['To'] = receiver_email
    msg['From'] = MAIL_USERNAME
    send_email(msg)

    return render_template('application_submitted.html', application=data, job=job)

def send_email(message):
    context = ssl.create_default_context()
    with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.send_message(message)
