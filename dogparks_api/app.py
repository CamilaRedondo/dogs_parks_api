from flask import Flask
from routes.park_routes import park_bp
from routes.aux_routes import aux_bp
from routes.address_routes import address_bp

app = Flask(__name__)
app.register_blueprint(park_bp)
app.register_blueprint(aux_bp)
app.register_blueprint(address_bp)

if __name__ == '__main__':
    app.run(debug=True)