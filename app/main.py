from flask import Flask
import random

app= Flask(__name__)

@app.route('/')
def index():
  my_list = ["scissor", "paper", "rock"]
  return random.choice(my_list)