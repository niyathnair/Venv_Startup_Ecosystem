import os
from google.generativeai import configure, GenerativeModel

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
configure(api_key=GEMINI_API_KEY)

class FAQModel:
    def __init__(self):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")

    def generate_faq(self, historical_tickets):
        """Generate FAQs using historical tickets and Gemini."""
        faqs = {}

        for ticket in historical_tickets:
            if ticket['resolved']:
                issue = ticket['issue']
                prompt = f"Generate an FAQ for the following issue: '{issue}' with this resolution: '{ticket['resolution']}'"
                response = self.model.generate_content(prompt)
                faq_content = response.text.strip() if response else "No FAQ generated."
                faqs[issue] = faq_content

        sorted_faqs = dict(sorted(faqs.items(), key=lambda x: x[0]))
        return sorted_faqs
