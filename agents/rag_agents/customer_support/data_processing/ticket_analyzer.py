# class TicketAnalyzer:
#     def analyze_tickets(self, tickets):
#         critical_tickets = [ticket for ticket in tickets if ticket['priority'] == 'high']
#         return critical_tickets

#     def generate_summary(self, tickets):
#         summary = {
#             "total_tickets": len(tickets),
#             "open_tickets": len([t for t in tickets if not t['resolved']]),
#             "resolved_tickets": len([t for t in tickets if t['resolved']])
#         }
#         return summary

import os
from google.generativeai import configure, GenerativeModel

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
configure(api_key=GEMINI_API_KEY)

class TicketAnalyzer:
    def __init__(self):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")

    def analyze_priority(self, tickets):
        """Identify high-priority tickets."""
        return [t for t in tickets if t.get('priority') == 'high']

    def generate_summary(self, tickets):
        """Summarize tickets."""
        return {
            "total_tickets": len(tickets),
            "open_tickets": len([t for t in tickets if not t['resolved']]),
            "resolved_tickets": len([t for t in tickets if t['resolved']])
        }

    def perform_sentiment_analysis(self, tickets):
        """Perform sentiment analysis using Gemini on ticket descriptions."""
        sentiment_details = []

        for ticket in tickets:
            description = ticket['description'].lower()
            prompt = f"Analyze the sentiment of this text: '{description}'"
            response = self.model.generate_content(prompt)
            sentiment_analysis = response.text.strip() if response else "Unknown"
            sentiment_details.append({
                "ticket_id": ticket.get('id', 'unknown'),
                "analysis": sentiment_analysis
            })

        summary = {
            "positive": len([t for t in sentiment_details if 'positive' in t['analysis'].lower()]),
            "negative": len([t for t in sentiment_details if 'negative' in t['analysis'].lower()]),
            "neutral": len([t for t in sentiment_details if 'neutral' in t['analysis'].lower()]),
            "detailed_analysis": sentiment_details
        }
        return summary

    def detect_anomalies(self, tickets):
        """Detect tickets with uncommon attributes for anomaly detection."""
        anomalies = [t for t in tickets if t.get('priority') == 'critical' and not t['resolved']]
        return anomalies
