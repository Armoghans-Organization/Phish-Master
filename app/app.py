from flask import Flask , render_template
from config import Config, db
from utilities import banner

# Initialize the Flask app
app = Flask(__name__)

app.config.from_object(Config)

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == '__main__':
  #  Print Terminal Banner
  banner.print_banner()
  app.run(port=5000,debug=True)