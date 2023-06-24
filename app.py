from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)


@app.route("/")
def home():
    JOBS = load_jobs_from_db()
    return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def list_job():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
