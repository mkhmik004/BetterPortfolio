
# Flask imports
from flask import Flask

# Load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask application
app = Flask(__name__,static_folder='assets')


# Load configuration from config.py
app.config.from_pyfile('config.py')

# Import and register views
from . import views  

# Register routes from the views module
views.register_routes(app)  
