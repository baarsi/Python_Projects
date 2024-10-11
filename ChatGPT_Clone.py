import requests

# Function to interact with OpenAI API to simulate a chatbot conversation
def send_request(message):
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": message,
        "max_tokens": 100
    }
    
    # Sending a POST request to OpenAI API with the user's message
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Main loop to send and receive chatbot messages
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    else:
        # Sending user input to the chatbot API
        bot_response = send_request(user_input)
        print(f"ChatGPT: {bot_response['choices'][0]['text']}")
