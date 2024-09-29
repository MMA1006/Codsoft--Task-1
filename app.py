from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you?" in user_input:
        return "I'm just a program, but thanks for asking! How can I assist you?"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created with Flask!"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "thank you" in user_input:
        return "Glad to help! if you have additional queries don't hesitate to reach out ."
    elif "goodbye" in user_input or "bye" in user_input:
        return "Bye! Have a wonderful day!"
    elif "what can you do" in user_input:
        return "I can help you with simple questions, assist you with information or just talk to you!"
    elif "your favorite color" in user_input:
        return "I do not really have a favorite color, but I love each and every color of the rainbow!"
    elif "tell me a joke" in user_input:
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems!",
            "What do you call fake spaghetti? An impasta!"
        ]
        return random.choice(jokes)
    elif "how old are you" in user_input:
        return "I have not existed for long and that is mostly due to my age!"
    elif "What is the weather like" in user_input:
        return "What is the weather like? I’m unable to answer that question. However, you can always seek the information on any online source or a weather app installed on your smart phone!"
    elif "news" in user_input:
        return " I cannot go to get news from the internet, but please go visit your preferred news website!"
    elif "do you love me" in user_input:
        return "I do not have emotions, but I am here to serve you!"
    elif "tell me about yourself" in user_input:
        return "I am a basic chatbot designed to help you in everything you want!"
    else:
        return "I'm sorry, I don't understand that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

