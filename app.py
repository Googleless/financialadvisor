from flask import Flask, request, render_template, session
from datetime import timedelta
from dotenv import load_dotenv
from ai_handler import run_model

load_dotenv()

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=7)
app.secret_key = 'FLASK_SESH_KEY'


def handle_deepseek(user_input):
    return f"deepseek: {user_input}"

def handle_openrouter(user_input):
    return f"openrouter: {user_input}"

def aiAgent(ai_agent, user_input):
    switch={
        'deepseek':handle_deepseek,
        'openrouter':handle_openrouter
    }
    return switch.get(ai_agent, lambda x: "Unknown agent")(user_input)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/read-form', methods=['POST'])
def read_form():
    ai_agent = request.form['aiAgent']
    user_input = request.form['userInput']

    session.permanent = True

    session['ai_agent'] = ai_agent
    session['user_input'] = user_input
    
    response = run_model()
    return render_template('index.html', response=response)

