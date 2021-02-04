from flask import Flask, jsonify


def create_app(test_config=None):
    app = Flask(__name__)
    @app.route('/')
    def home():
        return jsonify({'messsage':'hello world'})
    return app
    
