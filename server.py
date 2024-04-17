from flask import Flask
from flask import render_template
from flask import Flask, request, redirect, url_for, render_template, jsonify
import json
import random
import re

app = Flask(__name__)

data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    # Log the time the user accesses the lesson
    users_data.append({'lesson_id': lesson_id, 'timestamp': str(datetime.now())})
    return render_template('learn.html', lesson_id=lesson_id)

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    if request.method == 'POST':
        # Store user's answer from the form
        user_answer = request.form['answer']
        users_data.append({'quiz_id': quiz_id, 'answer': user_answer})
        return redirect(url_for('quiz', quiz_id=quiz_id + 1))
    return render_template('quiz.html', quiz_id=quiz_id)

@app.route('/results')
def results():
    # Compute results based on answers stored in users_data
    # For simplicity, just passing the raw data
    return render_template('results.html', data=users_data)

if __name__ == '__main__':
    app.run(debug=True)