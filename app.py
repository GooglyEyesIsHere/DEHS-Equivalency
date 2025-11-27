from flask import Flask
from app.routes import main_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)

    return app


# This is the app object Gunicorn will use
app = create_app()

# Allow local development: python app.py
if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
