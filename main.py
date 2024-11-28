from flask import Flask
from endpoints.production_plan import production_plan_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(production_plan_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8888)
