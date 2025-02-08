from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Store conversation history (Optional: Use a database for persistence)
conversation_history = []

class Chatbot(Resource):
    def post(self):
        try:
            data = request.get_json()
            user_message = data.get("message", "").strip()

            if not user_message:
                return {"error": "Message is required"}, 400

            # Simple Response Logic (You can replace this with AI models)
            bot_response = self.generate_response(user_message)

            # Store conversation history
            conversation_history.append({"user": user_message, "bot": bot_response})

            return jsonify({"response": bot_response, "history": conversation_history})

        except Exception as e:
            return {"error": str(e)}, 500

    def generate_response(self, user_message):
        """Basic response logic (Replace with AI like OpenAI or Llama)"""
        if "hello" in user_message.lower():
            return "Hello! How can I assist you today?"
        elif "bye" in user_message.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm here to help! Could you please rephrase that?"

# Add API resource
api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)
