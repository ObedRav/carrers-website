from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine, text
from os import getenv

USERNAME = getenv('USERNAME')
HOST= getenv('HOST')
PASSWORD = getenv('PASSWORD')
DATABASE= getenv('DATABASE')

engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4', connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem",
    }
}) 

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM jobs;'))
    print(result.all())