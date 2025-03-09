from flask import Flask
from app.infrastructure.api.routes import user_blueprint
from app.infrastructure.database.db import db
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Crear las tablas en la base de datos (solo la primera vez)
with app.app_context():
    db.create_all()

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)