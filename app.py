from flask import Flask, render_template, request
from main import CourseDatabase

app = Flask(__name__)
db = CourseDatabase("DE_Equivalency_List_Clean.csv")
db.load_data()
db.preprocess()


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/search")
def search():
    query = request.form.get("query")
    results = db.search(query)
    return render_template("results.html", results=results, query=query)
