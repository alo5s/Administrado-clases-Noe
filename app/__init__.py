from flask import Flask
from config import Config
from .routes import views_home, views_estudiantes, views_profesores, views_bonos, view_calendarioo

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

app.register_blueprint(views_home)
app.register_blueprint(view_calendarioo)
app.register_blueprint(views_estudiantes)
app.register_blueprint(views_profesores)
app.register_blueprint(views_bonos)
