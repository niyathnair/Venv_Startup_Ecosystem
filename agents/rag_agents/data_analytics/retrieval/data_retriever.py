import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

class DataRetriever:
    def __init__(self, knowledge_base_path):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")
        self.knowledge_base = knowledge_base_path

    def retrieve_data(self, query):
        prompt = f"Retrieve data related to {query}"
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def fetch_statistics(self, stat_type):
        prompt = f"Fetch statistics related to {stat_type}"
        response = self.model.generate_content(prompt)
        return response.text.strip()

