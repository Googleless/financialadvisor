from flask import Flask, request, render_template, session
from datetime import timedelta
from dotenv import load_dotenv
from ai_handler import run_model

# loads flask secret key
load_dotenv()

app = Flask(__name__)

# saves session for a week, plan to make it also retain the AI history of responses not to waste API tokens on pointless generations
app.permanent_session_lifetime = timedelta(days=7)
app.secret_key = 'FLASK_SESH_KEY'

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

