from app import create_app

app = create_app()
app.run('127.0.0.1', 5000, debug=app.config.get('DEBUG'))