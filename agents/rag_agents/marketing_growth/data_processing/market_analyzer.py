import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

class MarketAnalyzer:
    def __init__(self):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")

    def analyze_trends(self, market_data):
        """Analyze market trends using Gemini."""
        prompt = f"Analyze these market trends: {market_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Trend analysis unavailable."

    def analyze_customer_insights(self, customer_data):
        """Analyze customer insights using Gemini."""
        prompt = f"Analyze customer insights from this data: {customer_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Customer insight analysis unavailable."

    def perform_sentiment_analysis(self, feedback_data):
        """Perform sentiment analysis on customer feedback."""
        prompt = f"Perform sentiment analysis on this customer feedback: {feedback_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Sentiment analysis unavailable."

    def competitive_analysis(self, competitor_data):
        """Evaluate competitors' performance using Gemini."""
        prompt = f"Evaluate these competitors' performance: {competitor_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Competitor analysis unavailable."

    def customer_segmentation(self, customer_profiles):
        """Segment customers into clusters based on profiles."""
        prompt = f"Segment these customer profiles: {customer_profiles}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Customer segmentation unavailable."

    def forecast_market_trends(self, historical_market_data):
        """Forecast future market trends using historical data."""
        prompt = f"Forecast market trends using historical data: {historical_market_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Market trend forecasting unavailable."

    def identify_growth_opportunities(self, market_data):
        """Identify market growth opportunities using trend analysis."""
        prompt = f"Identify growth opportunities in this market data: {market_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Growth opportunities unavailable."


