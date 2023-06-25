from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def home():
    JOBS = load_jobs_from_db()
    return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def list_job():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)


@app.route("/jobs/<id>")
def job_detail(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)


if __name__ == "__main__":
    app.run(debug=True)
