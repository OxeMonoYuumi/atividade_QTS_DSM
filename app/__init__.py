from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # from .routes import main
    from app.routes.user_routes import user_bp
    # app.register_blueprint(main)
    app.register_blueprint(user_bp)

    # Nova Rota (interface)
    @app.route("/")
    def index():
        return render_template("users.html")

    return app
