from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine, text
from os import getenv

USERNAME = getenv('USERNAME')
HOST= getenv('HOST')
PASSWORD = getenv('PASSWORD')
DATABASE= getenv('DATABASE')


def connect() -> create_engine.__class__:
    engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4', connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })
    return engine

def get_jobs() -> dict:
    engine = connect()

    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs;'))

        list_results = []

        for row in result.all():
            list_row = list(row)
            dictionary = {
                'id': list_row[0],
                'title': list_row[1],
                'location': list_row[2],
                'salary': list_row[3],
                'currency': list_row[4],
                'responsibilities': list_row[5],
                'requirements': list_row[6]
            }
            list_results.append(dictionary)

        return(list_results)