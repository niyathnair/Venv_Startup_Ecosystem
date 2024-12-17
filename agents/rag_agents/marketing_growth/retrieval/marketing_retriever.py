import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

class MarketingRetriever:
    def __init__(self, knowledge_base_path):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")
        self.knowledge_base = knowledge_base_path

    def retrieve_documents(self, query):
        """Retrieve marketing-related documents using Gemini."""
        prompt = f"Retrieve marketing documents related to: {query}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Document retrieval failed."

    def retrieve_trends(self, query):
        """Retrieve latest market trends based on a query."""
        prompt = f"Find current market trends related to: {query}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Trend retrieval failed."

    def retrieve_competitor_data(self, query):
        """Retrieve competitor performance data from the knowledge base."""
        prompt = f"Retrieve competitor data related to: {query}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Competitor data retrieval failed."

    def retrieve_customer_feedback(self, product_name):
        """Retrieve customer feedback for a given product."""
        prompt = f"Retrieve customer feedback for product: {product_name}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Customer feedback retrieval failed."

    def search_campaign_history(self, campaign_name):
        """Search campaign history for past performance details."""
        prompt = f"Search past campaign performance records for: {campaign_name}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Campaign history retrieval failed."

    def fetch_marketing_insights(self, topic):
        """Fetch general marketing insights on a specific topic."""
        prompt = f"Fetch detailed marketing insights about: {topic}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Marketing insights retrieval failed."
