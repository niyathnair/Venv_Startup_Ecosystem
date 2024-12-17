import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

class CampaignOptimizer:
    def __init__(self):
        self.performance_history = {}
        self.model = GenerativeModel(model_name="gemini-1.5-pro")

    def suggest_improvements(self, campaign_data):
        """Suggest improvements using Gemini based on campaign performance."""
        prompt = f"Suggest improvements for campaign '{campaign_data['campaign']}' with engagement rate {campaign_data['engagement_rate']}%. in 5 words"
        response = self.model.generate_content(prompt)
        suggestion = response.text.strip() if response else "No suggestion available."
        campaign_name = campaign_data['campaign']
        previous_suggestions = self.performance_history.get(campaign_name, [])
        previous_suggestions.append(suggestion)
        self.performance_history[campaign_name] = previous_suggestions
        return suggestion

    def optimize_budget(self, current_budget, performance_metrics):
        """Dynamically adjust budget using Gemini for financial optimization."""
        prompt = (f"Optimize budget based on current ROI {performance_metrics['roi']} and engagement rate {performance_metrics['engagement_rate']}% "
                  f"starting with budget ${current_budget}. in 5 words.")
        response = self.model.generate_content(prompt)
        try:
            new_budget = float(response.text.strip()) if response else current_budget
        except ValueError:
            new_budget = current_budget
        return round(new_budget, 2)

    def evaluate_campaign_performance(self, campaign_name):
        """Returns a summary of previous suggestions for a campaign."""
        return self.performance_history.get(campaign_name, ["No history available."])

    def analyze_ad_spend_efficiency(self, budget_data):
        """Use Gemini to analyze budget utilization efficiency."""
        prompt = f"Analyze ad spend efficiency for budget data: {budget_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Analysis unavailable."

    def marketing_mix_modeling(self, historical_data):
        """Perform Marketing Mix Modeling using Gemini."""
        prompt = f"Perform marketing mix modeling based on historical data: {historical_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Modeling result unavailable."

    def perform_a_b_testing(self, variations):
        """Evaluate A/B testing variations using Gemini."""
        prompt = f"Evaluate these A/B testing variations: {variations}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Best variation not determined."

    def cross_channel_attribution(self, interaction_data):
        """Evaluate marketing channel contributions using attribution modeling."""
        prompt = f"Perform cross-channel attribution analysis for interaction data: {interaction_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Attribution analysis unavailable."

    def customer_segmentation(self, customer_data):
        """Segment customers into clusters using Gemini."""
        prompt = f"Segment these customers: {customer_data}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Segmentation result unavailable."

    def real_time_monitoring(self, metrics, thresholds):
        """Trigger actions based on live campaign monitoring metrics using Gemini."""
        prompt = f"Monitor these metrics {metrics} with thresholds {thresholds}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Monitoring result unavailable."
