import json
import google.generativeai as genai

genai.configure(api_key='AIzaSyCM8A81SBYFvxBFj93qCzHhhhz8lx4I8pA')

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

class Chatbot:
    def __init__(self, corpus_path):
        with open(corpus_path, 'r') as file:
            self.corpus = json.load(file)
    
    def get_response(self, question):
        if question in self.corpus:
            return self.corpus[question]
        else:
            return "Please contact the business owner directly."

