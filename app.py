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
    resultsList = []
    thisResult = []
    if results == None:
        return render_template("results.html", results=None, query=query, lenResults=0)
    for i, e in enumerate(results):
        thisResult.append(e)
        if i % 6 == 5:
            resultsList.append(thisResult)
            thisResult = []
    return render_template("results.html", results=resultsList, query=query, lenResults=len(results)//6)
