import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)

class CampaignModel:
    def __init__(self):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")

    def generate_message(self, product_info, market_trends):
        """Generate marketing messages based on product info and market trends."""
        prompt = f"Create a marketing message for product {product_info} considering these market trends: {market_trends}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Message generation failed."

    def score_campaign(self, campaign_text):
        """Evaluate campaign effectiveness using Gemini."""
        prompt = f"Score this campaign text based on potential effectiveness: {campaign_text}. in 5 words"
        response = self.model.generate_content(prompt)
        try:
            score = float(response.text.strip()) if response else 0.0
        except ValueError:
            score = 0.0
        return round(score, 2)

    def personalize_campaign(self, campaign_text, customer_profile):
        """Customize campaign messages based on customer profile."""
        prompt = f"Personalize this campaign text: '{campaign_text}' for this customer profile: {customer_profile}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Personalization failed."

    def optimize_campaign_language(self, campaign_text):
        """Improve campaign language for maximum engagement."""
        prompt = f"Optimize the language of this campaign text for better engagement: {campaign_text}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Language optimization failed."

    def suggest_visual_elements(self, product_info):
        """Suggest suitable visual elements for a campaign based on product information."""
        prompt = f"Suggest visual elements for a marketing campaign promoting this product: {product_info}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Visual suggestion failed."

    def generate_social_media_ad(self, campaign_text, platform):
        """Generate a platform-specific social media ad based on the campaign text."""
        prompt = f"Create a {platform} social media ad based on this campaign text: {campaign_text}. in 5 words"
        response = self.model.generate_content(prompt)
        return response.text.strip() if response else "Ad generation failed."
