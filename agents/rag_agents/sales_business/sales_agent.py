from agents.rag_agents.sales_business.data_processing.sales_analyzer import SalesAnalyzer
from agents.rag_agents.sales_business.models.lead_model import LeadModel
from agents.rag_agents.sales_business.retrieval.sales_retriever import SalesRetriever

class SalesBusinessAgent:
    def __init__(self, knowledge_base_path, communication_hub):
        self.retriever = SalesRetriever(knowledge_base_path)
        self.analyzer = SalesAnalyzer()
        self.lead_model = LeadModel()
        self.communication_hub = communication_hub

    def generate_sales_report(self, sales_data):
        return self.analyzer.analyze_sales(sales_data)

    def identify_sales_trends(self, sales_data):
        return self.analyzer.sales_trends(sales_data)

    def qualify_leads(self, lead_data):
        return self.lead_model.score_leads(lead_data)

    def forecast_sales(self, current_leads):
        return self.lead_model.forecast_sales(current_leads)

    def search_customer_records(self, query):
        return self.retriever.search_customers(query)
