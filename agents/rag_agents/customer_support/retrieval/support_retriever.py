import os
from google.generativeai import configure, GenerativeModel

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
configure(api_key=GEMINI_API_KEY)

class SupportRetriever:
    def __init__(self):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")

    def retrieve_ticket(self, ticket_id):
        """Retrieve support ticket details by ID using Gemini."""
        prompt = f"Retrieve detailed information for support ticket with ID {ticket_id}."
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Ticket not found."

    def search_issues(self, query):
        """Search for issues similar to the query using Gemini."""
        prompt = f"Search and list issues related to: '{query}'"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "No issues found."

    def multi_query_search(self, queries):
        """Search for multiple queries simultaneously using Gemini."""
        results = {}
        for query in queries:
            results[query] = self.search_issues(query)
        return results

    def advanced_search(self, query, filters=None):
        """Perform advanced search with filters if provided."""
        filter_description = f" with filters: {filters}" if filters else ""
        prompt = f"Perform an advanced search for: '{query}'{filter_description}."
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "No matching results found."
