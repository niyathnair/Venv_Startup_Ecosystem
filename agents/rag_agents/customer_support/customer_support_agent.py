import os
from google.generativeai import configure, GenerativeModel
from agents.rag_agents.customer_support.data_processing.ticket_analyzer import TicketAnalyzer
from agents.rag_agents.customer_support.models.faq_model import FAQModel
from agents.rag_agents.customer_support.retrieval.support_retriever import SupportRetriever

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
configure(api_key=GEMINI_API_KEY)

class CommunicationHub:
    """Central hub for agent communication and notifications."""
    def __init__(self):
        self.logs = []

    def notify(self, message):
        print(f"[Notification] {message}")
        self.logs.append(message)

    def log_event(self, event):
        self.logs.append(event)

    def get_logs(self):
        return self.logs

class CustomerSupportAgent:
    def __init__(self, knowledge_base_path, communication_hub):
        self.retriever = SupportRetriever()
        self.analyzer = TicketAnalyzer()
        self.faq_model = FAQModel()
        self.communication_hub = communication_hub

    def resolve_ticket(self, ticket_id):
        """Retrieve and auto-resolve a ticket."""
        ticket = self.retriever.retrieve_ticket(ticket_id)
        if ticket and 'resolved' not in ticket:
            ticket['resolved'] = True
            ticket['resolution'] = "Auto-resolved based on similar cases."
            self.communication_hub.notify(f"Ticket {ticket_id} resolved.")
        return ticket

    def analyze_tickets(self, tickets):
        """Perform ticket analysis."""
        summary = self.analyzer.generate_summary(tickets)
        priority_tickets = self.analyzer.analyze_priority(tickets)
        sentiment = self.analyzer.perform_sentiment_analysis(tickets)
        self.communication_hub.notify("Ticket analysis completed.")
        return {
            "summary": summary,
            "priority_tickets": priority_tickets,
            "sentiment_analysis": sentiment
        }

    def generate_faq(self, historical_tickets):
        """Generate FAQs based on historical tickets."""
        faqs = self.faq_model.generate_faq(historical_tickets)
        self.communication_hub.notify("FAQs updated dynamically.")
        return faqs

    def search_customer_issues(self, query):
        """Search for related customer issues."""
        results = self.retriever.search_issues(query)
        self.communication_hub.notify(f"Search completed for query: {query}")
        return results

    def advanced_issue_search(self, query, filters=None):
        """Perform advanced issue search with optional filters."""
        results = self.retriever.advanced_search(query, filters)
        self.communication_hub.notify(f"Advanced search completed for query: {query}")
        return results

    def process_user_input(self, user_input):
        """Process incoming user requests."""
        action = user_input.get("action")
        if action == "resolve_ticket":
            return self.resolve_ticket(user_input['ticket_id'])
        elif action == "analyze_tickets":
            return self.analyze_tickets(user_input['tickets'])
        elif action == "generate_faq":
            return self.generate_faq(user_input['historical_tickets'])
        elif action == "search_issues":
            return self.search_customer_issues(user_input['query'])
        elif action == "advanced_search":
            return self.advanced_issue_search(user_input['query'], user_input.get('filters'))
        else:
            self.communication_hub.notify("Invalid action provided.")
            return {"error": "Invalid action."}
