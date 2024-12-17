from agents.rag_agents.finance_legal.data_processing.financial_analyzer import FinancialAnalyzer
from agents.rag_agents.finance_legal.models.compliance_model import ComplianceModel
from agents.rag_agents.finance_legal.retrieval.legal_retriever import LegalRetriever

class FinanceLegalAgent:
    def __init__(self, knowledge_base_path, communication_hub):
        self.retriever = LegalRetriever(knowledge_base_path)
        self.analyzer = FinancialAnalyzer()
        self.compliance_model = ComplianceModel()
        self.communication_hub = communication_hub

    def generate_financial_report(self, financial_data):
        financial_summary = self.analyzer.generate_financial_summary(financial_data)
        violations = self.compliance_model.verify_compliance(financial_data)
        return {
            "summary": financial_summary,
            "compliance_violations": violations
        }

    def retrieve_tax_regulations(self):
        return self.retriever.fetch_tax_regulations()

    def fetch_legal_documents(self, query):
        return self.retriever.retrieve_legal_documents(query)
