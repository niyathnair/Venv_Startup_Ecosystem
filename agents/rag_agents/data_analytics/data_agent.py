import os
import json
import matplotlib.pyplot as plt
from agents.rag_agents.data_analytics.data_processing.data_cleaner import DataCleaner
from agents.rag_agents.data_analytics.models.insight_model import InsightModel
from agents.rag_agents.data_analytics.retrieval.data_retriever import DataRetriever
from shared_components.communication_hub import CommunicationHub

class DataAnalyticsAgent:
    def __init__(self, knowledge_base_path, communication_hub):
        self.retriever = DataRetriever(knowledge_base_path)
        self.cleaner = DataCleaner()
        self.insight_model = InsightModel()
        self.communication_hub = communication_hub

    def clean_and_normalize_data(self, raw_data):
        cleaned_data = self.cleaner.clean_data(raw_data)
        normalized_data = self.cleaner.normalize_data(cleaned_data)
        return normalized_data

    def generate_data_insights(self, data):
        return self.insight_model.generate_insights(data)

    def forecast_market_trends(self, historical_data):
        return self.insight_model.forecast_trends(historical_data)

    def retrieve_statistical_data(self, query):
        return self.retriever.retrieve_data(query)

    def fetch_key_statistics(self, stat_type):
        return self.retriever.fetch_statistics(stat_type)

    def analyze_sales_data(self, product_name, metrics):
        sales_data = self.retriever.retrieve_data(f"sales data for {product_name}")
        total_sales = sum(item['sales'] for item in sales_data)
        average_sales = total_sales / len(sales_data)
        result = {
            "product": product_name,
            "total_sales": total_sales,
            "average_sales": average_sales
        }
        self.send_data_analysis_result("MarketingAgent", result)
        return result

    def send_data_analysis_result(self, recipient, result):
        self.communication_hub.send_message("DataAnalyticsAgent", recipient, {
            "request": "data_analysis_result",
            "result": result
        })

    def receive_message(self, sender, message):
        if message['request'] == "data_analysis":
            metrics = message['metrics']
            product_name = metrics['campaign']
            self.analyze_sales_data(product_name, metrics)
            print(f"[DataAnalyticsAgent] Analysis completed for {product_name}")

    def get_competitor_and_market_data(self):
        # Retrieve competitor market data from Gemini
        competitor_data = self.retriever.retrieve_data("competitor market data")
        market_data = self.retriever.retrieve_data("market trends")

        competitor_stats = []
        if isinstance(competitor_data, list):
            for item in competitor_data:
                competitor_stats.append({
                    "Competitor": item.get("competitor_name", "Unknown"),
                    "Market Share (%)": item.get("market_share", "Not available"),
                    "Month": item.get("month", "Not available")
                })
        else:
            print(f"Competitor data is not in the expected format: {competitor_data}")

        market_stats = []
        if isinstance(market_data, list):
            for item in market_data:
                market_stats.append({
                    "Month": item.get("month", "Not available"),
                    "Growth Rate (%)": item.get("growth_rate", "Not available")
                })
        else:
            print(f"Market data is not in the expected format: {market_data}")

        return {
            "Competitor Data": competitor_stats,
            "Market Data": market_stats
        }