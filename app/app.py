from flask import Flask
from config import Config, db

# Initialize the Flask app
app = Flask(__name__)

app.config.from_object(Config)

# Initialize SQLAlchemy with the Flask app
db.init_app(app)


if __name__ == '__main__':
  app.run(port=5000,debug=True)