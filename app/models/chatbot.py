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
        # print(f"Loaded corpus: {self.corpus}")

    def get_response(self, question):
        # print(f"Received question: {question}")
        for item in self.corpus:
            if item['question'].lower() == question.lower():
                print(f"Match found: {item['answer']}")
                return item['answer']
        # print("No match found. Please contact the business owner directly.")
        return "Please contact the business owner directly."
