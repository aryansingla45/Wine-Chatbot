import google.generativeai as genai


genai.configure(api_key='AIzaSyCM8A81SBYFvxBFj93qCzHhhhz8lx4I8pA')

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config)

chat_session = model.start_chat(
  history=[
  ]
)

chat_session

response = chat_session.send_message("Hello, how are you?")

print(response.text)
print("====================================")
print(chat_session)
