from flask import Flask, render_template

app = Flask(__name__)


jobs = [
            {
                "id": "0001",
                "title": "Jr Data Scientist",
                "location": "London",
                "salary": "£45,000"
                },
            {
                "id": "0002",
                "title": "Data Scientist",
                "location": "Bristol",
                "salary": "£65,000",
                },
            {
                "id": "0003",
                "title": "Sr Data Engineer",
                "location": "Remote",
                "salary": "£85,000",
                },
            {
                "id": "0004",
                "title": "Machine Learning Engineer",
                "location": "New York",
                "salary": "$125,000",
            }
]


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
