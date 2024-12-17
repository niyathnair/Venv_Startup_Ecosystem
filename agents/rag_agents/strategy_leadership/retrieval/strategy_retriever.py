from google.generativeai import GenerativeModel
from configs.config import GEMINI_API_KEY

class StrategyRetriever:
    def __init__(self, knowledge_base_path):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")
        self.knowledge_base = knowledge_base_path

    def retrieve_performance_data(self, query):
        prompt = f"Retrieve performance data for {query}"
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def search_strategic_plans(self, query):
        prompt = f"Search for strategic plans related to {query}"
        response = self.model.generate_content(prompt)
        return response.text.strip()
