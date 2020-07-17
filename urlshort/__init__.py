from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'ag35jwqb4j32h8n8fsd787gy8s7edfgsa'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app