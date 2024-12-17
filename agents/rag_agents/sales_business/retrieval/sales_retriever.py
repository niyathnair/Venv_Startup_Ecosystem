from google.generativeai import GenerativeModel
from configs.config import GEMINI_API_KEY

class SalesRetriever:
    def __init__(self, knowledge_base_path):
        # Correct initialization using Generative AI
        self.model = GenerativeModel(model_name="gemini-1.5-pro")
        self.knowledge_base = knowledge_base_path

    def retrieve_sales_record(self, sales_id):
        # Correct prompt structure
        prompt = f"Retrieve sales record for {sales_id}"
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def search_customers(self, query):
        # Correct customer search prompt
        prompt = f"Search for customers related to {query}"
        response = self.model.generate_content(prompt)
        return response.text.strip()


