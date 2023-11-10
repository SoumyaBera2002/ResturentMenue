from flask import Flask, render_template, request, session, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
