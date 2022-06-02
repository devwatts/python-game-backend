from flask import Flask
from flask_cors import CORS
import random

app= Flask(__name__)

@app.route('/')
def index():
  my_list = ["scissor", "paper", "rock"]
  return random.choice(my_list)