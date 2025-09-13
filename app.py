from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session

# Quiz Questions
questions = [
    {
        "question": "Which language runs in a web browser?",
        "options": ["Java", "C", "Python", "JavaScript"],
        "answer": "JavaScript"
    },
    {
        "question": "What does CSS stand for?",
        "options": [
            "Central Style Sheets",
            "Cascading Style Sheets",
            "Cascading Simple Sheets",
            "Cars SUVs Sailboats"
        ],
        "answer": "Cascading Style Sheets"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hypertext Markup Language",
            "Hyper Trainer Marking Language",
            "Hyper Text Marketing Language",
            "HyperText Markdown Language"
        ],
        "answer": "Hypertext Markup Language"
    },
    {
        "question": "Which year was JavaScript launched?",
        "options": ["1996", "1995", "1994", "None of the above"],
        "answer": "1995"
    }
]

@app.route('/')
def index():
    session['score'] = 0
    session['current_question'] = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        selected_option = request.form.get('option')
        current_question = session.get('current_question', 0)

        # Check if answer is correct
        if selected_option == questions[current_question]['answer']:
            session['score'] = session.get('score', 0) + 1

        session['current_question'] = current_question + 1

        # If no more questions, go to result page
        if session['current_question'] >= len(questions):
            return redirect(url_for('result'))

    current_question = session.get('current_question', 0)
    return render_template('quiz.html', question=questions[current_question], qno=current_question + 1)

@app.route('/result')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
