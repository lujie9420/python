from flask import Flask
import config
from exts import db
from apps.cms.views import cms_bp
from apps.front.views import front_bp

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)

# @app.route('/')
# def index():
#     return 'index success'

if __name__ == '__main__':
    app.run(debug=True,port=8000)