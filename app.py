from flask import Flask, request, render_template

app = Flask(__name__)

def handle_deepseek(user_input):
    return f"deepseek: {user_input}"

def handle_openrouter(user_input):
    return f"openrouter: {user_input}"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/read-form', methods=['POST'])
def read_form():
    ai_agent = request.form['aiAgent']
    user_input = request.form['userInput']

    if ai_agent == 'deepseek':
        response = handle_deepseek(user_input)
    else:
        response = handle_openrouter(user_input)

    return {'response': response}