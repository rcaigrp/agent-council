from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Initialize database here if needed
    with app.app_context():
        pass  # Placeholder for db initialization
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
