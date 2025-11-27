from flask import Blueprint, render_template, request
from .search_engine import search

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def home():
    return render_template("index.html", results=None, query=None, lenResults=0)


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
    if results_df is None or results_df.empty:
        return render_template(
            "results.html",
            results=None,
            query=query,
            lenResults=0
        )

    results_list = results_df.values.tolist()

    return render_template(
        "results.html",
        results=results_list,
        query=query,
        lenResults=len(results_list)
    )
