from flask import Blueprint, render_template, request
from .search_engine import search

main_bp = Blueprint("main", __name__, static_folder="static")


@main_bp.get("/")
def home():
    return render_template("index.html")


@main_bp.post("/search")
def search_route():
    query = request.form.get("query", "").strip()

    if not query:
        return render_template(
            "index.html",
            results=None,
            query=query,
            lenResults=0,
            message="Please enter a search term."
        )

    results_df = search(query)

    # Convert results for HTML
    if results_df is None:
        return render_template(
            "results.html",
            results=None,
            query=query,
            lenResults=0
        )

    results_list = results_df
    print("Routes.py")
    print(results_list)

    return render_template(
        "results.html",
        results=results_list,
        query=query,
        lenResults=len(results_list)
    )


@main_bp.get("/hints")
def hints():
    return render_template("hints.html")
