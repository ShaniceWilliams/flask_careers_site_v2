from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import json

load_dotenv()

engine = create_engine(os.getenv('DB_CONN_STRING'), echo=True)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        results = []
        for row in result.all():
            row_as_dict = row._mapping
            results.append(row_as_dict)
        return results


def load_job_from_db(id):
    with engine.connect() as conn:
        query = text("select * from jobs where id = :val")
        job_id = {"val": id}
        result = conn.execute(query, job_id)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            results = [dict(row._mapping) for row in rows]
            return results

