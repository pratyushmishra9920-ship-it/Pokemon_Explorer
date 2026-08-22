from flask import Flask

app = Flask(__name__)


from .helper_func import character, get_character, validate_input
from . import routes
