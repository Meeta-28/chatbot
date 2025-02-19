from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
import openai
from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate

# Initialize Flask app
app = Flask(__name__)

# Firebase setup
cred = credentials.Certificate("C:/Users/meeta/OneDrive/Desktop/chatbot-project/backend/chatbot-a8da4-firebase-adminsdk-fbsvc-68ff8d9f37.json")  # Ensure correct path
firebase_admin.initialize_app(cred, {"storageBucket": "chatbot-a8da4.appspot.com"})
db = firestore.client()
bucket = storage.bucket()

# OpenAI API Key
openai.api_key = "your-openai-api-key"  # Replace with your OpenAI API key

# @app.route('/ask-question', methods=['POST'])
# def ask_question():
#     try:
#         question = request.form.get('question')
#         file = request.files.get('file')

#         file_url = None
#         if file:
#             blob = bucket.blob(file.filename)
#             blob.upload_from_file(file)
#             blob.make_public()
#             file_url = blob.public_url

#         # Save data to Firestore
#         db.collection("knowledge_base").add({
#             "question": question,
#             "file_url": file_url
#         })

#         # Retrieve stored knowledge
#         knowledge_base = db.collection("knowledge_base").stream()
#         context = ""
#         for doc in knowledge_base:
#             data = doc.to_dict()
#             context += f"Question: {data.get('question', '')}\nFile URL: {data.get('file_url', '')}\n"

#         # LangChain Prompt
#         prompt = PromptTemplate(input_variables=["context", "question"],
#                                 template="Context:\n{context}\n\nQuestion: {question}\nAnswer:")
#         llm = OpenAI(temperature=0)
#         tools = [Tool(name="Knowledge Base", func=lambda context, question: context)]
#         agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
        
#         answer = agent.run(input={"context": context, "question": question})
#         return jsonify({"answer": answer})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/ask-question', methods=['POST'])
def ask_question():
    try:
        question = request.form.get('question')
        file = request.files.get('file')

        print("Received question:", question)
        print("Received file:", file.filename if file else "No file uploaded")

        file_url = None
        if file:
            blob = bucket.blob(file.filename)
            blob.upload_from_file(file)
            blob.make_public()
            file_url = blob.public_url

            print("File uploaded to Firebase:", file_url)
            db.collection("knowledge_base").add({
                "question": question,
                "file_url": file_url
            })
            print("Data saved in Firestore")

        return jsonify({"message": "Upload successful!"})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


