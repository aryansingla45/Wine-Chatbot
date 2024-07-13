from flask import Flask, render_template, request, jsonify
from models.chatbot import Chatbot
import os

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'),
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'))

chatbot = Chatbot(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/corpus.json'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
