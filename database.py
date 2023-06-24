from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

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
